from loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable
import logic
import score

#телефон
@dp.message_handler(state=State.start_confirmation)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.begin_quest_btn:
        await message.answer(texts.ask_for_victim)
        await message.answer(texts.victim_received)
        await State.entering_code_name.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.begin_quest_kb)


@dp.message_handler(state=State.task_1_answering)
async def send_welcome(message: types.Message, state: FSMContext):
    answer = message.text
    
    if message.text == texts.hint_btn:
        await message.answer(texts.task1_hint_1, reply_markup=kb.answer_or_more_hint_kb)

    elif message.text == texts.more_hint_btn:
        await message.answer(texts.task1_hint_2, reply_markup=kb.answer_or_hint_kb)

    elif message.text == texts.answer_btn:
        await message.answer(texts.enter_number, reply_markup=kb.get_hint_kb)

    elif answer.isdecimal():
        if answer == texts.task1_3_ans:
            await message.answer(texts.right_number, reply_markup=kb.phone_keyboard)
            await State.entering_phone.set()

        elif len(answer) == 11:
            await message.answer(texts.wrong_number(answer), reply_markup=kb.get_hint_kb)
        else:
            await message.answer(texts.ask_for_whole_number)
    elif logic.remove_punctuation(answer.upper()) in texts.task1_wrong_ans:
        await message.answer(texts.no_need_question, reply_markup=kb.get_hint_kb)
    else:
        await message.answer(texts.wrong_answer, reply_markup=kb.get_hint_kb)


@dp.message_handler(content_types=types.ContentType.CONTACT, state=State.entering_phone)
async def set_phone_handler(message: types.Message, state: FSMContext):
    phone = message.contact.phone_number
    await message.answer(texts.voice_received)
    with open("audios/unavailable.ogg", "rb") as file:
        file_data = file.read()
        await message.answer_voice(file_data)
    await message.answer(texts.no_sound_description, reply_markup=kb.no_sound_kb)
    await message.answer('Продолжить?', reply_markup=kb.continue_kb)
    await State.asking_for_continue.set()
    await logic.notify_admins('Телефон', state)
    await aiotable.mark_cell(message.from_user.id, 1, "д")
    await score.complete_level(message.from_id, 1)
    await aiotable.update_cell(message.from_user.id, 12, phone)

@dp.callback_query_handler(state='*')
async def send_channels(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'sound':
        await callback.message.answer(texts.task_1_finish)
        await callback.answer()