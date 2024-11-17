import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ContentType
from aiogram.utils import executor

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO  # Ensure the level is set to INFO or another level you prefer
)
logger = logging.getLogger(__name__)

bot = Bot(token='')
dp = Dispatcher(bot)


# @dp.message_handler(commands=['start'])
# async def send_welcome(message: types.Message):
#     user_id = 7185696251
#     await message.reply("Assalomu Aleykum")
#     await message.answer_audio(open("chingiz_voice.ogg", "rb"))

# user_id = 5172746353
#
# @dp.message_handler(commands='start')
# async def send_welcome(message: types.Message):
#     if user_id == message.from_user.id:
#         await message.reply("Assalomu Aleykum")
#         await message.answer_audio(open("chingiz_voice.ogg", "rb"))
#     else:
#         await message.reply("Sizga dostup yo")


# @dp.message_handler(content_types=[ContentType.TEXT])
# async def handle_text(message: types.Message):
#     await message.reply("Bu TEXT!")
#     # await message.reply(message.text)


@dp.message_handler(content_types=[ContentType.PHOTO])
async def handle_photo(message: types.Message):
    await message.reply("Bu photo!")
    await message.answer_photo(open("img.jpg", "rb"))


@dp.message_handler(content_types=[ContentType.DOCUMENT])
async def handle_document(message: types.Message):
    document = message.document
    file_id = document.file_id
    file_name = document.file_name
    mime_type = document.mime_type
    file_size = document.file_size

    # Ответ бота с информацией о документе
    await message.reply(f"Вы загрузили документ:\n"
                        f"Имя файла: {file_name}\n"
                        f"Тип файла: {mime_type}\n"
                        f"Размер: {file_size} байт\n"
                        f"file_id: {file_id}")


@dp.message_handler(content_types=types.ContentType.VOICE)
async def handle_voice(message: types.Message):
    await message.reply("Bu voice")
    await message.answer_voice(open(f"chingiz_voice.ogg", "rb"))


@dp.message_handler(content_types=types.ContentType.AUDIO)
async def handle_audio(message: types.Message):
    await message.reply("Bu audio")
    await message.answer_audio(open(f"chingiz_voice.ogg", "rb"))


@dp.message_handler(content_types=types.ContentType.STICKER)
async def sticker_handler(message: types.Message):
    sticker_id = "CAACAgIAAxkBAAICJ2b-iE87TL56bDSUnZQ4z_cn2S0CAAL3GgACG7_xSdejPl2iAyNZNgQ"
    await message.answer_sticker(sticker_id)


@dp.message_handler(content_types=[ContentType.ANIMATION])
async def animation(message: types.Message):
    await message.reply("BU animation")
    await message.answer_animation(open("want.mp4", "rb"))


@dp.message_handler(commands="video")
async def video_handler(message: types.Message):
    await message.answer_video(open("tefal.mp4", "rb"))


@dp.message_handler(content_types=[ContentType.LOCATION])
async def send_location(message: types.Message):
    latitude = 41.7151
    longitude = 69.2679
    await bot.send_location(chat_id=message.chat.id, latitude=latitude, longitude=longitude)



if __name__ == '__main__':
    executor.start_polling(dp)
