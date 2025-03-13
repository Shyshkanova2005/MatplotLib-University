import json
import matplotlib.pyplot as plt

with open('lr2/json/pokedex.json', 'r') as file:
    data = json.load(file)

type_amount = {}

for pokemon in data["pokemon"]:
    for pokemon_type in pokemon["type"]:
        if pokemon_type not in type_amount:
            type_amount[pokemon_type] = 0
        type_amount[pokemon_type] += 1


labels = list(type_amount.keys())
values = list(type_amount.values())

plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title('Розподіл покемонів за типами')
plt.show()



