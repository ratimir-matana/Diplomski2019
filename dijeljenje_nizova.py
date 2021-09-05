import numpy as np

# generiranje fiksnih vrijednosti brojeva
np.random.seed(0)  #

# kreiranje 1-dimenzionalnog niza
niz1 = np.random.randint(10, size=7)

# ispis sadržaja niza
print("\n", niz1)

# ispis prvih 3 elemenata
print("\n", niz1[:3])

# ispis elemenata koji se nalaze iza indeksa 3
print("\n", niz1[3:])

# ispis podniza na sredini
print("\n", niz1[3:5])

# ispis svakog drugog elementa
print("\n", niz1[::2])

# ispis svakog drugog elementa počevši od indeksa 3
print("\n", niz1[3::2])

# ispis elemenata obrnutim poretkom
print("\n", niz1[::-1])

# ispis svakog drugog elementa obrnutog poretka počevši od indeksa 2
print("\n", niz1[2::-2])

# kreiranje 2-dimenzionalnog niza sa 4 retka i 4 stupca koji se popuni brojevima 0 - 10
niz2 = np.random.randint(10, size=(4, 4))

# ispis sadržaja 2-dimenzionalnog niza
print("\n", niz2)

# rezanje koje napravi novi niz od 3 retka i 3 stupca
print("\n", niz2[:3, :3])

# rezanje koje napravi novi niz od 4 retka i svakog drugog stupca
print("\n", niz2[:4, ::2])

# ispis niza obrnutim poretkom
print("\n", niz2[::-1, ::-1])

# ispis drugog stupca niza2
print("\n", niz2[:, 1])

# ispis drugog retka niza2
print("\n", niz2[1, :])

