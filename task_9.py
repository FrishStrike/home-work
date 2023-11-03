# 1
print("Первое задание")
num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))
mul = num_1*num_2
def nok(num_1, num_2):
    if num_1 == 0 or num_2 == 0:
        return mul / (num_1+num_2)
    if num_1 > num_2:
        num_1 %= num_2
        return nok(num_1, num_2)
    else:
        num_2 %= num_1
        return nok(num_1, num_2)
print(nok(num_1, num_2))
# 2
print("Второе задание")
num = int(input("Введите число: "))
lst_simple = []
for i in range(1, num+1):
    res = True
    if i != 1:
        for k in range(2, i):
            if i % k == 0:
                res = False
    if res:
        print(i)
        lst_simple.append(i)
print(lst_simple)
# 3
print("Третье задание")
n = int(input("Введите число: "))
for i in range(1, n+1):
    if n % i == 0:
        print(i)
# второе решение со списком
lst_num = [i for i in range(1, n+1) if n % i == 0]
print(lst_num)