from loader import dp, bot
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable
import logic


@dp.message_handler(state=State.asking_for_continue)
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == texts.continue_btn:
        status_victim = logic.get_status()
        if status_victim == "b'0'":
            await message.answer(texts.enter_code_w)
            await State.entering_code_name.set()
            return
        await message.answer(texts.ask_for_victim)
        await message.answer(texts.victim_received)
        await State.entering_code_name.set()
        # await State.choosing_a_victim.set()
    else:
        await message.answer(texts.use_kb, reply_markup=kb.continue_kb)


# @dp.message_handler(state=State.choosing_a_victim)
# async def send_welcome(message: types.Message, state: FSMContext):
#     if message.text == texts.victim_chosen_btn:
#         await message.answer(texts.victim_received)
#         await State.entering_code_name.set()
#     else:
#         await message.answer(texts.use_kb, reply_markup=kb.victim_chosen_kb)


@dp.message_handler(state=State.entering_code_name)
async def send_welcome(message: types.Message, state: FSMContext):
    code_word = message.text.upper()
    if code_word == texts.task1_2_ans:
        await message.answer(texts.task1_3_1)
        await message.answer(texts.task1_3_2, reply_markup=kb.get_hint_kb)
        await State.task_1_answering.set()
        await aiotable.mark_cell(message.from_user.id, 1, "Здесь")

    elif code_word == texts.task2_2_ans:
        await message.answer(texts.task2_3, reply_markup=kb.answer_or_hint_kb)
        await State.task_2_answering.set()
        await aiotable.mark_cell(message.from_user.id, 2, "Здесь")

    elif code_word == texts.task5_2_ans:
        await message.answer(texts.task5_3_1)
        await message.answer(texts.task5_3_2)
        await message.answer(texts.ask_for_btn_photoes, reply_markup=kb.photoes_uploaded_kb)
        await State.task_5_3.set()
        await aiotable.mark_cell(message.from_user.id, 5, "Здесь")

    elif message.text.upper() == texts.task7_2_ans:
        await message.answer(texts.task7_3, reply_markup=kb.done_kb)
        await State.task_7_3.set()
        await aiotable.mark_cell(message.from_user.id, 7, "Здесь")

    elif code_word == texts.task3_2_ans:
        await message.answer(texts.task3_3, reply_markup=kb.answer_or_hint_kb)
        await State.task_3_answering.set()
        await aiotable.mark_cell(message.from_user.id, 3, "Здесь")

    elif code_word == texts.task4_2_ans:
        await message.answer(texts.task4_3, reply_markup=kb.answer_or_hint_kb)
        await State.task_4_answering.set()
        await aiotable.mark_cell(message.from_user.id, 4, "Здесь")

    elif code_word == texts.task6_2_ans:
        # await message.answer(texts.task6_3_1)
        # await message.answer(texts.task6_3_2, reply_markup=kb.yes_kb)
        await message.answer(texts.task6_new1)
        await message.answer(texts.task6_new2, reply_markup=kb.answer_or_hint_kb)
        # await State.task_6_3_yes.set()
        await State.task_6_answering.set()
        await aiotable.mark_cell(message.from_user.id, 6, "Здесь")

    elif code_word == texts.exit_word:
        await message.answer(texts.ending)
        # with open('images/final_video.gif', 'rb') as video:
        #     await message.answer_animation(video)
        with open('images/final_video.MOV', 'rb') as video:
            await message.answer_video(video)
        await aiotable.mark_cell(message.from_user.id, 8, "Здесь")

    else:
        await message.answer(texts.wrong_code_word)

