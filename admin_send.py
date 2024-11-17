import sqlite3
import logging
from aiogram import Dispatcher, types, Bot
from aiogram.utils import executor
from aiogram.types import ContentType

ADMIN_ID = 6812498519

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


API_TOKEN = ""

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Function to send detailed user info to admin
async def send_message_to_admin(user: types.User, message_text: str):
    user_info = (
        f"Пользователь:\n"
        f"ID: {user.id}\n"
        f"Имя: {user.first_name}\n"
        f"Фамилия: {user.last_name if user.last_name else 'Не указана'}\n"
        f"Username: @{user.username if user.username else 'Не указан'}\n"
        f"Язык: {user.language_code}\n"
        f"Бот: {'Да' if user.is_bot else 'Нет'}\n\n"
        f"Сообщение пользователя: \"{message_text}\""
    )

    await bot.send_message(ADMIN_ID, user_info)


# Function to notify admin that the bot has started
async def notify_admin_bot_started():
    await bot.send_message(ADMIN_ID, "Run Bot")


# Handler for /start command
@dp.message_handler(commands='start')
async def process_start_command(message: types.Message):
    user = message.from_user
    message_text = message.text
    await send_message_to_admin(user, message_text)
    # await message.answer("Send message... Please wait!")
    print(user, message_text)


# Handler for all text messages
@dp.message_handler(content_types=ContentType.TEXT)
async def handle_text_message(message: types.Message):
    user = message.from_user
    message_text = message.text
    await send_message_to_admin(user, message_text)
    print(user, message_text)


# Notify admin when bot starts and start polling
if __name__ == '__main__':
    from aiogram import executor


    # Отправляем уведомление админу, когда бот запускается
    async def on_startup(dp):
        await notify_admin_bot_started()


    # Запускаем бота с уведомлением для админа
    executor.start_polling(dp, on_startup=on_startup, skip_updates=False)
