import numpy as np
import pandas as pd

filename = '1034-2016.csv'
with open(filename, 'r') as f:
    content = f.readlines()
content = [x.strip() for x in content]


'''
Ici on enlève les sauts de ligne et on recupère seulement les parties de type :
xx/xx/xx,...
Four : ....
'''
liste = []
for i in range(len(content)):
    if len(content[i].split()) == 0:
        print("")
    else:
        e = []
        if ('Four:' in content[i]) & ('Fourniture' not in content[i]):
            e.append(content[i-1]+content[i])
            liste.append(e)


liste[0][0].split(',')
liste2 = []
liste_date = []
liste_m3 = []
liste_tva = []
liste_valeur = []
liste_fourniseur = []


for i in range(0, 30):
    if('m3' in liste[i][0].split(',')[1]):
        liste_m3.append(liste[i][0].split(',')[1].split()[3])
    elif('kwh' in liste[i][0].split(',')[1]):
        liste_m3.append(liste[i][0].split(
            ',')[1].split()[3])
    elif('mwh' in liste[i][0].split(',')[1]):
        liste_m3.append(liste[i][0].split(
            ',')[1].split()[3])

    else:
        liste_m3.append(np.nan)
    liste_tva.append(liste[i][0].split('\"')[5].replace(',', '.'))
    liste_valeur.append(liste[i][0].split('\"')[3].replace(',', '.'))
    liste_fourniseur.append((liste[i][0].split(',')[8]).replace('Four:', ''))
    liste_date.append(liste[i][0].split()[0].split(',')[0])


liste_fini = []
for i in range(len(liste_date)):
    liste_fini.append([liste_date[i], liste_m3[i], liste_tva[i],
                       liste_valeur[i], liste_fourniseur[i]])

# print(type(liste_m3), type(liste_date[0]), type(
#     liste_tva[0]), type(liste_valeur), type(liste_fourniseur))
# len(liste_date)

data = pd.DataFrame()
data['Date'] = liste_date
data['ei'] = '1034'
data['consomation'] = liste_m3
data['TVA'] = liste_tva
data['Montant'] = liste_valeur
data['Fourniseur'] = liste_fourniseur

print(data)
