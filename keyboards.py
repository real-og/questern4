from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import texts


begin_quest_kb = ReplyKeyboardMarkup([[texts.begin_quest_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

yes_no_kb = ReplyKeyboardMarkup([[texts.yes_btn, texts.no_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

victim_chosen_kb = ReplyKeyboardMarkup([[texts.victim_chosen_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

answer_or_hint_kb = ReplyKeyboardMarkup([[texts.answer_btn, texts.hint_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

answer_or_more_hint_kb = ReplyKeyboardMarkup([[texts.answer_btn, texts.more_hint_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

answer_or_more_hint2_kb = ReplyKeyboardMarkup([[texts.answer_btn, texts.more_hint2_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

get_hint_kb = ReplyKeyboardMarkup([[texts.hint_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

continue_kb = ReplyKeyboardMarkup([[texts.continue_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

photoes_uploaded_kb = ReplyKeyboardMarkup([[texts.uploaded_btn]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)


