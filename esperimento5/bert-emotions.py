from transformers import pipeline
import pandas as pd

# Load the BERT-Emotions-Classifier
classifier = pipeline("text-classification", model="ayoubkirouane/BERT-Emotions-Classifier")

# Carica il dataset
df = pd.read_csv("dataset2.csv")
print("Ho letto il dataset...")

# Perform emotion classification
predicted_labels = []
for index, row in df.iterrows():
    print(f"Elaborazione della riga {index + 1}...")
    text = row['text']
    result = classifier(text)
    predicted_label = result[0]['label']
    predicted_labels.append(predicted_label)

# Aggiungi i risultati come nuova colonna accanto a quella esistente nel DataFrame
df.insert(loc=df.columns.get_loc('text') + 1, column='label', value=predicted_labels)

# Salva il nuovo dataset con le colonne aggiunte
df.to_csv('dataset2_etichettato.csv', index=False)
print("Elaborazione completata!")
