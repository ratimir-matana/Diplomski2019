import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA

iris = datasets.load_iris()
species = iris.target  # Vrste
x_reduced = PCA(n_components=3).fit_transform(iris.data)

# SCATTERPLOT 3D - 3D raspršeni crtež
fig = plt.figure()
ax = Axes3D(fig)
ax.set_title('PCA - Iris skup podataka ', size=14)
ax.scatter(x_reduced[:, 0], x_reduced[:, 1], x_reduced[:, 2], c=species)
ax.set_xlabel('Prvi eigenvector')      # prvi karakteristični ili svojstveni vektor
ax.set_ylabel('Drugi eigenvector')     # drugi karakteristični ili svojstveni vektor
ax.set_zlabel('Treći eigenvector')      # treći karakteristični ili svojstveni vektor
ax.w_xaxis.set_ticklabels(())
ax.w_yaxis.set_ticklabels(())
ax.w_zaxis.set_ticklabels(())
plt.show()
