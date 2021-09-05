import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

x = np.array([[1, 3], [1, 2], [1, 1.5], [1.5, 2], [2, 3], [2.5, 1.5],
             [2, 1], [3, 1], [3, 2], [3.5, 1], [3.5, 3]])
y = [0]*6 + [1]*5
svc = svm.SVC(kernel='linear', C=0.1).fit(x, y)
X, Y = np.mgrid[0:4:200j, 0:4:200j]
Z = svc.decision_function(np.c_[X.ravel(), Y.ravel()])
Z = Z.reshape(X.shape)
plt.contourf(X, Y, Z > 0, alpha=0.4)
plt.contour(X, Y, Z, colors=['k', 'k', 'k'], linestyles=['--', '-', '--'], levels=[-1, 0, 1])
plt.scatter(svc.support_vectors_[:, 0], svc.support_vectors_[:, 1], s=120, facecolors='w')
plt.scatter(x[:, 0], x[:, 1], c=y, s=50, alpha=0.9)
plt.show()