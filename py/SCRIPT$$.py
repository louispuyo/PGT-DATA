import csv  # pas utilis encore mais potentiellement plus tard
import numpy as np
import pandas as pd

filename = '/Users/louispuyo/PGT-DATA/data-jupyter/pdf/1120-2012.pdf'
with open(filename, 'r') as f:
    content = f.readlines()
content = [x.strip() for x in content]
Fournisseur = []
Consommation = []
Montant = []
TVA = []
Date = []
# Pour chaque ligne (sauf la dernière qui est inutile)
for i in np.arange(0, len(content)-1):
    try:  # ce try permet d'ignorer les sauts de ligne)
        if content[i].split()[0][2] == '/':  # si troisième caractere est un \ : date

            try:
                if content[i+1].split(sep=',')[1][:5] == 'Four:':
                    try:
                        fournisseur = content[i+1].split(sep=',')[1]
                        Fournisseur.append(
                            fournisseur[5:].strip().replace('Ã©', 'é'))
                    except:
                        Fournisseur.append(np.nan)
                else:
                    Fournisseur.append(np.nan)
            except:
                Fournisseur.append(np.nan)
            try:
                consommation = content[i].split()[3]
                if consommation[-3:-1] == 'm3':
                    Consommation.append(consommation[:-3])
                else:
                    consommation = np.nan
                    Consommation.append(np.nan)
            except:
                Consommation.append(np.nan)
            try:
                montant = content[i].split(sep='"')[1]
                if montant[-2:] == 'CR':
                    montant = montant[:-2]
                Montant.append(montant)
            except:
                Montant.append(np.nan)
            try:
                tva = content[i].split(sep='"')[5]
                TVA.append(tva)
            except:
                TVA.append(np.nan)

            Date.append(content[i].split(sep=',')[0])

        else:
            pass
    except:
        print(content[i], 'ligne', i+1, 'est vide')
        pass
factures = []
factures_numero_compte = []
for i in np.arange(0, len(content)):
    try:
        if content[i].split()[0][2] == '/':
            factures.append(1)
        elif content[i].split(sep=',')[1][:12] == 'Total compte':
            factures_par_numero = [content[i].split(
                sep=',')[1][13:21] if x == 1 else None for x in factures]
            for i in factures_par_numero:
                factures_numero_compte.append(i)
            factures = []

    except:
        pass

data = pd.DataFrame()
data['Date'] = Date
data['Fournisseur'] = Fournisseur
data['Consommation'] = Consommation
data['Montant'] = Montant
data['TVA'] = TVA
data['Compte'] = factures_numero_compte

print(data)
