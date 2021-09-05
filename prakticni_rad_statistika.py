import scipy as sp
import pandas as pd

df = pd.read_csv('2018_FIFA_World_Cup_Squads.csv')

print('Prosječna starost igrača:', sp.mean(df.Age))
print('Središnja vrijednost starosti igrača:', sp.median(df.Age))
print('Standardna devijacija starosti igrača:', sp.std(df.Age))
print('Varijanca starosti igrača:', sp.var(df.Age))

print('\n')

print('Prosječna vrijednost odigranih utakmica:', sp.mean(df.Caps))
print('Središnja vrijednost odigranih utakmica:', sp.median(df.Caps))
print('Standardna devijacija odigranih utakmica:', sp.std(df.Caps))
print('Varijanca odigranih utakmica:', sp.var(df.Caps))

print('\n')

print('Prosječna vrijednost datih golova:', sp.mean(df.Goals))
print('Središnja vrijednost datih golova:', sp.median(df.Goals))
print('Standardna devijacija datih golova:', sp.std(df.Goals))
print('Varijanca datih golova:', sp.var(df.Goals))



