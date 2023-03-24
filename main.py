import requests

def get_heroes_powerstat(names, stat):
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    heroes_powerstat = {}
    for name in response.json():
        if name['name'] in names:
            heroes_powerstat[name['name']] = name['powerstats'][stat]
    return heroes_powerstat

def compare_heroes_powerstat(names, stat):
    heroes_powerstat = dict(sorted(get_heroes_powerstat(names, stat).items(), key=lambda item: item[1]))
    higher_hero_powerstat = list(heroes_powerstat.items())[-1][-1]
    result = []
    for hero, powerstat in heroes_powerstat.items():
        if powerstat == higher_hero_powerstat:
            result.append(hero)
    ru_powerstat = {"intelligence" : 'интеллект' , "strength" : 'сила', "speed" : 'скорость', "durability" : 'стойкость', "power" : 'сила', "combat" : 'бой'}
    return print(f'Герой с наибольшей характеристикой {ru_powerstat[stat]} {", ".join(map(str,result))}.')


if __name__ == '__main__':
    compare_heroes_powerstat(['Hulk', 'Captain America', 'Thanos'], 'intelligence')