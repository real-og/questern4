import logic
import random

def generate_confirmation_msg(name):
    return f"{name} - так будет называться Ваша команда. Уверены?"

def generate_confirmation_victim_msg(name):
    return f"{name} хочет принести себя в жертву? Вы уверены?"

def wrong_number(input):
    return f"Вы ошиблись на {logic.count_non_matching_digits(input, task1_3_ans)} цифру(ы)"

def write_random_joke_3():
    return random.choice(task3_jokes)


welcome = """🔥 ИГРА НА ВЫЖИВАНИЕ🔥

❗️Я буду испытывать вас, а вы должны играть по моим правилам.

❗️Вам нужно разгадать загадки и прислать мне ответы на загадки.

❗️ Если вы справитесь, то получите противоядие и останетесь живы. 

Чтобы вступить в игру, напишите название своей команды."""

enter_another_name = "Хорошо, введите другое имя для вашей команды."

succes_registrated = """Чтобы получить первую загадку, нажмите на кнопку «Начать игру». Она находится внизу экрана ⤵️"""

use_kb = 'Используйте кнопки.'

use_a_button = 'Нажмите на кнопку «НАПИСАТЬ ОТВЕТ» ⤵️'

wrong_answer = 'Неверно!'


yes_btn = 'Да'
no_btn = 'Нет'
begin_quest_btn = "Начать игру"
victim_chosen_btn = "Жертва выбрана"
answer_btn = "Написать ответ"
hint_btn = "Получить подсказку"
more_hint_btn = "Получить ещё подсказку"
more_hint2_btn = "Получить подсказку снова"
continue_btn = 'Продолжить игру'
uploaded_btn = 'ФОТОГРАФИИ ГОТОВЫ'
done_btn = 'Испытание пройдено'
ready_btn = 'Мы готовы'
no_sound_btn = 'Ничего не слышно'

yes_btn = 'Да'.upper()
no_btn = 'Нет'.upper()
begin_quest_btn = "Начать игру".upper()
victim_chosen_btn = "Жертва выбрана".upper()
answer_btn = "Написать ответ".upper()
hint_btn = "Получить подсказку".upper()
more_hint_btn = "Получить ещё подсказку".upper()
more_hint2_btn = "Получить подсказку снова".upper()
continue_btn = 'Продолжить игру'.upper()
uploaded_btn = 'ФОТОГРАФИИ ГОТОВЫ'.upper()
done_btn = 'Испытание пройдено'.upper()
ready_btn = 'Мы готовы'.upper()
no_sound_btn = 'Ничего не слышно'.upper()


help_message = """От меня помощи не будет.  Обращайтесь к моему помощнику."""


ask_photo_victim = "Пришлите фото жертвы. Хочу посмотреть на этого альтруиста"

enter_another_victim = "Давайте другого"


ask_for_victim = """❗️Чтобы получить загадку, нужно принести в жертву игроков вашей команды. 

❗️ Количество жертв сообщит мой помощник. 

❗️ Выберите жертву и передайте моему помощнику.
"""


send_photo = 'Отправляйте фото'

victim_received = "❗️❗️Посмотрите видео и напишите кодовое слово."

photo_received = """Я принимаю вашу жертву. 
Введите кодовое слово, которое вам сообщит мой помощник"""

enter_code_w = '❗️Напишите кодовое слово, которое вам сообщит мой помощник.'

ask_for_codeword = """Введите кодовое слово, которое сообщит мой помощник."""

