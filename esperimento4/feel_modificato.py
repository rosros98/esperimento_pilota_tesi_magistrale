from feel_it.feel_it_modificato import EmotionClassifier, SentimentClassifier
import pandas as pd

# Carica il dataset
df = pd.read_excel("database-pulito.xlsx")
print("Ho letto il dataset...")

# Inizializza il classificatore di emozioni e sentimenti
emotion_classifier = EmotionClassifier()
sentiment_classifier = SentimentClassifier()
print("Ho inizializzato...")

def get_emotion(conversazione, puntatore):
    print(f"Sono dentro emozione - {puntatore+1}\{len(df)}")
    emotions_with_confidences = emotion_classifier.predict_emotmod([conversazione])[0]
    return ",\n ".join([f"'{emotion}', ({confidence:.7f})" for emotion, confidence in emotions_with_confidences])

def get_sentiment(conversazione, puntatore):
    print(f"Sono dentro sentimento - {puntatore+1}\{len(df)}")
    predictions, confidences = sentiment_classifier.predict_sentmod([conversazione])[0]
    return predictions, confidences


# Aggiungi le colonne 'emotion' e 'sentiment' al DataFrame
df['emotion'] = df.apply(lambda row: get_emotion(row['conversazione'], row.name), axis=1)
print("Ci sono?")
df['sentiment'] = df.apply(lambda row: get_sentiment(row['conversazione'], row.name), axis=1)

# Salva il nuovo dataset con le colonne aggiunte
df.to_csv('database_etichettato_corretto.csv', index=False)
print("Elaborazione completata!")

