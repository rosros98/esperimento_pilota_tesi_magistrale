from feel_it.feel_it_modificato import EmotionClassifier
#from feel_it import EmotionClassifier
import pandas as pd

# Carica il dataset
df = pd.read_csv("df_sentiment.csv")
print("Ho letto il dataset...")

# Inizializza il classificatore di emozioni e sentimenti
emotion_classifier = EmotionClassifier()
print("Ho inizializzato...")

def get_emotion(frase, puntatore):
    print(f"Sono dentro emozione - {puntatore+1}\{len(df)}")
    emotions_with_confidences = emotion_classifier.predict_emotmod([frase])[0]
    return ",\n ".join([f"'{emotion}', ({confidence:.7f})" for emotion, confidence in emotions_with_confidences])

# Definisci le funzioni per ottenere il sentimento e l'emozione per ogni testo
# def get_emotion_dominant(frase):
#     print("Sono dentro emozione")
#     return emotion_classifier.predict([frase])[0]

# Aggiungi le colonne 'emotion' al DataFrame
#df['Dominant_Emotion'] = df['Frase'].apply(get_emotion_dominant)

# Aggiungi le colonne 'emotion' al DataFrame
df['Emotion'] = df.apply(lambda row: get_emotion(row['Frase'], row.name), axis=1)

# Salva il nuovo dataset con le colonne aggiunte
df.to_csv('df_emotion_sentiment_final.csv', index=False)
print("Elaborazione completata!")

