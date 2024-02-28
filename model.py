import numpy as np
x1 = np.random.randint(100, size = 100)
x2 = np.random.randint(200, size = 100)
y = 3 * x1 + 2 * x2 - 1
# x1 = x1 + np.random.randint(5, size = 100) / 10
# x2 = x2 + np.random.randint(5, size = 100) / 10
# y = y + np.random.randint(5, size = 100) / 10

w1 = 0
w2 = 0
b = 0

lr = 0.02
epochs = 1000

losses = []
for epoch in range(1, epochs+1):
    for i in range(len(x1)):
        prediction = w1*x1[i] + w2*x2[i] + b
        w1 += 2*lr*x1[i]*(y[i]-prediction)
        w2 += 2*lr*x2[i]*(y[i]-prediction)
        b += 2*lr*(y[i]-prediction)
    loss=0
    for i in range(len(x1)):
        loss += (y[i]-(w1*x1[i]+w2*x2[i]+b))**2
    losses.append(loss)

print("w1  =", w1, "w2 =",  w2, "b =", b)