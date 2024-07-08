from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd

# questo test viene fatto su un campione di 300 righe rispetto alle 19mila totali
df_etichette_effettive_misto = pd.read_excel("frase_sentiment_emotion_300.xlsx")

df_previsioni_modello_misto = pd.read_excel("annotazione_manuale_300.xlsx")

# Aggiungi "nessuna emozione" come categoria nel DataFrame delle previsioni del modello
df_previsioni_modello_misto['emozione'] = pd.Categorical(df_previsioni_modello_misto['emozione'], categories=['anger', 'joy', 'fear', 'sadness', 'nessuna emozione'])

# Stampa i nomi delle colonne per verificare la presenza di 'sentimento' e 'emozione'
print("Colonne di df_etichette_effettive_misto:", df_etichette_effettive_misto.columns)
print("Colonne di df_previsioni_modello_misto:", df_previsioni_modello_misto.columns)


# Calcolo delle metriche per la sentiment analysis
accuracy_sentiment = accuracy_score(df_etichette_effettive_misto['sentimento'], df_previsioni_modello_misto['sentimento'])
precision_sentiment = precision_score(df_etichette_effettive_misto['sentimento'], df_previsioni_modello_misto['sentimento'], average='weighted')
recall_sentiment = recall_score(df_etichette_effettive_misto['sentimento'], df_previsioni_modello_misto['sentimento'], average='weighted')
f1_sentiment = f1_score(df_etichette_effettive_misto['sentimento'], df_previsioni_modello_misto['sentimento'], average='weighted')

print(f'Sentiment Analysis - Accuracy: {accuracy_sentiment}')
print(f'Sentiment Analysis - Precision: {precision_sentiment}')
print(f'Sentiment Analysis - Recall: {recall_sentiment}')
print(f'Sentiment Analysis - F1-Score: {f1_sentiment}')

# per l'emozione è stata considerata un'etichetta aggiuntiva rispetto al modello utilizzato, per indicare l'assenza di emozione
# Calcolo delle metriche per l'emotion classification
accuracy_emotion = accuracy_score(df_etichette_effettive_misto['emozione'], df_previsioni_modello_misto['emozione'])
precision_emotion = precision_score(df_etichette_effettive_misto['emozione'], df_previsioni_modello_misto['emozione'], average='weighted')
recall_emotion = recall_score(df_etichette_effettive_misto['emozione'], df_previsioni_modello_misto['emozione'], average='weighted')
f1_emotion = f1_score(df_etichette_effettive_misto['emozione'], df_previsioni_modello_misto['emozione'], average='weighted')

print(f'Emotion Classification - Accuracy: {accuracy_emotion}')
print(f'Emotion Classification - Precision: {precision_emotion}')
print(f'Emotion Classification - Recall: {recall_emotion}')
print(f'Emotion Classification - F1-Score: {f1_emotion}')
