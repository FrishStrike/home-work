# 1
print("Первое задание")
str = input("Введите строку: ")
str_list = str.split(" ")
str_list.reverse()
print(str_list)
# 2
print("Второе задание")
string = input("Введите строку: ")
final_list = []
for i in range(len(string)):
    if i % 2 != 0:
        continue
    final_list.append(string[i])
print("".join(final_list))
# 3
print("Третье задание")
nums = input("Введите числа: ")
n = int(input("Введите степень: "))
res = [int(i)**n for i in nums.split(" ")]
print(res)
# 4
print("Четвертая задача")
text = input("Введите текст: ")
sym = input("Введите символ: ")
result = [k*2 if k == sym else k for k in text]
print("".join(result))
# 5
print("Пятая задача")
text_2 = input("Введите текст: ")
x_count = text_2.count("x")
y_count = text_2.count("y")
print(f"x: {x_count}, y: {y_count}")
# 6
print("Шестая задача")
text_3 = input("Введите текст: ")
bracket_left = text_3.find("(")
bracket_right = text_3.find(")")
bracket_left_end = text_3.rfind("(")
bracket_right_end = text_3.rfind(")")
result_1 = text_3[bracket_left+1:bracket_right]
result_2 = text_3[bracket_left_end+1: bracket_right_end]
print(result_1+"\n"+result_2)