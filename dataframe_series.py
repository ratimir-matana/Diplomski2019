import pandas as pd

# deklaracija serija a
a = pd.Series([2, 6, 8, 11], index=['a', 'b', 'c', 'd'])

# sadržaj serija a
print(a)

# ključevi serije a
print("\n Ključevi: ", a.keys())

print("\n")

# dodavanje novog elementa u seriju a
a['e'] = 13

# provjera sadržaja serije a
print(a)

print("\n")

# rezanje serije a sa eksplicitnim indeksom
print("Dijeljenje: ")
print(a['a':'c'])

# deklaracija podataka za DataFrame niz koristeći rječnik
data = {'Tvtka': ['Microsoft', 'Gigabyte', 'NEC'],
        'Država': ['USA', 'Taiwan', 'Japan'],
        'Zaposlenici': [134944, 1303171035, 207847528]}

# deklaracija DataFrame niza df1
df1 = pd.DataFrame(data, columns=['Tvrtka', 'Država', 'Zaposlenici'])

# broj redaka i stupaca DataFrame niza df1
print("\n Veličina: ", df1.shape)

# kreiranje DataFrame niza iz serije a
df2 = pd.DataFrame(a, columns=['a'])

# ispis kreiranog DataFrame niza
print("\n DataFrame: ", df2)

# eksplicitno kreiranje indeksa
indeks1 = pd.Index([1, 4, 6, 8, 10])

# provjera ispisom
print("\n Indeks: ", indeks1)

# ispis vrijednosti serije a
print("\n Vrijednosti: ", a.values)

# ispis vrijednosti za indekse serije a
print("\n Indeksi: ", a.index)

# dohvaćanje jednog elementa iz serije a
print("\n Element: ", a['b'])

# dohvaćanje podniza Dataframe
print("\n", df1[1:])



