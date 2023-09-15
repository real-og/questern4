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


welcome = """Добро пожаловать в игру на выживание. \
Вам нужно разгадать загадки и написать мне ответы на загадки.
Сначала напишите название своей команды."""

enter_another_name = "Хорошо, введите другое имя для вашей команды."

succes_registrated = "Вы в игре! Чтобы получить первую загадку, нажмите на кнопку ⤵️"

use_kb = 'Используйте клавиатуру.'

use_a_button = 'Нажмите на кнопку «Написать ответ» ⤵️'

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
uploaded_btn = 'Фотографии загружены'
done_btn = 'Выполнено'


help_message = """По всем вопросам обращайтесь к координаторам в мастер-локации."""


ask_photo_victim = "Пришлите фото жертвы. Хочу посмотреть на этого альтруиста"

enter_another_victim = "Давайте другого"

ask_for_victim = "Чтобы получить загадку, выберите одного игрока из вашей команды. \
Кто готов принести себя в жертву в обмен на загадку? Напишите имя жертвы"

send_photo = 'Отправляйте фото'

photo_received = 'Я принимаю вашу жертву\nВведите кодовое слово'

ask_for_codeword = """Введите кодовое слово, которое сообщит мой помощник."""

task1_3 = """Расшифруйте вопросы. Ответ на вопрос – это цифра номера телефона. \
Напишите номер телефона в формате 89…"""
task1_hint_1 = "Переставьте буквы местами, и каждое слово обретёт свой истинный смысл."
task1_hint_2 = "Гуглить разрешается."
enter_number = "Напишите получившийся номер. Он состоит из одиннадцати цифр и начинается на 8."
ask_for_whole_number = "В номере телефона 11 цифр, мне нужен именно он."
no_need_question = 'Вы правильно расшифровали этот вопрос. Но мне нужен номер телефона.'
# task_1_finish = "В данный момент абонент недоступен. Но испытание пройдено. Поздравляю!"


task2_3 = "Используйте особый свет, чтобы увидеть загадку."
task2_hint_1 = "Загадка <tg-spoiler>невидима</tg-spoiler> и спрятана в чёрной ткани"
enter_answer = "Напишите ответ на задание."
no_need_question_2 = "Вы правильно расшифровали мою загадку. Теперь напишите ответ. Ответ – это всегда 1 слово."
task_2_finish = "<tg-spoiler>Вы гении!</tg-spoiler>\n 🔥Испытание пройдено🔥"

task3_3 = "Сейчас перед вами появится безмолвный человек. \
Внимательно следите за его жестами. Записывайте на листе бумаги всё, что он покажет."
task3_jokes = [
    'Я не бумага. Пишите свои числа на бумаге.',
    'Это ваш семейный бюджет?',
    'Я бот, а не калькулятор. ',
    'Вы ошиблись приложением. Учёт финансов здесь не ведётся.',
    'Зачем мне эта информация?',
    'Вы готовитесь к ЕГЭ по математике?'
]
task3_hint_1 = "Расшифруйте загадку и напишите ответ."
task3_hint_2 = "А что, если числа – это буквы?"
task_3_finish = '🔥Испытание пройдено🔥\n <tg-spoiler>Я под впечатлением от вашей игры</tg-spoiler>'

task4_3 = "Я приготовил для вас подарок. В коробке спрятана загадка из 6 слов. \
Все слова зашифрованы. Расшифруйте каждое слово и напишите ответ на загадку."
task4_hint_1 = "Здесь всё элементарно сложно."
task4_hint_2 = "Вы уверены, что сами не разберетесь?"
task4_hint_3 = "У меня нет для вас подсказки. Обратитесь к моему помощнику."
task_4_finish = '🔥Испытание пройдено🔥\n <tg-spoiler>Аплодирую вам!</tg-spoiler>'

task5_3_1 = "Я хочу, чтобы вы запомнили эту игру. Фотографии сохранят ваши воспоминания. \
Сделайте их по инструкции, покажите моему помощнику, а потом загрузите в Облако. Я должен их увидеть"
task5_3_2 = "Загрузите ваши фотографии по ссылке:\n\n \
<code>https://cloud.mail.ru/public/Jdq8/W3QzKVXEU</code>"
task5_3_3 = """Вы можете делать снимки на телефон любого игрока. \
Отсканируйте, чтобы загрузить их в Облако:"""

task_5_finish = 'Благодарю вас.\nЯ буду пересматривать ваши шедевры долгими зимними вечерами.'

task6_3 = """Следующая загадка находится в отдельном помещении. \
Туда может зайти 1 игрок на 1 минуту. После него может зайти следующий игрок на 1 минуту и т.д. \
Найдите загадку и напишите ответ.\n\n \
Выберите, кто пойдет первым.

Правила:
    1. Запрещается выносить что-либо из помещения
    2. Запрещается фотографировать то, что находится в помещении."""
task6_hint_1 = "Эта загадка состоит из 12 фрагментов."
task_6_finish = '🔥Испытание пройдено🔥\n <tg-spoiler>Горжусь вами!</tg-spoiler>'

task7_3 = "Это испытание для самого главного человека среди вас. \
Вы знаете, кто это. Ему понадобится проводник. Помощник объяснит суть испытания."
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
task2_wrong_ans = [
    'КАКАЯ ДЕВУШКА УМИРАЕТ В ПОСЛЕДНЮЮ ОЧЕРЕДЬ',
]

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
    'ЕСЛИ': 'Верно👍',
    'ЕГО': 'Верно👍',
    'УБЬЁШЬ': 'Верно👍',
    'СВОЮ': 'Верно👍',
    'КРОВЬ': 'Верно👍',
    'ПРОЛЬЁШЬ': 'Верно👍',
}

task5_2_ans = 'ФОТОГРАФИИ'

task6_2_ans = ['QR КОД', 'QRКОД', 'QR-КОД', 'КУАРКОД', 'КЬЮАРКОД']
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

ending = 'Бот покинул чат.'
ending_video = '*video'




