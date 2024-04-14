from sklearn.datasets import fetch_openml
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import scikitplot as skplt
from sklearn import metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix

mnist = fetch_openml(data_id=554)
type(mnist.data), type(mnist.categories), type(mnist.feature_names), type(mnist.target)
data = np.array(mnist.data)
targets = np.array(mnist.target)
plt.figure(figsize=(20,4))
for index, (image, label) in enumerate(zip(data[0:5],
                                           targets[0:5])):
    plt.subplot(1, 5, index + 1)
    plt.imshow(np.reshape(image, (28,28)), cmap=plt.cm.gray)
    plt.title('Training: ' + label, fontsize = 20);
X_train, X_test, y_train, y_test = train_test_split(data[:10000,:],
                                                   targets[:10000].astype('int'), #targets str to int convert
                                                   test_size=1/7.0,
                                                   random_state=0)


clf = LogisticRegression(n_jobs=5, tol=0.01, max_iter=1000,penalty='l2',solver='saga')
clf.fit(X_train, y_train)



y_pred = clf.predict(X_test)
accuracy = np.mean(y_pred == y_test)

print("Test accuracy: %.5f" % accuracy)
assert accuracy > 0.9, "попробуйте изменить следующие параметры: penalty, solver"

print('Хорошая работа!')

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Calculate precision
precision = precision_score(y_test, y_pred, average='weighted')
print("Precision:", precision)

# Calculate recall (sensitivity)
recall = recall_score(y_test, y_pred, average='weighted')
print("Recall (Sensitivity):", recall)

# Calculate F1-score
f1 = f1_score(y_test, y_pred, average='weighted')
print("F1-Score:", f1)

skplt.metrics.plot_confusion_matrix(y_test, y_pred, normalize=True)

print(classification_report(y_test, y_pred))