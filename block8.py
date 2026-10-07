#zadaniya s 36 po 40
#36
n = int(input("Введите число: "))
digit_sum = 0
temp = abs(n)
while temp > 0:
    digit_sum += temp % 10
    temp //= 10
print(f"Сумма цифр: {digit_sum}")
#37
n = int(input("Введите число: "))
reversed_num = 0
temp = n
while temp > 0:
    reversed_num = reversed_num * 10 + temp % 10
    temp //= 10
print(f"Перевернутое число: {reversed_num}")
#38
original = int(input("Введите число: "))
n = original
reversed_num = 0
while n > 0:
    reversed_num = reversed_num * 10 + n % 10
    n //= 10
if original == reversed_num:
    print("Число является палиндромом")
else:
    print("Число не является палиндромом")
#39
import random
secret = random.randint(1, 10)
guess = int(input("Угадайте число от 1 до 10: "))
while guess != secret:
    guess = int(input("Неверно, попробуйте еще раз: "))
print("Поздравляем, вы угадали!")
#40
num = int(input("Введите положительное число: "))
while num <= 0:
    num = int(input("Ошибка. Введите положительное число: "))
print(f"Спасибо, вы ввели: {num}")