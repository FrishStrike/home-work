from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
x = 2*np.random.rand(100,1)
y = 4+3*x+np.random.randn(100,1)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

model = LinearRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

plt.figure(figsize=(10,5))
plt.scatter(x_train,y_train,color="blue", label="Обучающий набор")
plt.scatter(x_test,y_test,color="green", label="Тестовый набор",alpha=0.6)
plt.plot(x_test,y_pred,color="red",label="Линейная регрессия")
plt.xlabel("Признак")
plt.ylabel("Целевая переменная")
plt.title("Линейная регрессия: Обучающие и Тестовые наборы")
plt.legend()
plt.grid(True)
plt.show()