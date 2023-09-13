from loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable


@dp.message_handler(state=State.start_confirmation)
async def get_to_menu(message: types.Message, state: FSMContext):
    data = await state.get_data()
    completed_tasks = data.get('completed_tasks')
    if len(completed_tasks) == 7:
        score = data.get('score')
        await message.answer(texts.congrats1)
        await message.answer(texts.generate_final_score(score))
        await message.answer(texts.congrats2)
        await message.answer(texts.congrats3)
        await State.finished.set()
        return
    
    chat = await bot.get_chat(message.chat.id)
    if not chat.pinned_message:           
        with open('images/map.jpg', 'rb') as photo:
            mes = await message.answer_photo(photo, caption=texts.map_instruction)
        await mes.pin(disable_notification=True)
        
    await message.answer(texts.route_instruction)
    team_number = data.get('team_number')
    await message.answer(texts.route_header, reply_markup=kb.generate_locations_kb(team_number, completed_tasks))
    await State.menu.set()

@dp.message_handler(state=State.finished)
async def ge(message: types.Message, state: FSMContext):
    await message.answer(texts.quest_finished)

