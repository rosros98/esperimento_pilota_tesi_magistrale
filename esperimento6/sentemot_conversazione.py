import pandas as pd

# Metrica per le conversazioni
# Carica il file CSV
df = pd.read_csv("without_neutral.csv")

# Considerando la colonna ID, che corrisponde a ogni conversazione
# si effettua calcolo del sentimento e dell'emozione maggiormente associati a ogni conversazione
grouped = df.groupby('ID').agg({
    'Dominant_Sentiment': lambda x: x.value_counts().idxmax(),
    'Dominant_Emotion': lambda x: x.value_counts().idxmax()
}).reset_index()

# Rinomina le colonne prima di inserirle nel nuovo file csv
grouped.columns = ['ID', 'Sentimento', 'Emozione']

# Salva il risultato in un nuovo file CSV
grouped.to_csv("sentimento_emozione_per_ID.csv", index=False)

# Seleziona solo le righe con Emozione positiva o negativa
positive_sentiment = grouped[grouped['Sentimento'].str.contains('POSITIVE', case=False)]
negative_sentiment = grouped[grouped['Sentimento'].str.contains('NEGATIVE', case=False)]

# Raggruppa per Emozione e conta le occorrenze delle emozioni per ogni sentimento
positive_emotion_counts = positive_sentiment['Emozione'].value_counts()
negative_emotion_counts = negative_sentiment['Emozione'].value_counts()

# Trova l'emozione maggiormente collegata al sentimento positivo e negativo
most_common_positive_emotion = positive_emotion_counts.idxmax()
most_common_negative_emotion = negative_emotion_counts.idxmax()

# Stampa l'emozione maggiormente collegate al sentimenti positivo e/o negativo
print("Emozione maggiormente collegata al sentimento positivo:", most_common_positive_emotion)
print("Emozione maggiormente collegata al sentimento negativo:", most_common_negative_emotion)