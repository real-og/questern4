from loader import dp,  bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable
import logic


@dp.message_handler(state=State.task_6_3)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.hint_btn:
        await message.answer(texts.task6_hint_1, reply_markup=kb.answer_or_hint_kb)
    elif message.text == texts.answer_btn:
        await message.answer(texts.enter_answer, reply_markup=kb.get_hint_kb)
        await State.task_6_answering.set()
    else:
        await message.answer(texts.use_a_button, reply_markup=kb.answer_or_hint_kb)


@dp.message_handler(state=State.task_6_answering)
async def send_welcome(message: types.Message, state: FSMContext):
    answer = message.text
    if message.text == texts.hint_btn:
        await message.answer(texts.task6_hint_1, reply_markup=kb.answer_or_hint_kb)
        await State.task_6_3.set()
    elif logic.remove_punctuation(answer.upper()) in texts.task6_wrong_ans:
        await message.answer(texts.no_need_question_6, reply_markup=kb.get_hint_kb)
    elif answer.upper() == texts.task6_3_ans:
        await message.answer(texts.task_6_finish, reply_markup=kb.continue_kb)
        await State.asking_for_continue.set()
        await logic.notify_admins('QR-код', state)
        await aiotable.mark_cell(message.from_user.id, 6, "д")
    else:
        await message.answer(texts.wrong_answer, reply_markup=kb.get_hint_kb)

