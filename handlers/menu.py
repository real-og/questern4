from loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable


@dp.message_handler(state=State.asking_for_continue)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.continue_btn:
        await message.answer(texts.ask_for_victim)
        await State.choosing_a_victim.set()


@dp.message_handler(state=State.choosing_a_victim)
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.generate_confirmation_victim_msg(message.text), reply_markup=kb.yes_no_kb)
    await State.confirmation_victim.set()


@dp.message_handler(state=State.confirmation_victim)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.yes_btn:
        await message.answer(texts.ask_photo_victim)
        await State.entering_photo_victim.set()
    elif message.text == texts.no_btn:
        await message.answer(texts.enter_another_victim)
        await State.choosing_a_victim.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.yes_no_kb)


@dp.message_handler(state=State.entering_photo_victim, content_types=['any'])
async def send_welcome(message: types.Message, state: FSMContext):
    if message.content_type in ['photo', 'document']:
        await message.answer(texts.photo_received)
        await State.entering_code_name.set()
    else:
        await message.answer(texts.send_photo)


@dp.message_handler(state=State.entering_code_name)
async def send_welcome(message: types.Message, state: FSMContext):
    code_word = message.text.upper()
    if code_word == texts.task1_2_ans:
        await message.answer(texts.task1_3, reply_markup=kb.answer_or_hint_kb)
        await State.task_1_3.set()
        await aiotable.mark_cell(message.from_user.id, 1, "Здесь")

    elif code_word == texts.task2_2_ans:
        await message.answer(texts.task2_3, reply_markup=kb.answer_or_hint_kb)
        await State.task_2_3.set()
        await aiotable.mark_cell(message.from_user.id, 2, "Здесь")

    elif code_word == texts.task5_2_ans:
        await message.answer(texts.task5_3_1)
        await message.answer(texts.task5_3_2)
        with open('images/qr.png', 'rb') as photo:
                await message.answer_photo(photo,
                                            reply_markup=kb.photoes_uploaded_kb,
                                            caption=texts.task5_3_3)
        await State.task_5_3.set()
        await aiotable.mark_cell(message.from_user.id, 5, "Здесь")

    elif message.text.upper() == texts.task7_2_ans:
        await message.answer(texts.task7_3, reply_markup=kb.done_kb)
        await State.task_7_3.set()
        await aiotable.mark_cell(message.from_user.id, 7, "Здесь")

    elif code_word == texts.task3_2_ans:
        await message.answer(texts.task3_3, reply_markup=kb.answer_or_hint_kb)
        await State.task_3_3.set()
        await aiotable.mark_cell(message.from_user.id, 3, "Здесь")

    elif code_word == texts.task4_2_ans:
        await message.answer(texts.task4_3, reply_markup=kb.answer_or_hint_kb)
        await State.task_4_3.set()
        await aiotable.mark_cell(message.from_user.id, 4, "Здесь")

    elif code_word == texts.task6_2_ans:
        await message.answer(texts.task6_3_1)
        await message.answer(texts.task6_3_2, reply_markup=kb.yes_kb)
        await State.task_6_3_yes.set()
        await aiotable.mark_cell(message.from_user.id, 6, "Здесь")

    elif code_word == texts.exit_word:
        await message.answer(texts.ending)
        with open('images/final_video.MOV', 'rb') as video:
                await message.answer_video(video)
        await aiotable.mark_cell(message.from_user.id, 8, "Здесь")

    else:
        await message.answer(texts.wrong_answer)

