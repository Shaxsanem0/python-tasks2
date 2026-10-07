#zadaniya s 26 po 30
# 26
num = 5
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")

# 27
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")

# 28
count = 0
for i in range(1, 1001):
    if i % 3 == 0:
        count += 1
print(count)

# 29
n = int(input())
total_sum = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        total_sum += i
print(total_sum)

# 30
for i in range(1, 21):
    print(i ** 2)