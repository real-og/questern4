from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import texts


def generate_locations_kb(team_number, completed_tasks):
    team_number = str(team_number)
    if team_number == '1':
        places_order = [1, 2, 3, 4, 5, 6, 7]
    elif team_number == '2':
        places_order = [2, 3, 4, 5, 6, 7, 1]
    elif team_number == '3':
        places_order = [3, 4, 5, 6, 7, 1, 2]
    elif team_number == '4':
        places_order = [4, 5, 6, 7, 1, 2, 3]
    elif team_number == '5':
        places_order = [5, 6, 7, 1, 2, 3, 4]
    elif team_number == '6':
        places_order = [6, 7, 1, 2, 3, 4, 5]
    elif team_number == '7':
        places_order = [7, 1, 2, 3, 4, 5, 6]
    elif team_number == '8':
        places_order = [1, 2, 3, 4, 5, 6, 7]
    elif team_number == '9':
        places_order = [2, 3, 4, 5, 6, 7, 1]
    places_names = [texts.places_btns[index - 1] for index in places_order]
    kb = InlineKeyboardMarkup(row_width=1)
    for place_name in places_names:
        btn_text = place_name
        if place_name in completed_tasks:
            btn_text += '✔️'
        kb.add(InlineKeyboardButton(text=btn_text, callback_data=place_name))
    return kb
        

begin_quest_kb = ReplyKeyboardMarkup([[texts.begin_quest_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

yes_no_kb = ReplyKeyboardMarkup([[texts.yes_btn, texts.no_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

finish_task_kb = ReplyKeyboardMarkup([[texts.finish_task_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)


helmet_kb = ReplyKeyboardMarkup([[texts.give_helmet_btn, texts.take_helmet_btn]],
                                 resize_keyboard=True,
                                  one_time_keyboard=True)


task_completed_kb = ReplyKeyboardMarkup([[texts.task_completed_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)



