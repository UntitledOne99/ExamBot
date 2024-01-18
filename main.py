import asyncio
import Config
import logging
import random

from Config import STUB as stub_text
from aiogram import Bot, Dispatcher, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import CommandStart, Command
from Questionforming import Form

bot = Bot(token=Config.TOKEN)

dp = Dispatcher()
question_collection = {}
key = 'Unique'
temp = 0


def stub():
    res = random.choice(stub_text.split(' '))
    return res


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text=f"{message.from_user.id} {message.from_user.full_name}")


@dp.message(Command("exam"))
async def question_factory(message: types.Message):
    builder = InlineKeyboardBuilder()
    form = Form(stub(), key, [stub(), stub(), stub()])
    form.make_a_question(builder)
    await message.answer(f"{form.question} ?", reply_markup=builder.as_markup())


@dp.callback_query((F.data).endswith(f'{key}'))
async def user_answer_handler(callback: types.CallbackQuery):
    if callback.message.text not in question_collection.keys():
        question_collection[callback.message.text] = callback.data.split(' ')[0]
        await question_factory(callback.message)
    print(question_collection.items())


async def main():
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
