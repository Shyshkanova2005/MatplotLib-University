import json
import matplotlib.pyplot as plt
from datetime import datetime

with open('lr2/json/eventsScottishParliament.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

dates = [datetime.strptime(event['Date'], '%Y-%m-%dT%H:%M:%S') for event in data]


sponsor_amount = {}
for event in data:
    sponsor = event["Sponsor"]
    if sponsor in sponsor_amount:
        sponsor_amount[sponsor] += 1
    else:
        sponsor_amount[sponsor] = 1

sorted_sponsors = sorted(sponsor_amount.items(), key=lambda x: x[1], reverse=True)[:10]

sponsor_name = [item[0] for item in sorted_sponsors]
event_amounts = [item[1] for item in sorted_sponsors]

plt.figure(figsize=(10, 6))
plt.bar(sponsor_name, event_amounts, color='b')
plt.xlabel('Спонсор')
plt.ylabel('Кількість подій')
plt.title('Кількість подій для 10 найбільш активних спонсорів')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

