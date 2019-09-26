from bs4 import BeautifulSoup
import requests
import json

req = requests.get('http://digidb.io/digimon-list/')
soup = BeautifulSoup(req.content, 'html.parser')

data = soup.find('tbody')
data = data.find_all('tr')

x = []

for i in data:
    no = i.find('td', width='5%').b.text.replace(u'\xa0', '')
    digimon = i.a.text
    img = i.img['src']
    stage = i.center.text
    type_ = i.find('td', width='7%').text
    attribute = i.find('td', width='7%').find_next_sibling().text
    memory = i.find('td', width='7%').find_next_sibling().find_next_sibling().text
    equip_slots = i.find('td', width='8%').text
    power = i.find_all('td', width=False)

    stats = []
    for item in power:
        stats.append(item.text)
    
    y = {
        'no': int(no),
        'digimon': digimon,
        'image': img,
        "stage": stage,
        'type': type_,
        'attribute': attribute,
        'memory': int(memory),
        'equip slots': int(equip_slots),
        "hp": int(stats[0]),
        "sp": int(stats[1]),
        "atk":int(stats[2]),
        "def":int(stats[3]),
        "int":int(stats[4]),
        "spd":int(stats[5])
        }
    x.append(y)

with open('digimon.json', 'w') as hello:
    json.dump(x, hello)