import numpy as np

# generiranje fiksnih vrijednosti brojeva
np.random.seed(0)

# kreiranje 1-dimenzionalnog niza koji se popuni slučajnim brojevima 0 - 10
niz1 = np.random.randint(10, size=7)

# kreiranje 2-dimenzionalnog niza sa 4 retka i 4 stupca koji se popuni brojevima 0 - 10
niz2 = np.random.randint(10, size=(4, 4))

# kreiranje trodimenzionalnog niza koji sadrži 3 matrice sa 3 retka i 3 stupca popunjen brojevima 0 - 10
niz3 = np.random.randint(10, size=(3, 3, 3))

print(" niz3 Broj dimenzija: ", niz3.ndim)
print(" niz3 Veličina svake dimenzije: ", niz3.shape)
print(" niz3 Ukupna veličina niza: ", niz3.size)
print(" niz3 Tip podataka: ", niz3.dtype)
print(" niz3 Veličina jednog elementa niza u bajtima: ", niz3.itemsize)
print(" niz3 Ukupna veličina niza u bajtima: ", niz3.nbytes)

print("\n niz2 Broj dimenzija: ", niz2.ndim)
print(" niz2 Veličina svake dimenzije: ", niz2.shape)
print(" niz2 Ukupna veličina niza: ", niz2.size)
print(" niz2 Tip podataka: ", niz2.dtype)
print(" niz2 Veličina jednog elementa niza u bajtima: ", niz2.itemsize)
print(" niz2 Ukupna veličina niza u bajtima: ", niz2.nbytes)

print("\n niz1 Broj dimenzija: ", niz1.ndim)
print(" niz1 Veličina svake dimenzije: ", niz1.shape)
print(" niz1 Ukupna veličina niza: ", niz1.size)
print(" niz1 Tip podataka: ", niz1.dtype)
print(" niz1 Veličina jednog elementa niza u bajtima: ", niz1.itemsize)
print(" niz1 Ukupna veličina niza u bajtima: ", niz1.nbytes)