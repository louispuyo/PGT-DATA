
import os
import pandas as pd
import tabula
from col_un1 import Main

directory_csv = '/home/snowden/airflow3/src/data/csv'

directory = './data/pdf'


def read_budgets(directory):
    #budgets = []
    '''

    for filename in os.listdir(directory):
        budget_tables = tabula.read_pdf(
            f"{directory}/{filename}",
            multiple_tables=True,
            pages='all'
        )
    '''

    return tabula.convert_into_by_batch(directory, output_format='csv', pages='all')


# read_budgets(directory)

CONTAINER = []

def start(directory_csv):
    for filename in os.listdir(directory_csv):

        Prog = Main(f"{directory_csv}/{filename}")

        script1 = Prog.date
        script6 = Prog.compte
        script3 = Prog.fournisseur
        script8 = Prog.bat_CODE

        script4 = Prog.ammount
        script7 = Prog.ei
        script5 = Prog.tva

        PDF_OBJ = {'Date': script1, 'Libelle': None, 'Fournisseur': script3,
                   'Montant TTC': script4, 'TVA': script5, 'compte': script6, 'ei': script7, 'cle BAT': script8}

        print('--executed--')
        CONTAINER.append(PDF_OBJ)
        
    return PDF_OBJ


start(directory_csv)
print(CONTAINER)