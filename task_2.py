# 1
print("Первое задание")
number = int(input("Введите число: "))
if number % 2 == 0:
    print("Данное число четное")
else:
    print("Данное число не является четным")
# 2
print("Второе задание")
num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
if num_1 > num_2:
    print(num_1)
elif num_1 < num_2:
    print(num_2)
else:
    print(num_1, num_2)
# 3
print("Третье задание")
x = int(input("Введите первое число: ")) # Буквы на доске
y = int(input("Введите второе число: ")) # Цифры на доске
if x % 2 == 0 and y % 2 != 0:
    print("YES")
else:
    print("NO")