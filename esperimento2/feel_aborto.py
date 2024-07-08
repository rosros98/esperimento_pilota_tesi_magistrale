from feel_it import EmotionClassifier, SentimentClassifier
import pandas as pd

# Carica il dataset
df = pd.read_csv("aborto_pulito.csv")
print("Ho letto il dataset...")

# Inizializza il classificatore di emozioni e sentimenti
emotion_classifier = EmotionClassifier()
sentiment_classifier = SentimentClassifier()
print("Ho inizializzato...")

# Definisci le funzioni per ottenere il sentimento e l'emozione per ogni testo
def get_emotion(text):
    print("Sono dentro emozione")
    return emotion_classifier.predict([text])[0]


def get_sentiment(text):
    print("Sono dentro sentimento")
    return sentiment_classifier.predict([text])[0]


# Aggiungi le colonne 'emotion' e 'sentiment' al DataFrame
df['emotion'] = df['text'].apply(get_emotion)
print("Ci sono?")
df['sentiment'] = df['text'].apply(get_sentiment)

# Salva il nuovo dataset con le colonne aggiunte
df.to_csv('aborto_etichettato.csv', index=False)
print("Elaborazione completata!")
