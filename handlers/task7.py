from loader import dp,  bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable
import logic

#камера
@dp.message_handler(state=State.task_7_3)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.done_btn:
        await message.answer(texts.task_7_finish, reply_markup=kb.continue_kb)
        await State.asking_for_continue.set()
        await logic.notify_admins('Камера', state)
        await aiotable.mark_cell(message.from_user.id, 7, "д")
    else:
        await message.answer(texts.use_a_button, reply_markup=kb.done_kb)

