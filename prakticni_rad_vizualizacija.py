import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set(font_scale=1.4)

df = pd.read_csv('2018_FIFA_World_Cup_Squads.csv')

# Broj igrača po poziciji - stupčani dijagram
df.Position.value_counts().plot(kind='bar')
plt.xlabel("Pozicije igrača", labelpad=20)
plt.ylabel("Broj igrača", labelpad=20)
plt.title("Broj igrača po pozicijama", y=1.05);

# Broj igrača po starosti - stupčani dijagram
df['Age'].value_counts().sort_index().plot(kind='bar', figsize=(6, 6))
plt.xlabel("Godine igrača", labelpad=20)
plt.ylabel("Broj igrača", labelpad=20)
plt.title("Broj igrača po starosti", y=1.05);

# Broj igrača po starosti - horizontalni stupčani dijagram
df['Age'].value_counts().sort_index().plot(kind='barh', figsize=(8, 6))
plt.xlabel("Broj igrača", labelpad=14)
plt.ylabel("Godine igrača", labelpad=14)
plt.title("Broj igrača po starosti", y=1.02);


