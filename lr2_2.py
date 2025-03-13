import matplotlib.pyplot as plt
import string 

def Num_of_vowels(text):
    vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ"
    vowels_count = {}
    for v in vowels:
        vowels_count[v] = 0

    for char in text:
        if char in vowels_count:
            vowels_count[char] += 1

    items = vowels_count.items()
    filter_dict = {}
    for k, v in items:
        if v > 0:
            filter_dict[k] = v
    return filter_dict

file_path = 'lr2/text.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

text = text.translate(str.maketrans("", "", string.punctuation))

vowels_num = Num_of_vowels(text)

plt.bar(vowels_num.keys(), vowels_num.values())
plt.title("Частота появи голосних")
plt.ylabel("Кількість появи")
plt.xlabel("Голосні")
plt.savefig("lr2/Гістограма")
plt.show()