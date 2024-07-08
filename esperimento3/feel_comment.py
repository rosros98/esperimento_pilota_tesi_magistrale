from feel_it import EmotionClassifier, SentimentClassifier
import pandas as pd

# Carica il dataset
df = pd.read_csv("LLM_FD_pulito.csv")
print("Ho letto il dataset...")

# Inizializza il classificatore di emozioni e sentimenti
emotion_classifier = EmotionClassifier()
sentiment_classifier = SentimentClassifier()
print("Ho inizializzato...")

# Definisci le funzioni per ottenere il sentimento e l'emozione per ogni testo
def get_emotion(comment):
    print("Sono dentro emozione")
    return emotion_classifier.predict([comment])[0]


def get_sentiment(comment):
    print("Sono dentro sentimento")
    return sentiment_classifier.predict([comment])[0]


# Aggiungi le colonne 'emotion' e 'sentiment' al DataFrame
df['emotion'] = df['comment'].apply(get_emotion)
print("Ci sono?")
df['sentiment'] = df['comment'].apply(get_sentiment)

# Salva il nuovo dataset con le colonne aggiunte
df.to_csv('LLM_FD_etichettato.csv', index=False)
print("Elaborazione completata!")
