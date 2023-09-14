from loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable
import logic


@dp.message_handler(state=State.start_confirmation)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.begin_quest_btn:
        await message.answer(texts.ask_for_victim)
        await State.choosing_a_victim.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.begin_quest_kb)


@dp.message_handler(state=State.task_1_3)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.hint_btn:
        await message.answer(texts.task1_hint_1, reply_markup=kb.answer_or_more_hint_kb)
    elif message.text == texts.more_hint_btn:
        await message.answer(texts.task1_hint_2, reply_markup=kb.answer_or_hint_kb)
    elif message.text == texts.answer_btn:
        await message.answer(texts.enter_number, reply_markup=kb.get_hint_kb)
        await State.task_1_answering.set()
    else:
        await message.answer(texts.use_a_button, reply_markup=kb.answer_or_hint_kb)


@dp.message_handler(state=State.task_1_answering)
async def send_welcome(message: types.Message, state: FSMContext):
    answer = message.text
    if message.text == texts.hint_btn:
        await message.answer(texts.task1_hint_1, reply_markup=kb.answer_or_more_hint_kb)
        await State.task_1_3.set()
    elif answer.isdecimal():
        if answer == texts.task1_3_ans:
            # await message.answer(texts.task_1_finish, reply_markup=kb.continue_kb)
            with open("audios/unavailable.ogg", "rb") as file:
                file_data = file.read()
                await message.answer_voice(file_data, reply_markup=kb.continue_kb)
            await State.asking_for_continue.set()
            await logic.notify_admins('Телефон', state)
            await aiotable.mark_cell(message.from_user.id, 1, "д")
        elif len(answer) == 11:
            await message.answer(texts.wrong_number(answer), reply_markup=kb.get_hint_kb)
        else:
            await message.answer(texts.ask_for_whole_number)
    elif logic.remove_punctuation(answer.upper()) in texts.task1_wrong_ans:
        await message.answer(texts.no_need_question, reply_markup=kb.get_hint_kb)
    else:
        await message.answer(texts.wrong_answer, reply_markup=kb.get_hint_kb)

