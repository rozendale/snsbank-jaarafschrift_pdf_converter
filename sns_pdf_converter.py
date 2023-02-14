import pypdf, re
import pandas as pd


def pdf_converter(filename):
    pdf_file = pypdf.PdfReader(filename)
    dictionary = []
    transacties = 0
    for page in pdf_file.pages:
        pagina = re.findall(r'(20[0-3][0-9]\d{4})\s?(-?\d*,\d\d)\s?(-?\d*,\d\d)\s?\s?(\d?\d)\s?(\d{4})\s?(\d*)\s(.+)', page.extract_text())
        transacties += len(pagina)
        for line in pagina:
            dictionary += [{
                "datum": line[0],
                "bedrag": line[1].replace(",", "."),
                "vorig_saldo": line[2].replace(",", "."),
                "volg_nr": line[3],
                "code": line[4],
                "tegen_rek": line[5],
                "omschrijving": line[6]
            }]
    print(f"There are {transacties} transactions.")
    return dictionary

# dict2017 = pdf_converter("2171280_2017.pdf")
# dict2018 = pdf_converter("2171280_2018.pdf")
# dict2019 = pdf_converter("2171280_2019.pdf")
# dict2020 = pdf_converter("2171280_2020.pdf")
# dict2021 = pdf_converter("2171280_2021.pdf")
dict2022 = pdf_converter("2171280_2022.pdf")
# dict2023 = pdf_converter("2171280_2023.pdf")
df = pd.DataFrame(dict2022).to_csv('converted_pdf_2022.csv')
df
