#zadaniya s 31 po 35
#31
n=1
while n<=100:
    print(n)
    n+=1
    #32
correct_password = "123"
while input("Введите пароль: ") != correct_password:
    print("Неверный пароль, попробуйте снова.")
print("Доступ разрешен!")
#33
num = int(input("Введите число 0: "))
while num != 0:
    print(f"вы ввели число: {num}")
    num = int(input("Введите число 0: "))
    print("вы ввели число 0 рограммма завершена")
    #34
    total_sum = 0
num = int(input("Введите число : "))
while num != 0:
    total_sum += num
    num = int(input("Введите число : "))
print(f"Сумма введённых чисел: {total_sum}")
#35
n = int(input("Введите число: "))
count = 0
if n == 0:
    count = 1
else:
    temp = abs(n)
    while temp > 0:
        count += 1
        temp //= 10
print(f"Количество цифр: {count}")
