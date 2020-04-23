import pandas
import numpy as np
import datetime
import re

filename = '/Users/louispuyo/depenses-2019/tabula-Relevé_des_dépenses_8810_31-12-19.csv'
tag_m3 = 'M3'
tag_kwh = 'KWH'

advice = ''' use filter function in python to check date or whaterver u want'''


_date = []
_compte = []
_montant = []
_m3 = []
_kwh = []
_tva = []
_libelle = []
_bill_number = []
_cle = []


with open(f'{filename}', 'r') as file:
    content = file.read()
    content = content.replace('_', '')
    content = content.split('\n')

    for line in content:
        line = line.split(',')
        # date scraping
        for date in line:

            if ('Facture' and 'Relevé') in date.split():
                date = date.split()
                print(f'DATE> {date[2]}')
                withoutdt = date
                withoutdt[2] = ''
                print(withoutdt)
                #date = re.search(r'^[0-3][0-9]\/[0-9][0-9]\/[1-3][1-9]')
                #print(f">>> {date}")
        for sub_line in line:
            if sub_line != '':

                sub_line = sub_line.split('-')

                # print(sub_line)
                for conso in sub_line:

                    if tag_kwh in conso.split():
                        print(f'CONSO ELEC>: {conso}')
                        _kwh += conso
                    elif tag_m3 in withoutdt.split():
                        print(f'CONSO EAU>: {conso}')
                        _m3 += conso

                    elif conso == '""':
                        pass
                    elif conso == "''":
                        pass
                    elif conso is float:
                        print(f'+ {conso}')
                        _montant += conso

        for conso in line:
            conso = conso.split(',')

        for row in line:
            row = row.split()
            compte = [l for l in row if l.isdigit()]

            if compte != []:
                count = 0
                count = sum([len(listElem) for listElem in compte])

                if ('/') in compte:
                    _date += compte
                elif count > 3:
                    print(f'TOTAL COMPTE>: {compte}')
                    _compte += compte
                elif count == 2:
                    print(f'TOTAL CLE>: {compte}')
                    _cle += compte
                else:
                    pass
            # print('==> ')


print(_date)
