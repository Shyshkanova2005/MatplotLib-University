import json
import matplotlib.pyplot as plt

with open('lr2/json/dailyCOVID_US.json', 'r') as file:
    data = json.load(file)

covid = data["data"]  
latest_data = covid[0]

cases = latest_data["cases"]["total"]["value"]
tests = latest_data["testing"]["total"]["value"]
deaths = latest_data["outcomes"]["death"]["total"]["value"]


labels = ['Підтверджені випадки', 'Загальні тести', 'Смерті']
values = [cases, tests, deaths]
colors = ['red', 'orange', 'blue']

explode = (0.1, 0.1, 0.1)

fig, ax = plt.subplots()

ax.pie(values, labels=labels, colors=colors, autopct='%1.1f%%', explode=explode,  startangle=140)

ax.set_title("Розподіл статистики COVID-19")
plt.show()
