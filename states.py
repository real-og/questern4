from aiogram.dispatcher.filters.state import StatesGroup, State


class State(StatesGroup):
    entering_name = State()
    confirmation_name = State()
    start_confirmation = State()

    entering_code_name = State()
    choosing_a_victim = State()
    asking_for_continue = State()

    ended = State()

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

    task_4_1 = State()
    task_4_2 = State()
    task_4_3 = State()
    task_4_answering = State()
    task_4_finished = State()

    task_5_1 = State()
    task_5_2 = State()
    task_5_3 = State()
    task_5_answering = State()
    task_5_finished = State()

    task_6_1 = State()
    task_6_2 = State()
    task_6_3 = State()
    task_6_answering = State()
    task_6_finished = State()

    task_7_1 = State()
    task_7_2 = State()
    task_7_3 = State()
    task_7_answering = State()
    task_7_finished = State()

