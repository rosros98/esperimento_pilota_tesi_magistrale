import pandas as pd
import re

# Carica il file CSV
df = pd.read_csv("without_neutral.csv")

# Estrai il valore numerico dall'emozione
df['Emotion_Value'] = df['Emotion'].str.extract(r'\(([^)]+)\)').astype(float)

# Filtra le righe con valori di emozione >= 0.5
# prendere l'emozione con percentuale maggiore
df_filtered = df[df['Emotion_Value'] >= 0.5]

# Raggruppa per "Interlocutore" e calcola il sentimento ed emozione più comune e le emozioni dominanti con valore più alto
grouped = df_filtered.groupby('Interlocutore').agg({
    'Dominant_Emotion': lambda x: x.value_counts().idxmax()
}).reset_index()

# Rinomina le colonne
grouped.columns = ['Interlocutore', 'Emozione_Comune']

# Salva il risultato in un nuovo file CSV
grouped.to_csv("sentimento_emozione_per_individuo.csv", index=False)
