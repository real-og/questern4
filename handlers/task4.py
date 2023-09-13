from loader import dp, CODES, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable
from handlers.menu import get_to_menu

#Фотодобыча
@dp.callback_query_handler(lambda c: c.data == texts.places_btns[3], state=State.menu)  
async def process_button1(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    completed_tasks = data.get('completed_tasks')
    if callback.data in completed_tasks:
        await callback.message.answer(texts.task_already_completed)
        await bot.answer_callback_query(callback.id)
        return
    await aiotable.set_current_level(callback.from_user.id, 4)
    
    await callback.message.answer(texts.task4, reply_markup=kb.task_completed_kb)

    completed_tasks.append(callback.data)
    await state.update_data(completed_tasks=completed_tasks)
    await State.task_4_inprogress.set()
    await bot.answer_callback_query(callback.id)


@dp.message_handler(state=State.task_4_inprogress)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.task_completed_btn:
        await message.answer(texts.ask_for_points)
        await State.task_4_points.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.task_completed_kb)
        

@dp.message_handler(state=State.task_4_points)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        with open(f'images/{message.text}1.jpg', 'rb') as photo:
            await message.answer_photo(photo)
        await aiotable.implement_score(message.from_id, 4, int(message.text))
        data = await state.get_data()
        score = data.get('score')
        await state.update_data(score=int(score) + int(message.text))
        await get_to_menu(message, state)
    else:
        await message.answer(texts.number_expected)
    