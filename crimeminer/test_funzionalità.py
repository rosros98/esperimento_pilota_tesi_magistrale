import pandas as pd
from collections import Counter

# Carica i dati della tabella
# Assumendo che la tabella sia denominata 'dataset' e sia già stata caricata
dataset = pd.read_csv("frase_sentiment_emotion.csv")

# Definisci il range di date
start_date = '2004-12-01'
end_date = '2004-12-31'

# Filtra la tabella per il range di date
tabella_filtrata = dataset[(dataset['data_conversazione'] >= start_date) & (dataset['data_conversazione'] <= end_date)]

# Raggruppa i dati per interlocutore e calcola l'emozione maggiormente provata
emozione_maggiormente_provata = tabella_filtrata.groupby('interlocutore')['emozione'].max()

# Crea una colonna con un dizionario che contiene le liste di interlocutori e ID conversazione per ciascun interlocutore
interlocutori_per_interlocutore = tabella_filtrata.groupby('interlocutore').apply(lambda x: {participant: conversation_id for participant, conversation_id in zip(x['lista_interlocutori'], x['numero'])})

# Unisci i risultati in un'unica tabella
tabella_risultato = pd.DataFrame({
    'Interlocutore': emozione_maggiormente_provata.index,
    'Emozione_maggiormente_provata': emozione_maggiormente_provata.values,
    'Interlocutori_conversazioni': interlocutori_per_interlocutore.values
})

# Salva la tabella risultato in un file CSV
tabella_risultato.to_csv('tabella_risultato.csv', index=False)