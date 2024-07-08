import pandas as pd

# Leggi il file CSV originale
df = pd.read_excel("dataset-nuovo.xlsx")

# Crea un nuovo DataFrame vuoto
new_df = pd.DataFrame(columns=['ID', 'Interlocutore', 'Frase'])

# Itera su ogni riga del DataFrame originale
for index, row in df.iterrows():
    print(f"Elaborazione della riga {index + 1}...")
    # Verifica che il valore nella cella sia di tipo stringa
    if isinstance(row[0], str):
        # Divide la cella della conversazione in righe separate
        conversation = row[0].split('\n')

        # Inizializza il nome dell'interlocutore
        interlocutor = None

        # Itera su ogni riga della conversazione
        for conv_row in conversation:
            # Verifica se la riga contiene il separatore " - "
            if ' - ' in conv_row:
                # Estrazione del nome dell'interlocutore e della frase
                name, phrase = conv_row.split(' - ', 1)
                # Se il nome dell'interlocutore è diverso da quello precedente, aggiorna l'interlocutore
                if name != interlocutor:
                    interlocutor = name
                # Aggiungi la riga al nuovo DataFrame con un ID univoco che identifica la conversazione per intero precedente
                new_df = new_df.append({'ID': index, 'Interlocutore': interlocutor, 'Frase': phrase}, ignore_index=True)

# Rimuovi le righe in cui la cella "Interlocutore" è vuota oppure ...
new_df = new_df[new_df['Interlocutore'] != '']
new_df = new_df[new_df['Interlocutore'] != ' ']
new_df = new_df[new_df['Interlocutore'] != 'Ore']
new_df = new_df[new_df['Interlocutore'] != '  ']

# Rimuovi le righe in cui la cella "Frase" è vuota oppure ...
new_df = new_df[new_df['Frase'] != '']
new_df = new_df[new_df['Frase'] != '  ']

# Normalizza i valori della colonna 'Frase' in minuscolo
new_df['Frase'] = new_df['Frase'].str.lower()

# Espressione regolare per individuare le righe in cui la cella "Frase" contiene solo una parola
# o una parola seguita da valori di punteggiatura o spazi
pattern = r'^\s*\b\w+\b[\s\.,;:!?]*$'

# Rimuovi le righe corrispondenti al pattern definito sopra
new_df = new_df[~new_df['Frase'].str.match(pattern)]

# Rimuovi le righe in cui la cella "Interlocutore" contiene una sola parola
new_df = new_df[new_df['Interlocutore'].str.split().apply(len) == 1]

# Salva il nuovo DataFrame in un nuovo file CSV
new_df.to_csv('df_completo.csv', index=False)
