import unicodedata
import re
from loader import bot, ADMIN_IDS

def remove_punctuation(s):
    no_punctuation = ''.join([char for char in s if not unicodedata.category(char).startswith('P')])
    no_double_spaces = re.sub(r'\s+', ' ', no_punctuation)
    return no_double_spaces.strip()  


def count_non_matching_digits(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i] and str1[i].isdigit() and str2[i].isdigit():
            count += 1
    return count

async def notify_admins(level, state):
    data = await state.get_data()
    team_name = data.get('team_name')
    for id in ADMIN_IDS:
        try:
            await bot.send_message(id, f"{team_name} закончил уровень {level}")
        except Exception as e:
            print(f'Не отправилось для {id}')






