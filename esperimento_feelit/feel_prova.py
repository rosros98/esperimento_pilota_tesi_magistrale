from feel_it import EmotionClassifier, SentimentClassifier
import pandas as pd

# Carica i vari dataset
#df = pd.read_csv("dataset/positivi.csv")
#df = pd.read_csv("dataset/negativi.csv")
df = pd.read_csv("dataset/misto.csv")
print("Ho letto il dataset...")

# Inizializza il classificatore di emozioni e sentimenti
emotion_classifier = EmotionClassifier()
sentiment_classifier = SentimentClassifier()
print("Ho inizializzato...")

# Definisci le funzioni per ottenere il sentimento e l'emozione per ogni testo
def get_emotion(tweet_text):
    print("Sono dentro emozione")
    return emotion_classifier.predict([tweet_text])[0]


def get_sentiment(tweet_text):
    print("Sono dentro sentimento")
    return sentiment_classifier.predict([tweet_text])[0]


# Aggiungi le colonne 'emotion' e 'sentiment' al DataFrame
df['emotion'] = df['tweet_text'].apply(get_emotion)
print("Ci sono?")
df['sentiment'] = df['tweet_text'].apply(get_sentiment)

# Salva il nuovo dataset con le colonne aggiunte
#df.to_csv('positivi_etichettato.csv', index=False)
#df.to_csv('negativi_etichettato.csv', index=False)
df.to_csv('misto_etichettato.csv', index=False)
print("Elaborazione completata!")
