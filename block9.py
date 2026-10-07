#zadaniya s 41 po 45
#41
text="hello"
print(f"lenth:{len(text)}")
#42
count_a=text.count('a')
print(f"kol-vo bukv 'a' v tekste: {count_a}")
#43
reversed_text=text[::-1]
print(f"{reversed_text}")
#44
text = input("Введите строку: ").lower().replace(" ", "")
if text == text[::-1]:
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")
#45
text = input("Введите строку: ").lower()
vowels = "аеёиоуыэюя"
count = sum(1 for char in text if char in vowels)
print(f"Количество гласных: {count}")
