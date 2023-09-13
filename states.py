from aiogram.dispatcher.filters.state import StatesGroup, State


class State(StatesGroup):
    entering_name = State()
    confirmation_name = State()
    start_confirmation = State()
    task_1_1 = State()
    task_1_2 = State()
    task_1_3 = State()
    task_1_answering = State()
    task_1_finished = State()
