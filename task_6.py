# 1
print("Первое задание")
def isPalindrome(string):
    result = False
    string_list = filter(lambda x: x != " ", string)
    string = "".join(string_list)
    string = string.lower()
    i = 0
    k = len(string)-1
    while string[i] == string[k]:
        i += 1
        k -= 1
        if i > k:
            result = True
            break
    return result
palindrome = input("Введите палиндром: ")
result = isPalindrome(palindrome)
print(result)
# 2
print("Второе задание")
def registration(name, lastname, surname, age):
    return f"{name} {lastname} {surname} {age} зарегистрирован"
res = registration("Данила", "Печерикин", "Дмитриевич", "2007 г.р.")
print(res)
# 3
print("Третье задание")
def maximum(num_1, num_2, num_3=0):
    nums = [num_1, num_2, num_3]
    res_num = 0
    for i in range(len(nums)):
        if nums[i] > res_num:
            res_num = nums[i]
    return res_num
res_num = maximum(5, 3, 7)
print(res_num)