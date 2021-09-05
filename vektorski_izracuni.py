import numpy as np

# generiranje fiksnih vrijednosti brojeva
np.random.seed(0)

# kreiranje 1-dimenzionalnog niza koji se popuni slučajnim brojevima 0 - 10
niz1 = np.random.randint(10, size=7)

# kreiranje 1-dimenzionalnog niza koji se popuni slučajnim brojevima 0 - 10
niz2 = np.random.randint(10, size=7)

# ispis sadržaja niza1
print("\n Niz1: ", (niz1))

# ispis sadržaja niza2
print("\n Niz2: ", (niz2))

# zbroj nizova
print("\n Zbrajanje:", np.add(niz1, niz2))

# oduzimanje nizova
print("\n Oduzimanje: ", np.subtract(niz1, niz2))

# množenje nizova
print("\n Množenje: ", np.multiply(niz1, niz2))

# dijeljenje nizova
print("\n Dijeljenje: ", np.divide(niz1, niz2))

# potenciranje nizova
print("\n Potenciranje: ", np.power(niz1, niz2))

# jednakost nizova
print("\n Jednakost: ", np.array_equal(niz1, niz2))

# kvadratni korijen niza1
print("\n Kvadratni korijen: ", np.sqrt(niz1))

# prirodni logaritam niza2
print("\n Logaritam: ", np.log(niz2))

# sinus niz2
print("\n Sinus: ", np.sin(niz2))

# apsolutna vrijednost niza2
print("\n Apsolutna vrijednost: ", np.abs(niz2))

# zaokruživanje na najveće cijele brojeve niza1
print("\n Zaokruživanje:  ", np.round(niz1))

# zaokruživanje na najmanje cijele brojeve koji su veći ili jednaki od elemenata niza1
print("\n Zaokruživanje na najmanje cijelo:", np.ceil(niz1))

# zaokruživanje na najveće cijele brojeve koji su manji ili jednaki od elemenata niza1
print("\n Zaokruživanje na najveće cijelo:", np.floor(niz1))
