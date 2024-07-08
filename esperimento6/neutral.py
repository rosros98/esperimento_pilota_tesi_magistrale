import pandas as pd

# Carica il file CSV
df = pd.read_csv("df_emotion_sentiment_final.csv")

# Standardizza i valori della colonna "Interlocutore" (ignorando maiuscole/minuscole)
df['Interlocutore'] = df['Interlocutore'].str.lower()

# Rimuove le righe con valore "NEUTRAL" nella colonna "Dominant_Sentiment"
df_filtered = df[df['Dominant_Sentiment'] != 'NEUTRAL']

# Salva il nuovo dataset in un nuovo file CSV
df_filtered.to_csv("without_neutral.csv", index=False)
