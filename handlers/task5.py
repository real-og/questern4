from loader import dp, CODES, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import logic
import aiotable
from handlers.menu import get_to_menu

#Числошифры
@dp.callback_query_handler(lambda c: c.data == texts.places_btns[4], state=State.menu)  
async def process_button1(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    completed_tasks = data.get('completed_tasks')
    if callback.data in completed_tasks:
        await callback.message.answer(texts.task_already_completed)
        await bot.answer_callback_query(callback.id)
        return
    await aiotable.set_current_level(callback.from_user.id, 5)
    
    await callback.message.answer(texts.task5)

    completed_tasks.append(callback.data)
    await state.update_data(completed_tasks=completed_tasks)
    if data.get('task_5_answered') is None:
        await state.update_data(task_5_answered = [])
    await State.task_5.set()
    await bot.answer_callback_query(callback.id)

@dp.message_handler(state=State.task_5)
async def send_welcome(message: types.Message, state: FSMContext):
    data = await state.get_data()
    task_5_answered = data.get('task_5_answered')
    answer = logic.remove_punctuation(message.text.upper())
    if answer in texts.task5_ans.keys():
        if texts.task5_ans.get(answer) not in task_5_answered:
            with open('images/11.jpg', 'rb') as photo:
                await message.answer_photo(photo, reply_markup=kb.finish_task_kb, caption=texts.correct_ans_header)
            await aiotable.implement_score(message.from_id, 5, 1)
            task_5_answered.append(texts.task5_ans.get(answer))
            await state.update_data(task_5_answered=task_5_answered)
            score = data.get('score')
            await state.update_data(score=int(score) + 1)
        else:
            await message.answer(texts.already_answered, reply_markup=kb.finish_task_kb)
    elif message.text == texts.finish_task_btn:
        await message.answer(texts.confirm_task_finish, reply_markup=kb.yes_no_kb)
        await State.task_5_exit.set()
    else:
        await message.answer(texts.wrong_answer, reply_markup=kb.finish_task_kb)


@dp.message_handler(state=State.task_5_exit)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.yes_btn:
        await get_to_menu(message, state)
    elif message.text == texts.no_btn:
        await message.answer(texts.task1)
        await State.task_5.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.yes_no_kb)