task1_3 = """🔥🔥 <b>ТЕЛЕФОН</b> 🔥🔥

Расшифруйте вопросы. Ответ на вопрос – это цифра номера телефона. \
Напишите номер телефона в формате 89…"""
task1_hint_1 = "Переставьте буквы местами, и каждое слово обретёт свой истинный смысл."
task1_hint_2 = "Гуглить разрешается."
task1_3_1 = """🔥🔥 <b>ТЕЛЕФОН</b> 🔥🔥

Помощник даст вам загадку.
❗️Расшифруйте вопросы. 
❗️Ответ на вопрос - это цифра номера телефона.
"""
task1_3_2="""☎️ Напишите номер телефона в формате 89…"""
enter_number = "☎️ Напишите номер телефона в формате 89…"
ask_for_whole_number = "В номере телефона 11 цифр, мне нужен именно он."
no_need_question = 'Вы правильно расшифровали этот вопрос. Но мне нужен номер телефона.'
task_1_finish = "<b>В настоящее время абонент недоступен. Но испытание считается пройдённым. Поздравляю!</b> 🎉"


task2_3 = """🔥🔥 <b>УЛЬТРАФИОЛЕТ</b> 🔥🔥

❗️Вам потребуется особый свет, чтобы разгадать эту загадку. Ответ на загадку - это одно слово."""
task2_hint_1 = "Загадка <tg-spoiler>невидима</tg-spoiler> и спрятана в чёрной ткани"
enter_answer = "Напишите ответ на загадку."
no_need_question_2 = """Вы правильно расшифровали мою загадку. Теперь напишите ответ. 

❗️Ответ – это всегда 1 слово."""
task_2_finish = "<tg-spoiler>Вы гении!</tg-spoiler>\n 🔥Испытание пройдено🔥"

task3_3 = """🔥🔥 <b>БЕЗМОЛВИЕ</b> 🔥🔥

Сейчас перед вами появится безмолвный человек.
❗️Внимательно следите за его жестами. 
❗️Записывайте на листе бумаги всё, что он покажет."""
task3_jokes = [
    'Я не бумага. Пишите свои числа на бумаге.',
    'Это ваш семейный бюджет?',
    'Я бот, а не калькулятор. ',
    'Вы ошиблись приложением. Учёт финансов здесь не ведётся.',
    'Зачем мне эта информация?',
    'Вы готовитесь к ЕГЭ по математике?'
]
task3_hint_1 = """Расшифруйте загадку и напишите ответ.
❗️ Ответ на загадку - это одно слово."""
task3_hint_2 = "А что, если числа – это буквы?"
task_3_finish = '🔥Испытание пройдено🔥\n <tg-spoiler>Я под впечатлением от вашей игры</tg-spoiler>'

task4_3 = """🔥🔥 <b>ПОДАРКИ</b> 🔥🔥

Я приготовил для вас подарки. 🎁 

♦️В коробке спрятана загадка из 6 слов. 
♦️ Все слова зашифрованы. 
♦️ Расшифруйте каждое слово, отгадайте загадку и напишите ответ. Ответ на загадку - это одно слово."""

task4_hint_1 = "Здесь всё элементарно сложно."
task4_hint_2 = "Расшифруйте каждое слово, чтобы получить загадку из 6 слов."
task4_hint_3 = "Отгадайте загадку и напишите мне ответ. Ответ – это всегда 1 слово."
task_4_finish = '🔥Испытание пройдено🔥\n <tg-spoiler>Аплодирую вам!</tg-spoiler>'

task5_3_1 = """🔥🔥 ФОТОГРАФИИ 🔥🔥

Я хочу, чтобы вы запомнили эту игру. Следуйте правилам:

1️⃣ Сделайте фотографии по инструкции, которую вы получите. 

2️⃣ Загрузите фотографии в специальное бот-хранилище: @SawPhotoBot
"""
task5_3_2 = 'Нажмите 👉 @SawPhotoBot'

ask_for_btn_photoes = '<i>Когда закончите, нажмите на кнопку ⤵️</i>'

task5_3_3 = """Вы можете делать снимки на телефон любого игрока. \
Отсканируйте, чтобы загрузить их в Облако:"""

task_5_finish = 'Благодарю вас.\nЯ буду пересматривать ваши шедевры долгими зимними вечерами.'

