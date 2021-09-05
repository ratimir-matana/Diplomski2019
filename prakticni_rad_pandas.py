import pandas as pd

df = pd.read_csv('2018_FIFA_World_Cup_Squads.csv')

print('Retci x stupci:', df.shape)
print('Retci ili opservacije:', df.columns)
print('\n')

print('Godine    Broj igrača ')  # Broj igrača sortiran prema starosti
print(df.Age.value_counts().sort_index())

print('\n')  # Koje su starosne skupine
print('Najmanja starosna dob: ', df.Age.min())
print('Najstarija starosna dob: ', df.Age.max())
print('Prosječna starosna dob:', df.Age.mean())

print('\n')
print('Momčad    Broj igrača')   # Koliko igrača ima svaka momčada?
print(df.Team.value_counts().sort_index())

print('\n')  # Operacija dijeljenja - Prikaz najmlađih igrača
print('Prikaz svih 19-godišnjih igrača:')
print(df[df.Age==19])

print('\n')
print('Pozicija   Broj igrača ')  # Koliko ima veznih, obrambenih, napadača
print(df.Position.value_counts().sort_index())

print('\n')
print(df[df.Team=='Brazil'])    # Operacija dijeljenja - prikaz momčadi Brazila

print('\n')
print(df[df.Club.isnull()])   # Ima li igrača koji su trenutno bez kluba?

print('\n')
print('Broj pozicija igrača Nigerijske momčadi:')       # Broj pozicija igrača po jednoj momčadi
print(df[df.Team=='Nigeria'].Position.value_counts())

print('\n')
print('Broj ruskih igrača po poziciji koji igraju u klubu CSKA Moskva')
print(df[(df.Team=='Russia') & (df.Club=='CSKA Moscow')].Position.value_counts())


