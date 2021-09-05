# Primjer jednostavne linearne regresije s jednom varijablom

# uvoz potrebnih biblioteka
import pandas as pd               # biblioteka za analizu podataka
import seaborn as sns             # biblioteka za vizualizaciju
import matplotlib.pyplot as plt   # biblioteka za vizualizaciju
from sklearn import linear_model  # uvoz linearnog modela iz sci-kit learn biblioteke

# uvoz skupa podataka u formatu csv i pridruživanje skupa pandas dataframe nizu
df = pd.read_csv("2018_FIFA_World_Cup_Squads.csv")

# prikaz prvih pet redaka skupa podataka za pretpregled i provjeru uvoza
df.head()

# prikaz distribucije točaka podataka razbacanim dijagramom
plt.scatter(df.Caps, df.Goals)

# prikaz korelacije između varijabli i provjera linearnosti
sns.heatmap(df.corr())

# pridruživanje vrijednosti stupca 'Utakmice' dataframe niza u nezavisnu varijablu X
X = df['Caps'].values

# pridruživanje vrijednosti stupca 'Golovi' dataframe niza u zavisnu varijable y
y = df['Goals'].values

# kreiranje objekta za linearnu regresiju
reg = linear_model.LinearRegression()

# treniranje modela linearne regresije
reg.fit(df[['Caps']], df.Goals)            # istovjetno naredbi - reg.fit(X, y)

# izračun koeficijenta, nagiba (slope)
print(reg.coef_)                        # rezultat: 0.15759523

# izračun presjeka (intercept)
print(reg.intercept_)                          # rezultat: -1.0121456651066145

# predviđanje koliko će igrač sa 20 nastupa zabiti golova?
reg.predict([[20]])                                          # rezultat: 2.139759

# ručna provjera predviđanja po formuli za regresiju
#  Y = a + bX  -> Y = (reg.intercept_) + (reg.coef_) * 20
#                 Y = (-1.0121456651066145) + (0.15759523) * 20 = 2,1397589348933855

# vizualizacija rezultata linearne regresije dijagramom

plt.xlabel('Utakmice', fontsize=25)
plt.ylabel('Golovi', fontsize=20)
plt.scatter(df.Caps, df.Goals, color='red')
plt.plot(df.Caps, reg.predict(df[['Caps']]), color='blue')
plt.show()

