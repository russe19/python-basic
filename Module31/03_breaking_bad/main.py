import requests
import json

s = requests.get('https://www.breakingbadapi.com/api/deaths')
data = json.loads(s.text)

info = dict()
for i in data:
    if (i['season'], i['episode']) in info:
        info[(i['season'], i['episode'])] += i['number_of_deaths']
    else:
        info[(i['season'], i['episode'])] = i['number_of_deaths']

season = 0
episode = 0
number_of_deaths = 0
print(info)
for i in info:
    if info[i] == max(info.values()):
        season, episode = i
        number_of_deaths = info[i]
print(season, episode)

s = requests.get(f'https://www.breakingbadapi.com/api/episodes')
d = json.loads(s.text)

for i in d:
    if i['season'] == str(season) and i['episode'] == str(episode) and i['series'] == 'Breaking Bad':
        id = i['episode_id']

with open('death.json', 'w') as file:
    json.dump(d, file, indent=4)

epis = dict()
epis['episode_id'] = id
epis['season'] = season
epis['episode'] = episode
epis['number_of_deaths'] = number_of_deaths
epis['deaths'] = ''
for i in data:
    if season == i['season'] and episode == i['episode']:
        if epis['deaths'] == '':
            epis['deaths'] = i['death']
        else:
            epis['deaths'] += ', ' + i['death']
print(epis)
with open('death.json', 'w') as file:
    json.dump(epis, file, indent=4)
