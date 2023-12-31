from loader import dp,  bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable
import logic
import score
#фотографии
@dp.message_handler(state=State.task_5_3)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.uploaded_btn:
        await message.answer(texts.task_5_finish, reply_markup=kb.continue_kb)
        await State.asking_for_continue.set()
        await logic.notify_admins('Фотографии', state)
        await aiotable.mark_cell(message.from_user.id, 5, "д")
        await score.complete_level(message.from_id, 5)
    else:
        await message.answer(texts.use_kb, reply_markup=kb.photoes_uploaded_kb)
