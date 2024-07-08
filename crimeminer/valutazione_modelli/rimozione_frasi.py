import pandas as pd

# Carica il dataset dal file CSV
df = pd.read_csv('../frase_sentiment_emotion_modificato.csv')

# Filtra le righe per mantenere solo quelle con "POSITIVE" e "NEGATIVE" nella colonna "sentimento"
df_filtered = df[df['sentimento'].isin(['POSITIVE', 'NEGATIVE'])]

# Mantieni solo la colonna "frase"
df_filtered = df_filtered[['frase']]

# Prendi solo le prime 300 righe
df_filtered = df_filtered.head(300)

# Se vuoi salvare il risultato in un nuovo file CSV
df_filtered.to_excel('frase_300.xlsx', index=False)

# Se non vuoi salvare il risultato ma solo vedere il dataframe risultante
print(df_filtered)
