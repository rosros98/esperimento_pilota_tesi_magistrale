from feel_it import EmotionClassifier, SentimentClassifier
import pandas as pd

# Carica il dataset
df = pd.read_excel("database-pulito.xlsx")
print("Ho letto il dataset...")
#print(df.head)

# Inizializza il classificatore di emozioni e sentimenti
emotion_classifier = EmotionClassifier()
sentiment_classifier = SentimentClassifier()
print("Ho inizializzato...")

# Definisci le funzioni per ottenere il sentimento e l'emozione per ogni testo
def get_emotion(conversazione):
    print("Sono dentro emozione")
    return emotion_classifier.predict([conversazione])[0]


def get_sentiment(conversazione):
    print("Sono dentro sentimento")
    return sentiment_classifier.predict([conversazione])[0]


# Aggiungi le colonne 'emotion' e 'sentiment' al DataFrame
df['emotion'] = df['conversazione'].apply(get_emotion)
print("Ci sono?")
df['sentiment'] = df['conversazione'].apply(get_sentiment)

# Salva il nuovo dataset con le colonne aggiunte
df.to_csv('database_etichettato.csv', index=False)
print("Elaborazione completata!")
