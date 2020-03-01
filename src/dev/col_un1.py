

import dask.dataframe as dd
import pandas as pd
import re
import numpy as np


class Main(object):
    def __init__(self, data):
        self.data = pd.read_csv(
            data, header=None, error_bad_lines=False)
        self.date = self.ext_date()
        self.ei = self.ext_ei()
        self.compte = self.ext_compte()
        self.fournisseur = self.ext_fournisseur()
        self.ammount = self.ext_montant()
        self.rel_ammount = self.cr_remove()
        self.tva = self.ext_tva()
        self.bat_CODE = self.bat_code()

    def ext_date(self):

        dfDate = self.data[0].str.extract(
            r'(\d+/\d+/\d+)')

        dfDate.fillna('null')
        return np.asarray(dfDate)

    def ext_compte(self):

        dfCompte = self.data[1].str.extract(
            r'(\d\d\d\d\d\d\d\)')
        return np.asarray(dfCompte)

    def ext_ei(self):
        s = self.data[1]
        s = s.loc[s.str.startswith('Copro', na=False)]
        s = s.str.extract('(\d\d\d\d)')
        return np.asarray(s)

    def ext_fournisseur(self):
        s = self.data[1]
        s = s.loc[s.str.startswith('Four:', na=False)]

        return np.asarray([s])

    def ext_montant(self):
        df_ammount = self.data[3]
        df_ammount.str.extract(r'(\d+)')
        return [np.asarray(df_ammount)]

    def cr_remove(self):
        Fct = []
        df = self.data[3]
        df = df.loc[df.str.endswith('CR', na=False)]
        for i, nf in enumerate(df):
            if nf.endswith('CR'):
                index = (len(nf)-2)
                nf = nf[:index]
                # print('-'+nf)
                Fct.append('-'+nf)

            elif nf.startswith(('Montant', 'N° Fact')):
                pass
            else:
                Fct.append(nf)
        return np.asarray(Fct)

    def ext_tva(self):
        df = self.data
        TVA = df[6]
        TVA.drop(df[df[6] == 'T.V.A.'].index, inplace=True)
        return np.asarray(TVA)
    
    def bat_code(self):
        s = self.data[1]
        s = s.loc[s.str.startswith('Total cl', na=False)]
        s = s.str.extract('(\d\d\d\d)')
        return np.asarray(s)

