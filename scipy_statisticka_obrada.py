import scipy as sp
import numpy as np
from scipy import stats

# generiranje fiksnih vrijednosti brojeva
np.random.seed(0)

# generiranje podataka - kreiranje numeričkog 1-dimenzionalong niza koji se popuni slučajnim brojevima
np1 = np.random.randint(20, size=15)
print('Podaci: ', np1)

# statistika
print('Mean:', sp.mean(np1))  # aritmetička sredina svih stupaca
print('Median:', sp.median(np1))  # središnja vrijednost za svaki stupac
print('Standard deviation (std):', sp.std(np1))  # standardna devijacija za svaki stupac
print('Max:', max(np1))  # najveća/maksimalna vrijednost
print('Min:', min(np1))  # najmanja/minimalna vrijednost
print('Production:', sp.prod(np1))  # produkt
print('Variance:', sp.var(np1))  # varijanca
print('Sum:', sp.sum(np1))  # suma
print('Skew:', sp.stats.skew(np1))  # asimetričnost/neujednačenost

