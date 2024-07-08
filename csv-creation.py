# import os
# import csv
#
# Qui ci sono le prove riguardanti il file convertito in csv e pdf
#
# def estrai_conversazioni(testo_csv, parole_chiave):
#     conversazioni = []
#     conversazione_attuale = []
#     in_conversazione = False
#
#     for riga in testo_csv:
#         riga = riga.strip()
#         if any(parola_chiave.lower() in riga.lower() for parola_chiave in parole_chiave):
#             in_conversazione = True
#             conversazione_attuale.append(riga)
#         elif in_conversazione and not riga:
#             in_conversazione = False
#             conversazioni.append(['\n'.join(conversazione_attuale)])
#             conversazione_attuale = []
#         elif in_conversazione:
#             conversazione_attuale.append(riga)
#
#     # aggiungi l'ultima conversazione se presente
#     if conversazione_attuale:
#         conversazioni.append(['\n'.join(conversazione_attuale)])
#
#     return conversazioni
#
# def main():
#     nome_file_csv = 'richiesta-cautelare-clan-cava.csv'
#     parole_chiave = ["colloquio", "intercettazione ambientale", "conversazione n",
#                      "conversazione ambientale", "ore", "leggenda", "tel n",
#                      "tel.", "decreto n", "omissis"]
#
#     output_directory = 'database'
#     if not os.path.exists(output_directory):
#         os.makedirs(output_directory)
#
#     with open(nome_file_csv, mode='r', newline='', encoding='utf-8') as file_csv:
#         reader = csv.reader(file_csv)
#         testo_csv = [riga[0] for riga in reader]
#
#     conversazioni = estrai_conversazioni(testo_csv, parole_chiave)
#
#     output_file_path = os.path.join(output_directory, 'database.csv')
#     with open(output_file_path, mode='w', newline='', encoding='utf-8') as file_csv:
#         writer = csv.writer(file_csv)
#         for conversazione in conversazioni:
#             writer.writerow(conversazione)
#
# if __name__ == "__main__":
#     main()
#

# import os
# import csv
# import docx
#
# def estrai_conversazioni(testo_doc, parole_chiave):
#     conversazioni = []
#     conversazione_attuale = []
#     in_conversazione = False
#
#     for paragrafo in testo_doc.paragraphs:
#         riga = paragrafo.text.strip()
#         if any(parola_chiave.lower() in riga.lower() for parola_chiave in parole_chiave):
#             in_conversazione = True
#             conversazione_attuale.append(riga)
#         elif in_conversazione and not riga:
#             in_conversazione = False
#             conversazioni.append([' '.join(conversazione_attuale)])
#             conversazione_attuale = []
#         elif in_conversazione:
#             conversazione_attuale.append(riga)
#
#     # Aggiungi l'ultima conversazione se presente
#     if conversazione_attuale:
#         conversazioni.append([' '.join(conversazione_attuale)])
#
#     return conversazioni
#
# def main():
#     nome_file_docx = 'richiesta-cautelare-clan-CAVA.docx'
#     parole_chiave = ["Colloquio", "Intercettazione ambientale", "Conversazione n",
#                      "Conversazione ambientale", "Ore", "Leggenda", "Tel n",
#                      "Tel.", "Decreto n", "omissis"]
#
#     output_directory = 'database'
#     if not os.path.exists(output_directory):
#         os.makedirs(output_directory)
#
#     doc = docx.Document(nome_file_docx)
#
#     conversazioni = estrai_conversazioni(doc, parole_chiave)
#
#     output_file_path = os.path.join(output_directory, 'database.csv')
#     with open(output_file_path, mode='w', newline='', encoding='utf-8') as file_csv:
#         writer = csv.writer(file_csv)
#         for conversazione in conversazioni:
#             writer.writerow(conversazione)
#
# if __name__ == "__main__":
#     main()
