#zadaniya s 46 po 50

# 46
text = input("Введите строку: ").lower()
consonants = "бвгджзклмнпрстфхцчшщ"
count = sum(1 for char in text if char in consonants)
print(f"Количество согласных: {count}")


# 47
text = input("Введите предложение: ")
words = text.split()
print(f"Количество слов: {len(words)}")

#48
text = input("Введите предложение: ")
words = text.split()
if words:
    longest_word = max(words, key=len)
    print(f"Самое длинное слово: {longest_word}")
else:
    print("Вы ничего не ввели.")


# 49
text = input("Введите строку с пробелами: ")
new_text = text.replace(" ", "-")
print(f"Результат: {new_text}")

# 50
text = input("Введите строку: ")
word = input("Введите слово для проверки: ")
if text.startswith(word):
    print(f"Да, строка начинается со слова '{word}'")
else:
    print(f"Нет, строка начинается не со слова '{word}'")