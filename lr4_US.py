import json
import matplotlib.pyplot as plt

with open('lr2/json/currentUSrepresentatives.json', 'r') as file:
    data = json.load(file)

representatives = data["objects"]

parties = [item["party"] for item in representatives]

party_amount = {}
for party in parties:
    if party not in party_amount:
        party_amount[party] = 1
    else:
        party_amount[party] += 1


plt.bar(party_amount.keys(), party_amount.values(), color=["blue", "red"])
plt.xlabel("Партії")
plt.ylabel("Кількість представників")
plt.title("Розподіл представників США за партіями")

plt.show()

