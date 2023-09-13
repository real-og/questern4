from loader import dp, CODES, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable
import logic


@dp.message_handler(state=State.task_3_finished)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.continue_btn:
        await message.answer(texts.ask_for_victim, reply_markup=kb.victim_chosen_kb)
        await State.task_4_1.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.continue_kb)


@dp.message_handler(state=State.task_4_1)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.victim_chosen_btn:
        await message.answer(texts.ask_for_codeword )
        await State.task_4_2.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.victim_chosen_kb)


@dp.message_handler(state=State.task_4_2)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text.upper() == texts.task4_2_ans:
        await message.answer(texts.task4_3, reply_markup=kb.answer_or_hint_kb)
        await State.task_4_3.set()
    else:
        await message.answer(texts.wrong_answer)


@dp.message_handler(state=State.task_4_3)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.hint_btn:
        await message.answer(texts.task4_hint_1, reply_markup=kb.answer_or_more_hint_kb)
    elif message.text == texts.more_hint_btn:
        await message.answer(texts.task4_hint_2, reply_markup=kb.answer_or_more_hint2_kb)
    elif message.text == texts.more_hint2_btn:
        await message.answer(texts.task4_hint_3, reply_markup=kb.answer_or_hint_kb)
    elif message.text == texts.answer_btn:
        await message.answer(texts.enter_answer, reply_markup=kb.get_hint_kb)
        await State.task_4_answering.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.answer_or_hint_kb)


@dp.message_handler(state=State.task_4_answering)
async def send_welcome(message: types.Message, state: FSMContext):
    answer = message.text
    if message.text == texts.hint_btn:
        await message.answer(texts.task4_hint_1, reply_markup=kb.answer_or_more_hint_kb)
        await State.task_4_3.set()
    elif message.text == texts.more_hint_btn:
        await message.answer(texts.task4_hint_2, reply_markup=kb.answer_or_more_hint2_kb)
        await State.task_4_3.set()
    elif message.text == texts.more_hint2_btn:
        await message.answer(texts.task4_hint_3, reply_markup=kb.answer_or_hint_kb)
        await State.task_4_3.set()
    elif logic.remove_punctuation(answer.upper()) in texts.task4_wrong_ans:
        await message.answer(texts.no_need_question_2, reply_markup=kb.get_hint_kb)
    elif answer.upper() == texts.task4_3_ans:
        await message.answer(texts.task_4_finish, reply_markup=kb.continue_kb)
        await State.task_4_finished.set()
    else:
        await message.answer(texts.wrong_answer, reply_markup=kb.get_hint_kb)

