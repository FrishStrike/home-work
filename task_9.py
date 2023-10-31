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
for i in range(1, num+1):
    print(i)
# второе решение со списком
list_num = [i for i in range(1, num+1)]
print(list_num)
# 3
print("Третье задание")
n = int(input("Введите число: "))
for i in range(1, n+1):
    if n % i == 0:
        print(i)
# второе решение со списком
lst_num = [i for i in range(1, n+1) if n % i == 0]
print(lst_num)