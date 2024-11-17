import logging

from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor
from aiogram.types import ContentType, InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)
bot = Bot(token='')
dp = Dispatcher(bot)

my_list = [f"{i}" for i in range(1, 14)]
page_size = 10


def get_buttons(page=1):
    start = (page - 1) * page_size
    end = start + page_size
    page_items = my_list[start:end]
    total = (len(my_list) + page_size - 1) // page_size

    buttons = InlineKeyboardMarkup(row_width=2)

    for i in range(start, end, 2):
        row_buttons = []
        if i < len(my_list):
            row_buttons.append(InlineKeyboardButton(my_list[i], callback_data=f"btn_{i}"))
        if i + 1 < len(my_list):
            row_buttons.append(InlineKeyboardButton(my_list[i + 1], callback_data=f"btn_{i + 1}"))
        # buttons.row(*row_buttons)

    page_change = InlineKeyboardButton(text=f'{page}/{total}', callback_data='current_page')
    buttons.add(page_change)
    navigation = []
    if page > 1:
        navigation.append(InlineKeyboardButton(text="<", callback_data=f'page_{page - 1}'))

    if page < total:
        navigation.append(InlineKeyboardButton(text=">", callback_data=f"page_{page + 1}"))

    buttons.row(*navigation)

    return buttons


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer("hello", reply_markup=get_buttons(page=1))


@dp.callback_query_handler(lambda c: c.data and c.data.startswith("page_"))
async def paginate_callback(callback_query: types.CallbackQuery):
    page = int(callback_query.data.split("_")[1])
    await callback_query.message.edit_reply_markup(reply_markup=get_buttons(page))

#

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
