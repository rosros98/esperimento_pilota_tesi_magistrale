import pandas as pd
#Processo atto ad effettuare una pulizia del file csv ogirinale, effettuando innazitutto una separazione
#Verranno creati due dataset uno per le emozioni positive e l'altro per quelle negative

#Effettuo lettura del dataset originale sfruttando pandas
with open('dataset/betsentiment-IT-tweets-sentiment-players.csv', 'r', encoding='ISO-8859-1') as file:
     dataset = pd.read_csv(file)

# Trasforma i valori della colonna "sentiment" in lettere minuscole
dataset['sentiment'] = dataset['sentiment'].str.lower()

# Elimina le colonne specificate
colonne_da_eliminare = ["tweet_date_created", "tweet_id", "language", "sentiment_score", "sentiment"]
dataset = dataset.drop(columns=colonne_da_eliminare)

# Elimina le righe con "neutral" nella colonna "sentiment"
dataset = dataset[(dataset['sentiment'] != 'neutral') & (dataset['sentiment'] != 'mixed')]

#Salva il dataset modificato in un altro file csv
#Dopo la prima esecuzione andata a buon fine, il rigo successivo viene commentato per evitare ulteriori elaborazioni
mix = dataset.to_csv('misto_sentiment.csv', index=False)

#Vengono creati due dataset diversi sulla base di quello ottenuto in precedenza
#Si vogliono avere tre dataset differenti: positivo, negativo, mix
# with open('risultati/misto_sentiment.csv, 'r', encoding='ISO-8859-1') as file:
#      dataset_modificato = pd.read_csv(file)
#
# # Trasforma i valori della colonna "sentiment" in lettere minuscole
# dataset_modificato['sentiment'] = dataset_modificato['sentiment'].str.lower()
#
# # Dividi il dataset in base al valore della colonna "sentiment"
# positivi = dataset_modificato[dataset_modificato['sentiment'] == 'positive']
# negativi = dataset_modificato[dataset_modificato['sentiment'] == 'negative']
#
# # Rimuovi la colonna 'sentiment' dai due dataset
# # positivi = positivi.drop(columns=['sentiment'])
# # negativi = negativi.drop(columns=['sentiment'])
#
# # Salva i due dataset in file CSV separati senza la colonna 'sentiment'
# positivi.to_csv('positivi_sentiment.csv', index=False)
# negativi.to_csv('negativi_sentiment.csv', index=False)

# Visualizza il dataset senza le colonne eliminate
print("Sto elaborando...")


