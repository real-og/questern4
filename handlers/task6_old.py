# from loader import dp,  bot
# from aiogram import types
# from aiogram.dispatcher import FSMContext
# import texts
# import keyboards as kb
# from states import State
# import aiotable
# import logic
# import score
# #коды
# @dp.message_handler(state=State.task_6_3_yes)
# async def send_welcome(message: types.Message, state: FSMContext):
#     if message.text == texts.yes_btn:
#         await message.answer(texts.task6_3_3, reply_markup=kb.ready_kb)
#         await State.task_6_3_conf.set()
#     else:
#         await message.answer(texts.use_kb, reply_markup=kb.yes_kb)

# @dp.message_handler(state=State.task_6_3_conf)
# async def send_welcome(message: types.Message, state: FSMContext):
#     if message.text == texts.ready_btn:
#         await message.answer(texts.enter_answer, reply_markup=kb.get_hint_kb)
#         await State.task_6_answering.set()
#     else:
#         await message.answer(texts.use_kb, reply_markup=kb.ready_kb)

# @dp.message_handler(state=State.task_6_answering)
# async def send_welcome(message: types.Message, state: FSMContext):
#     answer = message.text
#     if message.text == texts.hint_btn:
#         await message.answer(texts.task6_hint_1, reply_markup=kb.answer_or_hint_kb)

#     elif message.text == texts.answer_btn:
#         await message.answer(texts.enter_answer, reply_markup=kb.get_hint_kb)

#     elif logic.remove_punctuation(answer.upper()) in texts.task6_wrong_ans:
#         await message.answer(texts.rigth, reply_markup=kb.get_hint_kb)
#     elif answer.upper() == texts.task6_3_ans:
#         await message.answer(texts.task_6_finish, reply_markup=kb.continue_kb)
#         await State.asking_for_continue.set()
#         await logic.notify_admins('Коды', state)
#         await aiotable.mark_cell(message.from_user.id, 6, "д")
#         await score.complete_level(message.from_id, 6)
#     else:
#         await message.answer(texts.no_part, reply_markup=kb.get_hint_kb)


# @dp.callback_query_handler(state='*')
# async def send_channels(callback: types.CallbackQuery, state: FSMContext):
#     if callback.data == 'sound':
#         await callback.message.answer(texts.task_1_finish)


