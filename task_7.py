from functools import reduce
# 1
print("Первая задача")
arr_1 = [1, 2, 3]
arr_2 = [4, 5, 6]
arr_3 = list(map(lambda x, y: x+y, arr_1, arr_2))
print(arr_3)
# 2
print("Вторая задача")
lst_1 = [12, 23, 13, 39, 144, 71]
lst_2 = list(filter(lambda x: x % 12 == 0 or x % 13 == 0, lst_1))
print(lst_2)
# 3
print("Третья задача")
new_lst = [-2, 5, 12, 10, 0, -1, 9]
res = reduce(lambda x, y: x if(x>y) else y, new_lst)
print(res)