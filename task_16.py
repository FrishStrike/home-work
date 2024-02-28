# def func(x):
#     num_1 = int(x[0])**2 + int(x[1])**2
#     num_2 = int(x[1])**2 + int(x[2])**2
#     new_x = str(num_1) + str(num_2)
#     return new_x

# i = 100

# while i < 100000:
#     new_x = func(str(i))
#     if new_x == "9752":
#         print(i, new_x)
#     i += 1
  
print("x y w z")
for x in 0,1:
    for y in 0,1:
        for w in 0,1:
            for z in 0,1:
                if not((x <= y) <= w) and z:
                    print(x, y, w, z)