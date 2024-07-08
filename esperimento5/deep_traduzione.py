import csv
from deep_translator import GoogleTranslator

def translate_text_column(input_file, output_file, block_size=100):
    # Funzione per tradurre il testo della colonna "text"
    def translate_text(text):
        print(f"Traduzione del testo: {text}")
        translated_text = GoogleTranslator(source='en', target='it').translate(text)
        print(f"Testo tradotto: {translated_text}")
        return translated_text

    # Lettura del file CSV originale e seguente memorizzazione delle righe
    input_rows = []
    with open(input_file, 'r', newline='', encoding='utf-8') as csv_in:
        reader = csv.DictReader(csv_in)
        for row in reader:
            input_rows.append(row)

    # Traduzione e concatenazione dei blocchi di righe
    with open(output_file, 'w', newline='', encoding='utf-8') as csv_out:
        writer = csv.DictWriter(csv_out, fieldnames=reader.fieldnames)
        writer.writeheader()

        for start_index in range(0, len(input_rows), block_size):
            end_index = min(start_index + block_size, len(input_rows))
            translated_block = []

            for index, row in enumerate(input_rows[start_index:end_index], start=start_index + 1):
                print(f"Traduzione della riga {index}")
                translated_row = {key: value for key, value in row.items()}
                translated_row['text'] = translate_text(row['text'])
                translated_block.append(translated_row)

            writer.writerows(translated_block)
            print(f"Blocco {start_index // block_size + 1}/{len(input_rows) // block_size + 1} tradotto.")

# Percorsi dei file csv di input e output
input_file_path = 'dataset2_etichettato.csv'
output_file_path = 'dataset2_tradotto.csv'

# Traduzione del testo nella colonna "text" del file CSV e concatenazione di tutti i risultati ottenuti
translate_text_column(input_file_path, output_file_path)
print("Traduzione completata. Il file tradotto è stato salvato come 'dataset2_tradotto.csv'")

