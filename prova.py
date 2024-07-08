import docx
import pandas as pd

#Converto il file docx in file csv, sulla quale andare a lavorare e generare il file csv voluto.
def converti_docx_in_csv(nome_file_docx, nome_file_csv):
    doc = docx.Document(nome_file_docx)
    dati = []
    for paragrafo in doc.paragraphs:
        dati.append(paragrafo.text)
    df = pd.DataFrame(dati)
    df.to_csv(nome_file_csv, index=False, header=False)

def elimina_celle(file_csv, riga_iniziale, riga_finale, colonna_iniziale, colonna_finale):
    # Carica il file CSV in un DataFrame
    df = pd.read_csv(file_csv)
    # Elimina le celle nell'intervallo specificato
    df.iloc[riga_iniziale:riga_finale + 1, colonna_iniziale:colonna_finale + 1] = None
    # Salva il DataFrame modificato nel file CSV
    df.to_csv('pulito-richiesta-cautelare-clan-CAVA.csv', index=False)

def main():
    nome_file_docx = 'richiesta-cautelare-clan-CAVA.docx'
    nome_file_csv = 'richiesta-cautelare-clan-CAVA.csv'
    # Converte il file DOCX in CSV
    converti_docx_in_csv(nome_file_docx, nome_file_csv)
    elimina_celle(nome_file_csv, 1, 984, 1, 1)

if __name__ == "__main__":
    main()
