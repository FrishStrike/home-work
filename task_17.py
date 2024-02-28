import matplotlib.pyplot as plt

x = [1,3,7]
y = [2,6,14]

plt.scatter(x,y,color="red")
plt.plot([1,7],[0.379008,1.945856*7+0.379008])
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.show()