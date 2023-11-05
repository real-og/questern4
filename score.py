import redis.asyncio as redis
import json

redis_client = redis.StrictRedis(host='localhost', port=6379, db=5)

async def clear_data():
    await redis_client.delete('teams')
    await redis_client.delete('level1')
    await redis_client.delete('level2')
    await redis_client.delete('level3')
    await redis_client.delete('level4')
    await redis_client.delete('level5')
    await redis_client.delete('level6')
    await redis_client.delete('level7')


async def add_team(id, name):
    team = {'id': id, 'name': name}
    await redis_client.rpush('teams', json.dumps(team))


async def get_teams():
    result = await redis_client.lrange('teams', 0, -1)
    return result

async def get_level_result(level):
    result = await redis_client.lrange(f'level{level}', 0, -1)
    return result

async def complete_level(id, level):
    key = f'level{level}'
    await redis_client.rpush(key, id)


async def get_level_results():
    text = "Команды и количество очков\n\n"

    teams = await get_teams()
    teams_dict = dict()
    for team in teams:
        teams_dict[f"b'{str(json.loads(team).get('id'))}'"] = json.loads(team).get('name')

    result = dict()

    for i in range(1, 8):
        level_result = await get_level_result(i)
        for place, id in enumerate(level_result):
            result[id] = result.get(id, 0) + place + 1

    sorted_result = dict(sorted(result.items(), key=lambda item: item[1]))

    final_place = 0
    for id in sorted_result:
        final_place += 1
        if teams_dict.get(str(id)) is None:
            text += f"{final_place}) {id} - {sorted_result.get(id)}\n"
        else:
            text += f"{final_place}) {teams_dict.get(str(id))} - {sorted_result.get(id)}\n"

    return text

        





    

   




