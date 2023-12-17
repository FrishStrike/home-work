import matplotlib.pyplot as plt
import numpy as np

# 1

x = np.linspace(1, 8, 100)

def myFunc(x):
    return np.sin(x**5)*1000

plt.axis([0, 10, 0, 10])
plt.xticks(np.arange(9), ("0", "1", "2", "3", "4", "5", "6", "7", "8"))
plt.yticks(np.arange(9), ("0", "1", "2", "3", "4", "5", "6", "7", "8"))

plt.xlabel("X")
plt.ylabel("Y")

plt.title("График")

plt.grid()

plt.plot(x, myFunc(x), color="g", dashes=[2, 2], label="Вот такая моя функция", alpha=0.5)

plt.legend(loc=0)
plt.show()

# 2

X = np.random.normal(0, 1, 3000)
Y = np.random.normal(3, 4, 3000)

plt.scatter(X, Y, c=["b"], marker="*", s=20, alpha=0.2)

plt.xlabel("X")
plt.ylabel("Y")

plt.title("График")

plt.grid()

plt.show()

# 3

data = np.random.normal(16, 2, 1000)

plt.hist(data, color="r", alpha=0.5)

plt.show()