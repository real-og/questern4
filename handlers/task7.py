from loader import dp, CODES, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable
import logic


@dp.message_handler(state=State.task_6_finished)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.continue_btn:
        await message.answer(texts.ask_for_victim, reply_markup=kb.victim_chosen_kb)
        await State.task_7_1.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.continue_kb)


@dp.message_handler(state=State.task_7_1)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.victim_chosen_btn:
        await message.answer(texts.ask_for_codeword)
        await State.task_7_2.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.victim_chosen_kb)


@dp.message_handler(state=State.task_7_2)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text.upper() == texts.task7_2_ans:
        await message.answer(texts.task7_3, reply_markup=kb.done_kb)
        await State.task_7_3.set()
    else:
        await message.answer(texts.wrong_answer)


@dp.message_handler(state=State.task_7_3)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.done_btn:
        await message.answer(texts.task_7_finish, reply_markup=kb.continue_kb)
        await State.task_7_finished.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.done_kb)

