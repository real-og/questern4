from loader import dp, CODES, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable
import logic


@dp.message_handler(state=State.task_2_3)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.hint_btn:
        await message.answer(texts.task2_hint_1, reply_markup=kb.answer_or_hint_kb)
    elif message.text == texts.answer_btn:
        await message.answer(texts.enter_answer, reply_markup=kb.get_hint_kb)
        await State.task_2_answering.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.answer_or_hint_kb)


@dp.message_handler(state=State.task_2_answering)
async def send_welcome(message: types.Message, state: FSMContext):
    answer = message.text
    if message.text == texts.hint_btn:
        await message.answer(texts.task2_hint_1, reply_markup=kb.answer_or_hint_kb)
        await State.task_2_3.set()
    elif logic.remove_punctuation(answer.upper()) in texts.task2_wrong_ans:
        await message.answer(texts.no_need_question_2, reply_markup=kb.get_hint_kb)
    elif answer.upper() == texts.task2_3_ans:
        await message.answer(texts.task_2_finish, reply_markup=kb.continue_kb)
        await State.asking_for_continue.set()
    else:
        await message.answer(texts.wrong_answer, reply_markup=kb.get_hint_kb)

