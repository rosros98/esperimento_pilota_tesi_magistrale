from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
import pandas as pd

# Carica il file CSV originale
df_originale = pd.read_csv("nuovo_dataset.csv")

#Effettuo previsione
df_previsioni = pd.read_csv("dataset_etichettato.csv")

# Calcola la precisione
#"average" calcolerà la precisione per ciascuna classe separatamente e restituirà la media aritmetica non ponderata delle precisioni per tutte le classi.
precision = precision_score(df_originale['label'], df_previsioni['label'], average='macro', zero_division=1)

# Calcola il richiamo
recall = recall_score(df_originale['label'], df_previsioni['label'], average='macro', zero_division=1)

# Calcola il punteggio F1
f1 = f1_score(df_originale['label'], df_previsioni['label'], average='macro')

# Calcola l'accuratezza
accuracy = accuracy_score(df_originale['label'], df_previsioni['label'])

# Stampa i risultati
print(f'Precisione: {precision}')
print(f'Richiamo: {recall}')
print(f'Punteggio F1: {f1}')
print(f'Accuratezza: {accuracy}')
