import pandas as pd
import torch
from torch import nn
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Carica il tokenizer e il modello
tokenizer = AutoTokenizer.from_pretrained("neuraly/bert-base-italian-cased-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("neuraly/bert-base-italian-cased-sentiment")

# Carica il file csv
df = pd.read_csv("df_completo.csv")

# Funzione per applicare il modello BERT sentiment a ogni conversazione considerando un limite di token
def predict_sentiment(sentence):
    # Limita la lunghezza della frase, in questo caso è stato posto prima a 128, poi 512 e poi 1500
    # Questa lunghezza viene modificata in base al modello (512 valore massimo di parole che un modello BERT può considerare)
    max_length = 150
    sentence = sentence[:max_length]
    input_ids = tokenizer.encode(sentence, add_special_tokens=True, return_tensors="pt", max_length=max_length, truncation=True)
    with torch.no_grad():
        logits = model(input_ids)[0]
    proba = nn.functional.softmax(logits, dim=1)
    return proba.squeeze(0)

# Funzione per estrarre il sentimento dominante
def get_dominant_sentiment(row):
    print(f"Stabilisco sentimento predominante - {row.name}/{len(df)}")
    if isinstance(row['Frase'], str):  # Verifica se la cella è una stringa
        probabilities = predict_sentiment(row['Frase'])
        negative, neutral, positive = probabilities.tolist()
        sentiment_label = max((negative, "NEGATIVE"), (neutral, "NEUTRAL"), (positive, "POSITIVE"))[1]
        return sentiment_label
    else:
        return ""

# Funzione che calcola e restituisce la predizione per ogni sentimento considerato dal modello vicino a ogni conversazione
def get_sentiment(row):
    print(f"Definisco valori per ogni sentimento - {row.name}/{len(df)}")
    if isinstance(row['Frase'], str):  # Verifica se la cella è una stringa
        probabilities = predict_sentiment(row['Frase'])
        negative, neutral, positive = probabilities.tolist()
        return f"Negative: {negative:.7f}%,\nNeutral: {neutral:.7f}%,\nPositive: {positive:.7f}%"
    else:
        return ""

# Aggiunta di una nuova colonna al dataframe per memorizzare le percentuali di predizione per ogni sentimento
df['Sentiment'] = df.apply(get_sentiment, axis=1)

# Aggiunta di una nuova colonna al dataframe per indicare il sentimento dominante
df['Dominant_Sentiment'] = df.apply(get_dominant_sentiment, axis=1)

# Salvataggio del dataframe nel file CSV
df.to_csv("df_sentiment.csv", index=False)
print("Elaborazione completata!")