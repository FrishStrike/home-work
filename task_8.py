lst = [1, 2, -3, -2, 83, 23, 71, 97, 3, 4, 32, 53, 70]
def maximum(lst, res=0):
    if res < lst[0]:
        res = lst[0]
    if len(lst) == 1:
        return res
    result = maximum(lst[1:], res)
    return result
result = maximum(lst)
print(result)