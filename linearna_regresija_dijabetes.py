import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import datasets

diabetes = datasets.load_diabetes()
x_train = diabetes.data[:-20]
y_train = diabetes.target[:-20]
x_test = diabetes.data[-20:]
y_test = diabetes.target[-20:]
x0_test = x_test[:, 0]
x0_train = x_train[:, 0]
x0_test = x0_test[:, np.newaxis]
x0_train = x0_train[:, np.newaxis]
linreg = linear_model.LinearRegression()
linreg.fit(x0_train, y_train)
y = linreg.predict(x0_test)
plt.scatter(x0_test, y_test, color='k')
plt.plot(x0_test, y, color='b', linewidth=3)
plt.show()