from loader import dp, CODES, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable
from handlers.menu import get_to_menu

#Роспись касок
@dp.callback_query_handler(lambda c: c.data == texts.places_btns[2], state=State.menu)  
async def process_button1(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    completed_tasks = data.get('completed_tasks')
    if callback.data in completed_tasks:
        await callback.message.answer(texts.task_already_completed)
        await bot.answer_callback_query(callback.id)
        return
    await aiotable.set_current_level(callback.from_user.id, 3)
    await callback.message.answer(texts.task3)
    completed_tasks.append(callback.data)
    await state.update_data(completed_tasks=completed_tasks)
    await State.task_3_to_start.set()
    await bot.answer_callback_query(callback.id)


@dp.message_handler(state=State.task_3_to_start, content_types=['any'])
async def send_welcome(message: types.Message, state: FSMContext):
    if message.content_type in ['photo', 'document']:
        await message.send_copy(6150574145)
        await bot.send_message(6150574145, str(message.from_user.id))
        await message.answer(texts.task3_2, reply_markup=kb.helmet_kb)
        await State.helmet_decision.set()
    else:
        await message.answer(texts.send_photo)
        


@dp.message_handler(state=State.helmet_decision)
async def send_welcome(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if message.text == texts.take_helmet_btn:
        await bot.send_message(6150574145, str(message.from_user.id) + ' take')
        with open('images/51.jpg', 'rb') as photo:
            await message.answer_photo(photo)
        await aiotable.implement_score(message.from_id, 3, 5)
        score = data.get('score')
        await state.update_data(score=int(score) + 5)
        await get_to_menu(message, state)
    elif message.text == texts.give_helmet_btn:
        await bot.send_message(6150574145, str(message.from_user.id) + ' give')
        with open('images/101.jpg', 'rb') as photo:
            await message.answer_photo(photo)
        await aiotable.implement_score(message.from_id, 3, 10)
        score = data.get('score')
        await state.update_data(score=int(score) + 10)
        await get_to_menu(message, state)
    else:
        await message.answer(texts.use_kb, reply_markup=kb.helmet_kb)

    

