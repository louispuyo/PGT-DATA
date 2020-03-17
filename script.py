import os
import pandas
import numpy as np

filename = '/Users/louispuyo/depenses-2019/tabula-Relevé_des_dépenses_8810_31-12-19.csv'

with open(f'{filename}', 'r') as file:
    content = file.read()
    content = content.replace('_', '')
    content = content.split('\n')

    for line in content:
        line = line.split(',')
        print(line)

        for row in line:
            row = row.split('-')

        class elements:

            def __init__(self, date, tva, montant, supplier, compte, bill_number, cle):
                self.date = self.get_date()
                self.tva = self.get_tva()
                self.compte = self.get_compte()
                self.montant = self.get_montant()

            def get_compte():
                content = [content for content in file]
                line = [line for line in content]
                if 'TOTAL' in line:
                    line = line.replace('TOTAL', '')
                    return line

            def get_cle():
                if 'TOTAL CLE' in line:
                    line = line.replace('TOTAL CLE', '')
                    return line

            def get_montant():
                if 'TTC' in line:
                    print(line)
                return line

            def get_ei():
                pass

            def get_date():
                if r'\d/+' in line:
                    return line

            def get_supplier():
                pass

compte = elements.get_compte()
content = [content for content in file]
line = [line for line in content]
for line in content:
    cle_sample = elements.get_cle()
    compte_sample = elements.get_compte()
    get_date = elements.get_date()
    print(cle_sample, compte_sample, get_date)
