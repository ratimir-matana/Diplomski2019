import numpy as np

# generiranje fiksnih vrijednosti brojeva
np.random.seed(0)

# kreiranje jednodimenzionalnog niza a koji se popuni slučajnim brojevima 0 - 10
a = np.random.randint(10, size=8)

# kreiranje dvodimenzionalnog niza b sa 4 retka i 4 stupca koji se popuni brojevima 0 - 10
b = np.random.randint(10, size=(4, 4))

# kreiranje trodimenzionalnog niza c koji sadrži 3 matrice sa 3 retka i 3 stupca popunjen brojevima 0 - 10
c = np.random.randint(10, size=(3, 3, 3))

print("\n Niz a: ", a)
print("\n Prvi element niza a:", a[0])
print("\n Zadnji element niza a:", a[-1])
print("\n Predzadnji element niza a:", a[-2])
print("\n")

# ispis dvodimenzionalnog niza b
print(b)

# ispis elementa dvodimenzionalnog niza b koji se nalazi na početku prvog retka i prvog stupca
print("\n Element [0,0]:", b[0, 0])

# promjena vrijednosti elementa
b[0, 0] = 7

# ispis nakon promjene vrijednosti
print("\n Element [0,0]:", b[0, 0])