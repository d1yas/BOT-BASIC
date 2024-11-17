import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware

API_TOKEN = ''

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Храним ID пользователей, которые ждут собеседника
waiting_users = set()

# Храним пары пользователей, которые сейчас общаются
chat_pairs = {}


# Команда /start
@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
    user_id = message.from_user.id

    # Если пользователь уже находится в чате
    if user_id in chat_pairs:
        await message.answer("Вы уже находитесь в чате!")
        return

    # Если есть пользователи, которые ждут собеседника, соединяем их
    if waiting_users:
        partner_id = waiting_users.pop()  # Берем пользователя, который ждет
        chat_pairs[user_id] = partner_id
        chat_pairs[partner_id] = user_id

        await bot.send_message(partner_id, "Найден собеседник! Вы можете начинать общение.")
        await message.answer("Найден собеседник! Вы можете начинать общение.")
    else:
        # Если никто не ждет, добавляем пользователя в ожидание
        waiting_users.add(user_id)
        await message.answer("Ожидание собеседника...")


# Пересылка сообщений
@dp.message_handler()
async def message_handler(message: types.Message):
    user_id = message.from_user.id

    # Проверяем, находится ли пользователь в чате
    if user_id not in chat_pairs:
        await message.answer("Вы не находитесь в чате. Отправьте /start, чтобы начать поиск собеседника.")
        return

    # Пересылаем сообщение собеседнику
    partner_id = chat_pairs[user_id]
    await bot.send_message(partner_id, message.text)


# Команда /stop для выхода из чата
@dp.message_handler(commands='stop')
async def stop_handler(message: types.Message):
    user_id = message.from_user.id

    # Если пользователь не находится в чате
    if user_id not in chat_pairs:
        await message.answer("Вы не находитесь в чате.")
        return

    # Завершаем чат
    partner_id = chat_pairs.pop(user_id)
    chat_pairs.pop(partner_id, None)

    await bot.send_message(partner_id, "Ваш собеседник покинул чат. Отправьте /start, чтобы найти нового.")
    await message.answer("Вы покинули чат. Отправьте /start, чтобы найти нового собеседника.")


# Команда /cancel для выхода из очереди ожидания
@dp.message_handler(commands='cancel')
async def cancel_handler(message: types.Message):
    user_id = message.from_user.id

    # Если пользователь не ждет собеседника
    if user_id not in waiting_users:
        await message.answer("Вы не находитесь в режиме ожидания.")
        return

    # Убираем пользователя из списка ожидания
    waiting_users.remove(user_id)
    await message.answer("Вы покинули очередь ожидания.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
