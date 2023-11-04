from loader import dp,  bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable
import logic


#подарки
@dp.message_handler(state=State.task_4_answering)
async def send_welcome(message: types.Message, state: FSMContext):
    answer = message.text.replace('ё', 'е')
    print(answer)
    if message.text == texts.hint_btn:
        await message.answer(texts.task4_hint_1, reply_markup=kb.answer_or_more_hint_kb)

    elif message.text == texts.answer_btn:
        await message.answer(texts.enter_answer, reply_markup=kb.get_hint_kb)

    elif message.text == texts.more_hint_btn:
        await message.answer(texts.task4_hint_2, reply_markup=kb.answer_or_more_hint2_kb)

    elif message.text == texts.more_hint2_btn:
        await message.answer(texts.task4_hint_3, reply_markup=kb.answer_or_hint_kb)

    elif logic.remove_punctuation(answer.upper()) in texts.task4_wrong_ans:
        ans = texts.task4_wrong_ans.get(logic.remove_punctuation(answer.upper()))
        await message.answer(ans, reply_markup=kb.get_hint_kb)
    elif answer.upper() == texts.task4_3_ans:
        await message.answer(texts.task_4_finish, reply_markup=kb.continue_kb)
        await State.asking_for_continue.set()
        await logic.notify_admins('Подарки', state)
        await aiotable.mark_cell(message.from_user.id, 4, "д")
    else:
        await message.answer(texts.wrong_answer, reply_markup=kb.get_hint_kb)

