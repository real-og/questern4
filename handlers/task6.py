from loader import dp, CODES, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable
from handlers.menu import get_to_menu

#танцевальный баттл
@dp.callback_query_handler(lambda c: c.data == texts.places_btns[5], state=State.menu)  
async def process_button1(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    completed_tasks = data.get('completed_tasks')
    if callback.data in completed_tasks:
        await callback.message.answer(texts.task_already_completed)
        await bot.answer_callback_query(callback.id)
        return
    await aiotable.set_current_level(callback.from_user.id, 6)
    
    await callback.message.answer(texts.task6, reply_markup=kb.task_completed_kb)

    completed_tasks.append(callback.data)
    await state.update_data(completed_tasks=completed_tasks)
    await State.task_6_inprogress.set()
    await bot.answer_callback_query(callback.id)


@dp.message_handler(state=State.task_6_inprogress)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.task_completed_btn:
        await message.answer(texts.task6_2)
        await State.task_6_keyword_entering.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.task_completed_kb)

@dp.message_handler(state=State.task_6_keyword_entering)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text.upper() == texts.task6_ans:
        with open('images/51.jpg', 'rb') as photo:
            await message.answer_photo(photo)
        await aiotable.implement_score(message.from_id, 6, 5)
        data = await state.get_data()
        score = data.get('score')
        await state.update_data(score=int(score) + 5)
        await get_to_menu(message, state)
    else:
        await message.answer(texts.wrong_answer)
        

