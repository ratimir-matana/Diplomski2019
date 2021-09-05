# deklaracija liste sa 3 elemenata
drvece = ["Breza", "Brijest", "Jasen"]

# ispis sadržaja liste
print("\n Ispis liste nakon deklaracije: ", drvece)

# ispis drugog elementa liste koristeći indeks
print("\n Ispis drugog elementa: ", drvece[1])

# promjena vrijednosti trećeg elementa
drvece[2] = "Hrast"

# ispis sadržaja liste
print("\n Ispis nakon promjene elementa: ", drvece)

print("\n")
# iteracija elemenata liste for petljom, ispis svih elemenata liste
for drvo in drvece:
    print(drvo)

print("\n")
# provjera da li se element nalazi u listi
if "Breza" in drvece:
  print("'Breza' se nalazi u listi")
# provjera broja elemenata liste pomoću len() metode
print("\n Trenutni broj elemenata liste: ", len(drvece))

# dodavanje novog elementa na kraj liste
drvece.append("Cedar")

# provjera sadržaja liste
print("\n Ispis nakon dodavanja elementa: ", drvece)

# provjera trenutnog broja elemenata liste
print("\n Trenutni broj elemenata liste: ", len(drvece))

# dodavanje elementa na treću poziciju
drvece.insert(2, "Bukva")

# provjera dodavanja elemenata
print("\n Ispis nakon dodavanja elementa: ", drvece)

# brisanje elementa 'Hrast' iz liste drvece
drvece.remove("Hrast")

# provjera sadržaja liste ispisom
print("\n Ispis nakon micanja elementa: ", drvece)

# provjera trenutnog broja elemenata
print("\n Trenutni broj elemenata liste: ", len(drvece))

# brisanje trećeg elementa iz liste
drvece.pop(2)

# provjera sadržaja liste
print("\n Ispis nakon micanja elementa: ", drvece)

# promjena redoslijeda elemenata liste
drvece.reverse()

# provjera sadržaja liste
print("\n Ispis nakon promjene redoslijeda: ", drvece)

# sortiranje liste abecednim redoslijedom
drvece.sort()

# provjera sadržaja liste
print("\n Ispis nakon sortiranja: ", drvece)

# najmanji element liste po abecedi
print("\n Minimalni element liste: ", min(drvece))

# najveći element po abecedi
print("\n Maksimalni element liste: ", max(drvece))

# provjera vrijednosti indeksa elementa liste 'Brijest'
print("\n Element Brijest ima vrijednost indeksa: ", drvece.index('Brijest'))

# konkatenacija ili nadovezivanje elemenata liste drvece
nadovezivanje = ''
for drvo in drvece:
    nadovezivanje = nadovezivanje + drvo
print("\n Rezultat nadovezivanja: ", nadovezivanje)