task6_3_1 = """❗️Следующая загадка находится в отдельном помещении. 
‼️ В нём действуют особые правила:"""
task6_3_2 = """1️⃣ В помещении может находиться только 1 игрок от каждой команды и только 1 минуту. У игрока должен быть мобильный телефон. 
2️⃣ Игроки должны заходить в помещение по команде помощника. 
3️⃣ Запрещается выносить что-либо из помещения. 
4️⃣ Запрещается фотографировать то, что находится в помещении.

‼️ Вы принимаете эти правила?"""
task6_3_3 = """❗️Ваша задача - найти загадку. 

❗️Выберите, кто пойдет первым, кто вторым и т.д. 

Когда будете готовы, нажмите на кнопку ⤵️"""
task6_hint_1 = 'Эта загадка состоит из 12 фрагментов.'
task_6_finish = '🔥Испытание пройдено🔥\n <tg-spoiler>Горжусь вами!</tg-spoiler>'

task7_3 = """🔥🔥 <b>КАМЕРА</b> 🔥🔥

❗️Это испытание для самого главного человека среди вас. Вы знаете, кто это? 
❗️ Ему (ей) понадобится проводник. 
❗️ Помощник объяснит суть испытания. 

Когда справитесь с испытанием, нажмите на кнопку ⤵️"""
task_7_finish = 'Хорошо.'


task1_2_ans = 'ТЕЛЕФОН'
task1_3_ans = '89629435619'
task1_wrong_ans = [
    'СКОЛЬКО ГРАНЕЙ У КУБА',
    'КАКОЙ АТОМНЫЙ НОМЕР ГЕЛИЯ',
    'СКОЛЬКО НУЛЕЙ У МИЛЛИАРДА',
    'КАКОЙ ПОРЯДКОВЫЙ НОМЕР ИВАНА ГРОЗНОГО',
    'СКОЛЬКО ЛЮДЕЙ В ЛОДКЕ НЕ СЧИТАЯ СОБАКИ',
    'СКОЛЬКО МУЗЫКАНТОВ В КВИНТЕТЕ',
    'КАКОЙ НОМЕР ПОМЕЩЕНИЯ У ЧЕХОВА',
    'СКОЛЬКО ГЛАЗ У ЦИКЛОПА',
    'КАКОЙ ПОРЯДКОВЫЙ НОМЕР БУКВЫ I В АНГЛИЙСКОМ АЛФАВИТЕ',
]

task2_2_ans = 'УЛЬТРАФИОЛЕТ'
task2_3_ans = 'НАДЕЖДА'
task2_wrong_ans = {
    'КАКАЯ ДЕВУШКА УМИРАЕТ В ПОСЛЕДНЮЮ ОЧЕРЕДЬ': no_need_question_2,
    'КАКАЯ': 'Кто какая?',
    'ДЕВУШКА': 'Кто же еще',
    'УМИРАЕТ': 'О, нет!',
    'В ПОСЛЕДНЮЮ': 'Обидно..',
    'ОЧЕРЕДЬ': 'За чем очередь?',
}

task3_2_ans = 'БЕЗМОЛВИЕ'
task3_3_ans = 'ПУЛЯ'
task3_wrong_ans = {
    'ЛЕТИТ ВОРОН В ОКОВАХ КОГО КЛЮНЕТ ТОМУ СМЕРТЬ': no_need_question_2,
    'ЛЕТИТ': 'Кто летит?',
    'ВОРОН': 'Допустим. И что?',
    'ЛЕТИТ ВОРОН': 'Допустим. И что?',
    'В ОКОВАХ': 'Ок, я это запомню.',
    'ЛЕТИТ ВОРОН В ОКОВАХ': 'Ок, я это запомню.',
    'КОГО': 'Чего?',
    'КОГО КЛЮНЕТ': 'Чего?',
    'КЛЮНЕТ': 'Чего?',
    'ТОМУ': 'Какому еще Тому?',
    'ТОМУ СМЕРТЬ': 'Ужас какой💀',
    'СМЕРТЬ': 'Ужас какой💀',
}

