import pandas as pd
#Processo atto ad effettuare una pulizia del file csv ogirinale

#Effettuo lettura del dataset originale sfruttando pandas
with open('aborto.csv', 'r', encoding='ISO-8859-1') as file:
     dataset = pd.read_csv(file, nrows=4000)

# Elimina le colonne specificate
colonne_da_eliminare = ["author_id", "author_name", "author_username", "created_at", "id", "public_metrics", "withheld_x",
                        "withheld_y", "retweet_count", "like_count"]
dataset = dataset.drop(columns=colonne_da_eliminare)
dataset = dataset.drop(dataset.columns[0], axis=1)

#Salva il dataset modificato in un altro file csv
mix = dataset.to_csv('aborto_pulito.csv', index=False)
