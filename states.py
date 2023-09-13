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
    task_2_1 = State()
    task_2_2 = State()
    task_2_3 = State()
    task_2_answering = State()
    task_2_finished = State()
    task_3_1 = State()
    task_3_2 = State()
    task_3_3 = State()
    task_3_answering = State()
    task_3_finished = State()
