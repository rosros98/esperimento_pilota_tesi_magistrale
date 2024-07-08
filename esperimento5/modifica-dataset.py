import pandas as pd

# Carica il dataset
dataset = pd.read_csv("training.csv")

# Definisci una funzione per sostituire i valori nella colonna "label"
def sostituisci_label(valore):
    if valore == 0:
        return "sadness"
    elif valore == 1:
        return "joy"
    elif valore == 2:
        return "love"
    elif valore == 3:
        return "anger"
    elif valore == 4:
        return "fear"
    elif valore == 5:
        return "surprise"
    else:
        return valore

# Applica la funzione alla colonna "label" del dataset
dataset["label"] = dataset["label"].apply(sostituisci_label)

#rimozione della colonna "Label" per applicare il modello per l'emotion classification
dataset = dataset.drop(dataset.columns[1], axis=1)

# Salva il nuovo dataset modificato
dataset.to_csv("dataset2.csv", index=False)
