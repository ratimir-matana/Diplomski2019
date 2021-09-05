import numpy as np
import pandas as pd
import datetime

# deklaracija niza tipa datetime
date = np.array('2019-02-28', dtype=np.datetime64)
print("\n", date)

# primjer vektorske operacije nad nizom date
print("\n", date + np.arange(8))

# deklaracija tipa datetime
date2 = np.datetime64('2019-02-28 12:30')
print("\n", date2)

# primjer prosljeđivanja funkciji to_datetime()
date3 = pd.to_datetime("28th of February, 2019")
print("\n Timestamp:", date3)

# primjer prosljeđivanja funkciji to_datetime() nizova datuma
print("\n DatetimeIndex:", date3 + pd.to_timedelta(np.arange(8), 'D'))

# deklaracija nizova datuma tipa DatetimeIndex
date4 = pd.DatetimeIndex(['2018-02-28', '2019-02-28',
'2018-03-21', '2019-03-21'])

# indeksiranje podataka po vremenskim pečatima
data = pd.Series([0, 1, 2, 3], index=date4)

print("\n")
# ispis indeksiranih datumskih podataka
print(data)


