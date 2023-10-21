# 1
print("Первая задача")
city_count = int(input("Введите количество городов: "))
towns = [input() for i in range(city_count)]
result = 0
for i in range(len(towns)):
    for k in range(len(towns)):
        if towns[i] == towns[k] and i != k:
            result += 1
print(result)
# 2
print("Вторая задача")
text = input("Введите текст: ")
first_letter = 0
final_list = []
skip = 0
while text[first_letter] == " ":
    final_list.append(text[first_letter])
    first_letter += 1  
final_list.append(text[first_letter].upper())
for i in range(first_letter+1, len(text)):
    if skip:
        skip -= 1
        continue
    if text[i-1] != "." and text[i-1] != "!" and text[i-1] != "?":
        final_list.append(text[i])
        continue
    while text[i] == " ":
        final_list.append(text[i])
        skip += 1
        i += 1
    final_list.append(text[i].upper())
print("".join(final_list))
# 3
print("Третье задание")
str_1 = input("Введите первую строку: ")
str_2 = input("Введите вторую строку: ")
set_1 = {i for i in str_1 if i != " "}
set_2 = {i for i in str_2 if i != " "}
first_len = len(set_1)
set_1.update(set_2)
second_len = len(set_1)
if first_len == second_len and len(str_1) == len(str_2):
    print("Строки являются аннограмами")
else:
    print("Строки не являются аннограмами")
# 4
print("Четвертое задание")
math_1 = set(input("Введите фамилии победителей олимпиады по алгебре: ").split(" "))
math_2 = set(input("Введите фамилии победителей олимпиады по геометрии: ").split(" "))
math_3 = set(input("Введите фамилии победителей олимпиады по тригонометрии: ").split(" "))
lose_1 = math_1.difference(math_2)
lose_2 = math_1.difference(math_3)
lose_1.update(lose_2)
win = math_1.difference(lose_1)
if len(win) == 0:
    print("Все три задачи никто не решил")
else:
    print(win)
