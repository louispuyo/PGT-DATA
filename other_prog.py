import re


def listToString(s):

    # initialize an empty string
    str1 = " "

    # return string
    return (str1.join(s))


class pdfs:
    def __init__(self):
        self.date = date
        self.fourn = fourn
        self.conso = conso
        self.compte = compte
        self.tva = tva
        self.lib = lib
        self.cle = cle


class pdfobject(pdfs):
    def __init__(self):
        super().__init__()

    def _return_init(self):
        return __init__()


cln_container = []
pdf = open(
    '/Users/louispuyo/depenses-2019/tabula-Relevé_des_dépenses_8810_31-12-19.csv')
with open('/Users/louispuyo/depenses-2019/tabula-Relevé_des_dépenses_8810_31-12-19.csv', 'r') as file:
    for line in iter(file):
        if '_' in line:
            sub = sub
        else:
            sub = line
            line_split = line.split(',')
        for linesplit in (line_split):
            # print(f'+ {linesplit}')
            for linesplit in line_split:
                linesplit = linesplit.replace('-U29R', '-')
                linesplit = str(linesplit).replace('\n', '')
                linesplit = linesplit.replace(',', '')
                linesplit = linesplit.split('-')
                for i in linesplit:
                    # print(f'- {i}')

                    x = re.findall(r'[0.-9.]+', i)
                    x = listToString(x)
                    if '.' in x:
                        print(i.split())
                    if len(x) == 6:
                        print(f'compte> {x}')
                    if len(x) == 2:
                        print(f'cle> {x}')

                # line = str(line).rsplit()
