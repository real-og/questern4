from loader import dp, ADMIN_IDS, bot 
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
import aiotable
import logic
from aiogram.dispatcher import filters
import score



@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    await score.complete_level(message.from_id, 1)
    await message.answer(texts.welcome)
    await State.entering_name.set()


@dp.message_handler(commands=['help'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.help_message)


@dp.message_handler(commands=['send_hint'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    if str(message.from_user.id) not in ADMIN_IDS:
        return
    ids = await aiotable.get_ids()
    for id in ids[1:]:
        print(id)
        try:
            await bot.send_message(id, texts.task3_hint_2)
        except:
            print(f'Не отправлена подсказка для {id}')


@dp.message_handler(commands=['status'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    if str(message.from_user.id) not in ADMIN_IDS:
        return
    await message.answer(logic.get_status())

@dp.message_handler(commands=['enable'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    if str(message.from_user.id) not in ADMIN_IDS:
        return
    logic.set_victim(True)
    await message.answer('ok')

@dp.message_handler(commands=['disable'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    if str(message.from_user.id) not in ADMIN_IDS:
        return
    logic.set_victim(False)
    await message.answer('ok')


@dp.message_handler(commands=['clear'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    if str(message.from_user.id) not in ADMIN_IDS:
        return
    await score.clear_data()
    await message.answer('ok')


@dp.message_handler(commands=['get_results'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    if str(message.from_user.id) not in ADMIN_IDS:
        return
    text = await score.get_level_results()
    await message.answer(text)

