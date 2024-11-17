from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
import math

bot = Bot(token="7846426508:AAGyv47GaBX2p85RqCpBjaDhDvfJTAD2KRU")
dp = Dispatcher(bot)

my_list = [f"Button {i}" for i in range(1, 12)]

ITEMS_PER_PAGE = 10


def create_keyboard(page=1):
    keyboard = InlineKeyboardMarkup(row_width=2)

    total_pages = math.ceil(len(my_list) / ITEMS_PER_PAGE)
    start_index = (page - 1) * ITEMS_PER_PAGE
    end_index = min(start_index + ITEMS_PER_PAGE, len(my_list))


    for i in range(start_index, end_index, 2):
        row_buttons = []
        if i < len(my_list):
            row_buttons.append(InlineKeyboardButton(my_list[i], callback_data=f"btn_{i}"))
        if i + 1 < len(my_list):
            row_buttons.append(InlineKeyboardButton(my_list[i + 1], callback_data=f"btn_{i + 1}"))
        keyboard.row(*row_buttons)

    navigation_buttons = []
    if page > 1:
        navigation_buttons.append(InlineKeyboardButton("←", callback_data=f"page_{page - 1}"))

    navigation_buttons.append(InlineKeyboardButton(f"{page}/{total_pages}", callback_data="current_page"))

    if page < total_pages:
        navigation_buttons.append(InlineKeyboardButton("→", callback_data=f"page_{page + 1}"))

    keyboard.row(*navigation_buttons)

    return keyboard


@dp.message_handler(commands="start")
async def send_welcome(message: types.Message):
    await message.answer("Выберите кнопку:", reply_markup=create_keyboard(page=1))


@dp.callback_query_handler(lambda c: c.data.startswith("page_"))
async def process_page_navigation(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    page = int(callback_query.data.split("_")[1])
    await bot.send_message(callback_query.from_user.id, f"{page}:", reply_markup=create_keyboard(page=page))


#
# @dp.callback_query_handler(lambda c: c.data.startswith("btn_"))
# async def process_callback_button(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     button_id = callback_query.data.split("_")[1]
#     await bot.send_message(callback_query.from_user.id, f"Вы нажали кнопку {my_list[int(button_id)]}")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
