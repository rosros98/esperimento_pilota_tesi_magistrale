import pandas as pd
import matplotlib.pyplot as plt
import time

# Leggi il file CSV
df = pd.read_csv("sentimento_emozione_per_individuo.csv")

# Definisci i colori per ogni emozione
colori = {'anger': 'red', 'fear': 'orange', 'joy': 'green', 'sadness': 'blue'}

# Itera su ogni riga del dataframe
for index, row in df.iterrows():
    # Dividi la stringa in coppie di emozioni e percentuali
    emozioni_percentuali = row['Emozioni_Dominanti'].split(',')
    emozioni = [emozioni_percentuali[i].strip().strip("'") for i in range(0, len(emozioni_percentuali), 2)]
    percentuali = [float(emozioni_percentuali[i].strip().strip("()")) for i in range(1, len(emozioni_percentuali), 2)]

    # Filtra le emozioni e le percentuali comprese tra 0.99 e 0.80
    emozioni_filtrate = [emozioni[i] for i in range(len(percentuali)) if 0.80 <= percentuali[i] <= 1.0]
    percentuali_filtrate = [percentuali[i] for i in range(len(percentuali)) if 0.80 <= percentuali[i] <= 1.0]

    # Crea il grafico a linee solo se ci sono dati filtrati
    if emozioni_filtrate:
        plt.figure(figsize=(10, 6))
        plt.plot(emozioni_filtrate, percentuali_filtrate, marker='o')

        # Aggiungi titolo e label agli assi
        plt.title(f'Emozioni per {row["Interlocutore"]}')
        plt.xlabel('Emozione')
        plt.ylabel('Percentuale')
        plt.ylim(0.8, 1.0)  # Assicura che l'asse y vada da 0 a 1 per le percentuali

        # Mostra il grafico
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        time.sleep(5)  # Aggiungi un ritardo di 1 secondo
    else:
        print(f"Nessun dato filtrato trovato per {row['Interlocutore']}.")
