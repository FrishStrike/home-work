import scikitplot as skplt
from sklearn import datasets
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

hard_problem = datasets.make_classification(
    n_samples=100,
    n_features=100,
    n_informative=50,
    n_classes=3,
    n_redundant=50,
    n_clusters_per_class=1,
    random_state=42,
)

X_train, X_test, y_train, y_test = train_test_split(
    *hard_problem,
    test_size=0.3,
    random_state=1,
)

clf = KNeighborsClassifier(n_neighbors=8)
clf.fit(X_train, y_train)

predictions = clf.predict(X_test)
accuracy_score(y_test, predictions)


param_grid = {'n_neighbors': np.arange(1, 20)}
knn = KNeighborsClassifier()
grid_search = GridSearchCV(knn, param_grid, cv=5)
grid_search.fit(X_train, y_train)
k_optim = grid_search.best_params_['n_neighbors']

accuracy_values = []
for k in np.arange(1, 20):
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracy_values.append(accuracy)

plt.figure(figsize=(10, 6))
plt.plot(np.arange(1, 20), accuracy_values, marker='o')
plt.xlabel('Number of Neighbors (k)')
plt.ylabel('Accuracy')
plt.title('Accuracy vs Number of Neighbors')
plt.grid(True)
plt.show()

clf = KNeighborsClassifier(n_neighbors=16, weights='uniform', metric='euclidean')
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print("Test accuracy: %.5f" % accuracy)
assert accuracy > 0.8, "попробуйте изменить следующие параметры: penalty, solver"

print('Хорошая работа!')

skplt.metrics.plot_confusion_matrix(y_test, y_pred, normalize=True)

print(classification_report(y_test, y_pred))