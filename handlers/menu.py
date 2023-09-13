from loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable


@dp.message_handler(state=State.asking_for_continue)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.continue_btn:
        await message.answer(texts.ask_for_victim, reply_markup=kb.victim_chosen_kb)
        await State.choosing_a_victim.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.continue_kb)
        

@dp.message_handler(state=State.choosing_a_victim)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.victim_chosen_btn:
        await message.answer(texts.ask_for_codeword)
        await State.entering_code_name.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.victim_chosen_kb)


@dp.message_handler(state=State.entering_code_name)
async def send_welcome(message: types.Message, state: FSMContext):
    code_word = message.text.upper()
    if code_word == texts.task1_2_ans:
        await message.answer(texts.task1_3, reply_markup=kb.answer_or_hint_kb)
        await State.task_1_3.set()

    elif code_word == texts.task2_2_ans:
        await message.answer(texts.task2_3, reply_markup=kb.answer_or_hint_kb)
        await State.task_2_3.set()

    elif code_word == texts.task5_2_ans:
        await message.answer(texts.task5_3, reply_markup=kb.photoes_uploaded_kb)
        with open('images/qr.png', 'rb') as photo:
                await message.answer_photo(photo)
        await State.task_5_3.set()

    elif message.text.upper() == texts.task7_2_ans:
        await message.answer(texts.task7_3, reply_markup=kb.done_kb)
        await State.task_7_3.set()

    elif code_word == texts.task3_2_ans:
        await message.answer(texts.task3_3, reply_markup=kb.answer_or_hint_kb)
        await State.task_3_3.set()

    elif code_word == texts.task4_2_ans:
        await message.answer(texts.task4_3, reply_markup=kb.answer_or_hint_kb)
        await State.task_4_3.set()

    elif code_word in texts.task6_2_ans:
        await message.answer(texts.task6_3, reply_markup=kb.answer_or_hint_kb)
        await State.task_6_3.set()

    else:
        await message.answer(texts.wrong_answer)

