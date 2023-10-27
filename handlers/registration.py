from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable


@dp.message_handler(state=State.entering_name)
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.generate_confirmation_msg(message.text), reply_markup=kb.yes_no_kb)
    await state.update_data(team_name=message.text)
    await State.confirmation_name.set()

@dp.message_handler(state=State.confirmation_name)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.yes_btn:
        data = await state.get_data()

        with open('audios/saw.gif', 'rb') as video:
            await message.answer_animation(video)

        # with open('audios/saw.MOV', 'rb') as video:
        #     await message.answer_animation(video, caption=texts.succes_registrated, reply_markup=kb.begin_quest_kb)

        await message.answer(texts.succes_registrated, reply_markup=kb.begin_quest_kb)
        await State.start_confirmation.set()
        await aiotable.append_user(message.from_user.id, message.from_user.username, data.get('team_name'))
    elif message.text == texts.no_btn:
        await message.answer(texts.enter_another_name)
        await State.entering_name.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.yes_no_kb)

