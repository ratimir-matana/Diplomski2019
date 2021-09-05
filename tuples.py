# deklaracija n-torke vjestine
vjestine = ("Aikido", "Judo", "Capoeira")

# ispis n-torke
print("\n Borilačke vještine: ", vjestine)

# pristup prvom elementu n-torke
print("\n", vjestine[0])

print("\n")
# iteracija nad elementima n-torke
for x in vjestine:
    print(x)
if "Capoeira" in vjestine:
    print("\n Capoeira se nalazi u ntorki")

# trenutni broj elemenata n-torke
print("\n Broj elemenata ntorke: ", len(vjestine))

# trenutni sadržaj n-torke
# print(vjestine)

# kreiranje n-torke kroz konstruktor
vjestine2 = tuple(("Jeet Kune Do", "Kung Fu", "Muay Thai"))

# ispis trenutnog sadržaja n-torke vjestine2
print("\n Vjestine2: ", vjestine2)

# brisanje n-torke vjestine2
del(vjestine2)

# provjera koliko se puta element ponavlja u n-torki
print("\n Broj pojavljivanja elemenata Judo: ", vjestine.count("Judo"))

# provjera koju vrijednost indeksa ima element
print("\n Indeks elementa Aikido: ", vjestine.index("Aikido"))
