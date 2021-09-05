# uvoz matplotlib biblioteke
import matplotlib.pyplot as plt

# korak 1: priprema podataka
x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

# korak 2: kreiranje crteža - kreiranje figure
fig = plt.figure()

# korak 3: crtanje
# crtanje koordinatnih osi - redak, stupac, broj panela
ax = fig.add_subplot(1, 1, 1)

# postavljanje naslova i oznaka za x i y os
ax.set(title='Primjer grafa s povezanim i nepovezanim točkama',
       ylabel='Y-os',
       xlabel='X-os')

# crtanje grafa s linijom plave boje i debljine 4
ax.plot(x, y, color='blue', linewidth=4)

# 4 korak: modifikacija crteža
# crtanje nepovezanih točaka i dodavanje boje i markera
ax.scatter([3, 4, 5],
           [20, 30, 40],
           color='red',
           marker='x')

# postavljanje ograničenja za x os od 1 do 7
ax.set_xlim(1, 7)

# postavljanje ograničenja za x os od 1 do 50
ax.set_ylim(10, 50)

# korak 5: spremanje crteža u png formatu
plt.savefig('axes.png')

# korak 6: prikaz crteža
plt.show()
