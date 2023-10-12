# 1
print("Первая задача")
number = input("Введите число: ")
res = 0
for i in range(len(number)):
    res += int(number[i])
print(res)
# 2
print("Вторая задача")
n = int(input("Введите число: "))
res = 1
for i in range(1, n+1):
    res *= i
print(res)
# 3
print("Третья задача")
n_2 = int(input("Введите число: "))
for i in range(1, n_2+1):
    if i % 7 == 0:
        print(i)