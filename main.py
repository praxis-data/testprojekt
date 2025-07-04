import pandas as pd
import matplotlib.pyplot as plt

# CSV-Datei einlesen
df = pd.read_csv('daten/vwl_daten.csv')

# Daten anzeigen
print("Erste Zeilen der Daten:")
print(df.head())

# Durchschnittliches Einkommen berechnen
avg_income = df['Einkommen'].mean()
print(f"\nDurchschnittliches Einkommen: {avg_income:.2f} EUR")

# Inflationsrate über die Jahre plotten
plt.plot(df['Jahr'], df['Inflationsrate'], marker='o')
plt.title('Inflationsrate über die Jahre')
plt.xlabel('Jahr')
plt.ylabel('Inflationsrate (%)')
plt.grid(True)
plt.show()
