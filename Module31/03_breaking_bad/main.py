import requests
import json

s = requests.get('https://www.breakingbadapi.com/api/deaths')
data = json.loads(s.text)

info = dict()
for i in data:
    if (i['season'], i['episode']) in info:
        info[(i['season'], i['episode'])] += 1
    else:
        info[(i['season'], i['episode'])] = 1
season, episode = max(info)

s = requests.get(f'https://www.breakingbadapi.com/api/episodes')
d = json.loads(s.text)

for i in d:
    if i['season'] == str(season) and i['episode'] == str(episode) and i['series'] == 'Breaking Bad':
        id = i['episode_id']

with open('death.json', 'w') as file:
    json.dump(d, file, indent=4)

epis = dict()
epis[1] = id
epis[2] = season
epis[3] = episode
epis[4] = 0
epis[5] = list()
for i in data:
    if season == i['season'] and episode == i['episode']:
        epis[4] += 1
        epis[5].append(i['death'])
print(epis)
with open('death.json', 'w') as file:
    json.dump(epis, file, indent=4)
