from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from asyncio import sleep

bot = Bot(token="5810830070:AAG22oUpP8joFO20DlYScOow-qnoj1ZiHOo")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

text1 = "❗Щоб активувати чек, підпишіться на канали❗"
text2 = "❗Партнери платять нам, а ми вам, підпишіться на канали та отримайте винагороду❗" 

buttons_data = {
    "Подписаться 1": "https://cryptyt.com/go/um4wOUUJMkeQXHQGUTEFQ",
    "Подписаться 2": "https://workua.info/go/bnBiPT3zmEqdE4Wcg6bFZw",
    "Подписаться 3": "https://detalno.info/go/k7MJHSC7E0uuxMgmg7pIfw",
}

buttons_data2 = {
    "Подписаться 1": "https://detalno.info/go/1gT8PgPDEqz0bjnWdgQ",
    "Подписаться 2": "https://cryptyt.com/go/2hdrwjXvEavHo15zyfWDg",
    "Подписаться 3": "https://detalno.info/go/Os5gawc0WUC3oAiB6XOXYw",
}

kb = InlineKeyboardMarkup()
kb2 = InlineKeyboardMarkup()

for label,link in buttons_data.items():
    button = InlineKeyboardButton(text=label, url = link)
    kb.add(button)

for label,link in buttons_data2.items():
    button = InlineKeyboardButton(text=label, url = link)
    kb2.add(button)


@dp.chat_join_request_handler()
async def start1(update: types.ChatJoinRequest):
    await bot.send_message(
        chat_id=update.from_user.id, 
        text=text1,
        reply_markup=kb
    )
    await sleep(45)
    await bot.send_message(
        chat_id=update.from_user.id, 
        text=text2,
        reply_markup=kb2
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
