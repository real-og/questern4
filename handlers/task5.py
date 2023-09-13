from loader import dp, CODES, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable
import logic


@dp.message_handler(state=State.task_4_finished)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.continue_btn:
        await message.answer(texts.ask_for_victim, reply_markup=kb.victim_chosen_kb)
        await State.task_5_1.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.continue_kb)


@dp.message_handler(state=State.task_5_1)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.victim_chosen_btn:
        await message.answer(texts.ask_for_codeword )
        await State.task_5_2.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.victim_chosen_kb)


@dp.message_handler(state=State.task_5_2)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text.upper() == texts.task5_2_ans:
        await message.answer(texts.task5_3, reply_markup=kb.photoes_uploaded_kb)
        with open('images/qr.png', 'rb') as photo:
                await message.answer_photo(photo)
        await State.task_5_3.set()
    else:
        await message.answer(texts.wrong_answer)


@dp.message_handler(state=State.task_5_3)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.uploaded_btn:
        await message.answer(texts.task_5_finish, reply_markup=kb.continue_kb)
        await State.task_5_finished.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.photoes_uploaded_kb)
