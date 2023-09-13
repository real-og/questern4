from loader import dp, CODES, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable
import logic


@dp.message_handler(state=State.task_7_3)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.done_btn:
        await message.answer(texts.task_7_finish, reply_markup=kb.continue_kb)
        await State.asking_for_continue.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.done_kb)

