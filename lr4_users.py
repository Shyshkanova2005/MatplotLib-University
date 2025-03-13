import json
import matplotlib.pyplot as plt

with open('lr2/json/users_100.json', 'r') as file:
    data = json.load(file)

users = data

all_hobbies = []
for person in users:
    for friend in person["friends"]:
        all_hobbies.extend(friend["hobbies"])


hobbies_amount = {}
for hobby in all_hobbies:
    if hobby in hobbies_amount:
        hobbies_amount[hobby] += 1
    else:
        hobbies_amount[hobby] = 1

sorted_hobbies = sorted(hobbies_amount.items(), key=lambda x: x[1], reverse=True)
sorted_hobbies_names = [hobby[0] for hobby in sorted_hobbies]
sorted_hobbies_counts = [hobby[1] for hobby in sorted_hobbies]

plt.bar(sorted_hobbies_names, sorted_hobbies_counts, color=["orange"])
plt.ylabel("Розподіл найпоширеніших хобі серед усіх людей")
plt.xlabel("Хобі")
plt.title("Кількість людей")
plt.xticks(rotation=90, fontsize=7)
plt.tight_layout()
plt.show()