task4_2_ans = 'ПОДАРКИ'
task4_3_ans = 'КОМАР'
task4_wrong_ans = {
    'ЕСЛИ ЕГО УБЬЁШЬ СВОЮ КРОВЬ ПРОЛЬЁШЬ' : no_need_question_2,
    'ЕСЛИ ЕГО УБЬЕШЬ СВОЮ КРОВЬ ПРОЛЬЕШЬ' : no_need_question_2,
    'ЕСЛИ ЕГО УБЬЁШЬ СВОЮ КРОВЬ ПРОЛЬЕШЬ' : no_need_question_2,
    'ЕСЛИ ЕГО УБЬЕШЬ СВОЮ КРОВЬ ПРОЛЬЁШЬ' : no_need_question_2,
    'ЕСЛИ ЕГО УБЬЕШЬ КРОВЬ СВОЮ ПРОЛЬЕШЬ': no_need_question_2,
    'КРОВЬ СВОЮ ПРОЛЬЕШЬ ЕСЛИ ЕГО УБЬЕШЬ': no_need_question_2,
    'СВОЮ КРОВЬ ПРОЛЬЕШЬ ЕСЛИ ЕГО УБЬЕШЬ': no_need_question_2,
    # '': no_need_question_2,
    'ЕСЛИ': 'Верно👍',
    'ЕГО': 'Верно👍',
    'УБЬЁШЬ': 'Верно👍',
    'УБЬЕШЬ': 'Верно👍',
    'СВОЮ': 'Верно👍',
    'КРОВЬ': 'Верно👍',
    'ПРОЛЬЁШЬ': 'Верно👍',
    'ПРОЛЬЕШЬ': 'Верно👍',
}

task5_2_ans = 'ФОТОГРАФИИ'

task6_2_ans = 'КОДЫ'
task6_3_ans = 'РЫБА'
task6_wrong_ans = [
    'НЕ ДЫШИТ',
    'НО ЖИВЕТ',
    'КАК СМЕРТЬ',
    'НЕМА',
    'НЕ ПЬЕТ',
    'ХОТЯ',
    'В ВОДЕ',
    'СИДИТ',
    'В КОЛЬЧУГЕ',
    'ХОТЬ И',
    'НЕ ЗВЕНИТ',
    'И ХОЛОДНА',
]
no_need_question_6 = "Вы правильно расшифровали этот фрагмент. \
Но мне нужен ответ на загадку. Ответ – это всегда 1 слово."

task7_2_ans = 'КАМЕРА'

exit_word = 'ВЫЖИВАНИЕ'

ending = 'Пила покинул чат.'
ending_video = '*video'

rigth = 'Верно 👍'
no_part = 'Такого в моей загадке нет'

wrong_code_word = """Неверно! ⛔️
Узнайте кодовое слово у моего помощника."""

game_ended = """‼️‼️ Ваша игра окончена ‼️‼️"""

task6_new1 = """🔥🔥 <b>КОДЫ</b> 🔥🔥

❗️Эта загадка разбита на части и закодирована. 
❗️ Чтобы раскодировать загадку, вам потребуется мобильный телефон.
❗️Помощник сообщит вам детали. """
task6_new2 = """Разгадайте загадку и напишите ответ.
❗️Ответ на загадку - это одно слово."""
task6_new3 = """Вы нашли 1 фрагмент большой загадки 🧩
❗️Найдите все фрагменты и напишите ответ на загадку. 
❗️Ответ - это всегда одно слово."""

help_admin = """Команды

/status - включена ли жертва
/enable - включить жертву
/disable - выключить жертву
/results - посмотреть результаты
/clear - очистить результаты"""

no_sound_description = "Если ничего не слышно, нажмите на кнопку ⤵️"

right_number = """Правильно 👍 
Чтобы позвонить на этот номер, нужен ваш телефон.
Нажмите на кнопку внизу ⤵️"""

phone_btn = "Поделиться телефоном"

voice_received = """Получено аудиосообщение. Нажмите, чтобы прослушать ⤵️"""





