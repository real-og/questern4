from aiogram.dispatcher.filters.state import StatesGroup, State


class State(StatesGroup):
    entering_name = State()
    confirmation_name = State()
    menu = State()
    start_confirmation = State()
    task_1 = State()
    task_1_exit = State()
    task_2 = State()
    task_2_exit = State()
    task_3_to_start = State()
    helmet_decision = State()
    task_4_inprogress = State()
    task_4_points = State()
    task_5 = State()
    task_5_exit = State()
    task_6_inprogress = State()
    task_6_keyword_entering = State()
    task_7_inprogress = State()
    task_7_points = State()
    finished = State()
