from loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable
import logic
import score


#ультрафиолет
@dp.message_handler(state=State.task_2_answering)
async def send_welcome(message: types.Message, state: FSMContext):
    answer = message.text
    if message.text == texts.hint_btn:
        await message.answer(texts.task2_hint_1, reply_markup=kb.answer_or_hint_kb)


    elif message.text == texts.answer_btn:
        await message.answer(texts.enter_answer, reply_markup=kb.get_hint_kb)

    elif logic.remove_punctuation(answer.upper()) in texts.task2_wrong_ans:
        ans = texts.task2_wrong_ans.get(logic.remove_punctuation(message.text.upper()))
        await message.answer(ans, reply_markup=kb.get_hint_kb)

    elif answer.upper() == texts.task2_3_ans:
        await message.answer(texts.task_2_finish, reply_markup=kb.continue_kb)
        await State.asking_for_continue.set()
        await logic.notify_admins('Ультрафиолет', state)
        await aiotable.mark_cell(message.from_user.id, 2, "д")
        await score.complete_level(message.from_id, 2)
    else:
        await message.answer(texts.wrong_answer, reply_markup=kb.get_hint_kb)

