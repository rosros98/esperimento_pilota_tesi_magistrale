# import zipfile
# import io
# from xml.etree import ElementTree as ET
#
#
# def extract_text_with_border(docx_file_path):
#     # Open the docx file as a zip file
#     with zipfile.ZipFile(docx_file_path, 'r') as zip_ref:
#         # Extract the 'word/document.xml' file
#         xml_content = zip_ref.read('word/document.xml')
#
#     # Parse the XML content
#     xml_root = ET.fromstring(xml_content)
#
#     # Define the namespace
#     NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
#
#     # Initialize an empty list to store the text blocks with borders
#     bordered_blocks = []
#
#     # Iterate through all paragraph elements
#     for para in xml_root.findall('.//w:p', NS):
#         # Check for the presence of the <w:pPr><w:rPr><w:bdr/></w:rPr></w:pPr> element
#         if para.find('.//w:rPr/w:bdr', NS) is not None:
#             # Extract the text of the paragraph
#             bordered_blocks.append(para.find('.//w:t', NS).text.strip())
#
#     return bordered_blocks
#
# docx_file_path = 'richiesta-cautelare-clan-CAVA.docx'
# bordered_blocks = extract_text_with_border(docx_file_path)
# print(f'Bordered blocks: {bordered_blocks}')

from lxml import etree
import csv


# Funzione per estrarre il testo segnato dai tag dei bordi
def extract_text_with_borders(xml_file):
    # Apri il file XML
    tree = etree.parse(xml_file)
    root = tree.getroot()

    # Namespace
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

    # Inizializza una lista per contenere il testo estratto
    extracted_text = []

    # Trova tutti i paragrafi nel documento
    paragraphs = root.findall('.//w:p', namespaces=ns)

    # Itera attraverso i paragrafi
    for paragraph in paragraphs:
        # Trova i bordi del paragrafo
        borders = paragraph.findall('.//w:pBdr', namespaces=ns)
        if borders:
            # Estrai il testo dal paragrafo
            text = paragraph.findtext('.//w:t', namespaces=ns)
            if text:
                # Aggiungi il testo estratto alla lista
                extracted_text.append(text)

    return extracted_text


# Funzione per scrivere il testo estratto in un file CSV
def write_to_csv(text_list, csv_file):
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        for text in text_list:
            csv_writer.writerow([text])


# Testiamo la funzione
xml_file_path = 'document.xml'
csv_file_path = 'testo.csv'

# Estrai il testo segnato dai tag dei bordi
extracted_text = extract_text_with_borders(xml_file_path)

# Scrivi il testo estratto in un file CSV
write_to_csv(extracted_text, csv_file_path)

print("Estrazione completata!")

