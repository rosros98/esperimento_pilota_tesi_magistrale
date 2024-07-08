import pandas as pd
#Processo atto ad effettuare una pulizia del file csv ogirinale

#Effettuo lettura del dataset originale sfruttando pandas
with open('LLM_DF.csv', 'r', encoding='ISO-8859-1') as file:
     dataset = pd.read_csv(file, nrows=4000)

# Elimina le colonne specificate
colonne_da_eliminare = ["title", "date", "name", "stars"]
dataset = dataset.drop(columns=colonne_da_eliminare)
dataset = dataset.drop(dataset.columns[0], axis=1)

#Salva il dataset modificato in un altro file csv
mix = dataset.to_csv('LLM_FD_pulito.csv', index=False)
