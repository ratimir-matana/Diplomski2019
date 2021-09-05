import pandas as pd  # biblioteka za analizu podataka
import matplotlib.pyplot as plt  # biblioteka za vizualizaciju
from sklearn.preprocessing import StandardScaler  # uvoz objekta za standardizaciju skupa podataka
from sklearn.decomposition import PCA  # uvoz objekta za PCA analizu

# uvoz skupa podataka u formatu csv i pridruživanje skupa pandas dataframe nizu
df = pd.read_csv("2018_FIFA_World_Cup_Squads.csv")

# prikaz prvih pet redaka skupa podataka za pretpregled i provjeru uvoza
df.head()

# pridruživanje stupaca u varijablu features, 4-dimenzionalni niz
features = ['Squad Number', 'Age', 'Caps', 'Goals']

# izdvajanje vrijednosti stupaca iz varijable features dataframe niza u varijablu x
x = df.loc[:, features].values

# izdvajanje vrijednosti stupca Club dataframe niza u varijablu y koja predstavlja target
y = df.loc[:, ['Club']].values

# Standardizacija stupaca na jediničnu skalu (srednja vrijednost = 0 i varijanca = 1)
x = StandardScaler().fit_transform(x)

# kreiranje instance, objekta PCA klase i postavljanje argumenta n-components na vrijednost 2
pca = PCA(n_components=2)

# redukcija 4-dimenzionalnog niza na 2 dimenzije
principalComponents = pca.fit_transform(x)

# pridruživanje 2-dimenzionalnog dataframe niza u varijablu principaldf
principaldf = pd.DataFrame(data=principalComponents,
                           columns=['Principal component 1', 'Principal component 2'])

# konkatenacija niza principaldf sa odredišnim nizom Club u finalni niz
finaldf = pd.concat([principaldf, df[['Club']]], axis=1)

# vizualizacija pca analize dijagramom

# kreiranje figure širine 7 i visine 7
fig = plt.figure(figsize=(7, 7))

# dodavanje podcrteža figuri (broj redaka, broj stupaca, indeks podcrteža)
ax = fig.add_subplot(1, 1, 1)

# postavljanje naziva labele za x-os
ax.set_xlabel('Principal Component 1', fontsize=20)

# postavljanje naziva labele za y-os
ax.set_ylabel('Principal Component 2', fontsize=20)

# postavljanje naslova
ax.set_title('PCA analiza', fontsize=20)

# inicijalizacija liste klubovi vrijednostima koje su prisutne u stupcu Club
klubovi = ['Real Madrid', 'Barcelona', 'Valencia']

# inicijalizacija liste boje vrijednostima (r - crvena, g - zelena, b - plava)
boje = ['r', 'g', 'b']

# for petlja za iteraciju po stupcu Club dataframe niza finaldf i crtanje točaka
for target, color in zip(klubovi, boje):
    indeks_retka = finaldf['Club'] == target
    ax.scatter(finaldf.loc[indeks_retka, 'Principal component 1']
               , finaldf.loc[indeks_retka, 'Principal component 2']
               , c=color
               , s=50)

# kreiraj legendu
ax.legend(klubovi)
# kreiraj kvadratnu mrežu
ax.grid()
# prikaži vizualizaciju
plt.show()

# prikaz omjera varijanci u postocima
pca.explained_variance_ratio_

