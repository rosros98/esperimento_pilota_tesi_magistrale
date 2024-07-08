from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
import pandas as pd

# Carica i file CSV
df_etichette_effettive_positivi = pd.read_csv("positivi_sentiment.csv")
df_etichette_effettive_negativi = pd.read_csv("negativi_sentiment.csv")
df_etichette_effettive_misto = pd.read_csv("risultati/misto_sentiment.csv")

#Effettuo previsione per quelle positive
df_previsioni_modello_positivi = pd.read_csv("positivi_etichettato.csv")

#Effettuo previsione per quelle negative
df_previsioni_modello_negativi = pd.read_csv("negativi_etichettato.csv")

#Effettuo previsione per quelle miste
df_previsioni_modello_misto = pd.read_csv("risultati/misto_etichettato.csv")

# Calcola la precisione
precision = precision_score(df_etichette_effettive_positivi['sentiment'], df_previsioni_modello_positivi['sentiment'], pos_label='positive')
precision = precision_score(df_etichette_effettive_negativi['sentiment'], df_previsioni_modello_negativi['sentiment'], pos_label='negative')
#"average" calcolerà la precisione per ciascuna classe separatamente e restituirà la media aritmetica non ponderata delle precisioni per tutte le classi.
precision = precision_score(df_etichette_effettive_misto['sentiment'], df_previsioni_modello_misto['sentiment'], average='macro')

# Calcola il richiamo
recall = recall_score(df_etichette_effettive_positivi['sentiment'], df_previsioni_modello_positivi['sentiment'], pos_label='positive')
recall = recall_score(df_etichette_effettive_negativi['sentiment'], df_previsioni_modello_negativi['sentiment'], pos_label='negative')
recall = recall_score(df_etichette_effettive_misto['sentiment'], df_previsioni_modello_misto['sentiment'], average='macro')

# Calcola il punteggio F1
f1 = f1_score(df_etichette_effettive_positivi['sentiment'], df_previsioni_modello_positivi['sentiment'], pos_label='positive')
f1 = f1_score(df_etichette_effettive_negativi['sentiment'], df_previsioni_modello_negativi['sentiment'], pos_label='negative')
f1 = f1_score(df_etichette_effettive_misto['sentiment'], df_previsioni_modello_misto['sentiment'], average='macro')

# Calcola l'accuratezza
accuracy = accuracy_score(df_etichette_effettive_positivi['sentiment'], df_previsioni_modello_positivi['sentiment'])
accuracy = accuracy_score(df_etichette_effettive_negativi['sentiment'], df_previsioni_modello_negativi['sentiment'])
accuracy = accuracy_score(df_etichette_effettive_misto['sentiment'], df_previsioni_modello_misto['sentiment'])

# Stampa i risultati
print(f'Precisione: {precision}')
print(f'Richiamo: {recall}')
print(f'Punteggio F1: {f1}')
print(f'Accuratezza: {accuracy}')
