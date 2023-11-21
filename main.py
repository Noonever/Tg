from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from asyncio import sleep


bot = Bot(token="6537408071:AAEa157ruHpqCdAQTJVeu8KzjdzROd3Lw1Q")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

text1 = "Щоб вашу заявку прийняли, та чек активувався, необхідно відправити запит!"
text2 = "Обов'язково надішліть заявку на всі канали, щоб отримати гроші!" 
text3 = "Від вас потрібна лише заявка, потім можете відписатися!" 

buttons_data = {
    "Подписаться 1": "https://cryptyt.com/go/yrascEd5m0eatMhRkOyvw",
    "Подписаться 2": "https://detalno.info/go/FlkALo2LrUKXgr991KWRkQ",
    "Подписаться 3": "https://cryptyt.com/go/Rq4FN83LUe5xzxmQRKrJA",
}

buttons_data2 = {
    "Подписаться 1": "https://detalno.info/go/3C0lV58vEqgeOnA9i1OQ",
    "Подписаться 2": "https://detalno.info/go/grW7fejhG0iB6vXMiV2LrA",
}

buttons_data3 = {
    "ТУТ": "https://cryptyt.com/go/CdUTfxGrREi6WVb46u0rtw",
    "Забирай": "https://tovarpro.com/go/cbegVucNp0KoHTgoMfyO0w",
}

kb = InlineKeyboardMarkup()
kb2 = InlineKeyboardMarkup()
kb3 = InlineKeyboardMarkup()

for label,link in buttons_data.items():
    button = InlineKeyboardButton(text=label, url = link)
    kb.add(button)

for label,link in buttons_data2.items():
    button = InlineKeyboardButton(text=label, url = link)
    kb2.add(button)

for label,link in buttons_data3.items():
    button = InlineKeyboardButton(text=label, url = link)
    kb3.add(button)



@dp.chat_join_request_handler()
async def start1(update: types.ChatJoinRequest):
    await bot.send_message(
        chat_id=update.from_user.id, 
        text=text1,
        reply_markup=kb
    )
    await sleep(45 )
    await bot.send_message(
        chat_id=update.from_user.id, 
        text=text2,
        reply_markup=kb2
    )
    await sleep(45 )
    await bot.send_message(
        chat_id=update.from_user.id, 
        text=text3,
        reply_markup=kb3
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)