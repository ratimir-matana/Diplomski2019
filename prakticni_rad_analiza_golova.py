# uvoz potrebnih biblioteka
import pandas as pd       # biblioteka za analizu podataka
import matplotlib as plt  # biblioteka za vizualizaciju

# uvoz skupa podataka u formatu csv i pridruživanje skupa pandas dataframe nizu
df = pd.read_csv("2018 FIFA World Cup Squads(hor1).csv")

# prikaz prvih pet redaka skupa podataka za pretpregled i provjeru uvoza
print(df.head())

# prikaz broja igrača po pojedinom horoskopskom znaku
print('Horoskop    Broj igrača')
print(df.Horoscope.value_counts())

# vizualni prikaz broja igrača po pojedinom horoskopskom znaku
print(df.Horoscope.value_counts().sort_values().plot(kind='bar'))

print('Broj postignutih golova po horoskopskom znaku igrača')
print('\n')
print('Igrači s horoskopskim znakom vodenjaka zabili su: ', df[df.Horoscope == 'Aquarius'].Goals.sum())
print('Igrači s horoskopskim znakom ribe zabili su: ', df[df.Horoscope == 'Pisces'].Goals.sum())
print('Igrači s horoskopskim znakom ovna zabili su: ', df[df.Horoscope == 'Aries'].Goals.sum())
print('Igrači s horoskopskim znakom bika zabili su: ', df[df.Horoscope == 'Taurus'].Goals.sum())
print('Igrači s horoskopskim znakom blizanca zabili su: ', df[df.Horoscope == 'Gemini'].Goals.sum())
print('Igrači s horoskopskim znakom raka zabili su: ', df[df.Horoscope == 'Cancer'].Goals.sum())
print("\n")
print('Igrači s horoskopskim znakom lava zabili su: ', df[df.Horoscope == 'Leo'].Goals.sum())
print('Igrači s horoskopskim znakom djevice zabili su: ', df[df.Horoscope == 'Virgo'].Goals.sum())
print('Igrači s horoskopskim znakom vage zabili su: ', df[df.Horoscope == 'Libra'].Goals.sum())
print('Igrači s horoskopskim znakom škorpiona zabili su: ', df[df.Horoscope == 'Scorpio'].Goals.sum())
print('Igrači s horoskopskim znakom strijelca zabili su: ', df[df.Horoscope == 'Sagittarius'].Goals.sum())
print('Igrači s horoskopskim znakom jarca zabili su: ', df[df.Horoscope == 'Capricorn'].Goals.sum())
print('\n')
print('Ukupan broj golova: ', df.Goals.sum())

# prikaz broja igrača po horoskopskom znaku i njihovih postignutih golova
# počevši od najmanje postignutih golova i najvećeg broja igrača
print(df.groupby('Goals')['Horoscope'].value_counts())

# prikaz broja igrača i njihovih postignutih golova po horoskopskom znaku
# počevši od najmanje postignutih pa do najviše postignutih golova
print(df.groupby('Horoscope')['Goals'].value_counts())
