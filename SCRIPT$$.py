import csv  # pas utilis encore mais potentiellement plus tard
import numpy as np
import pandas as pd

import re
import sys
filename = '/Users/louispuyo/PGT-DATA/data-jupyter/pdf/1120-2013.csv'


with open(filename, 'r') as f:
    content = f.readlines()
content = [x.strip() for x in content]


def check_for_consumption(elem):
    value = None
    for reg in tags:
        if reg in elem:
            value = reg
    return value


class line(object):
    def __init__(self, date, consumption, bill_number, amount, vta):
        self.date = date
        self.consumption = consumption
        self.bill_number = bill_number
        self.amount = amount
        self.vta = vta

    def define_supplier(self, supplier):
        self.supplier = supplier

    def define_account(self, account):
        self.account = account

    def define_ei(self, ei):
        self.ei = ei


List = []

accounts = []
tags = ['m3', 'KWH', 'mwh']
Row = None
# Pour chaque ligne (sauf la dernière qui est inutile)
for i in np.arange(0, len(content)-3):
    row = content[i].split(';')
    consommation = row[1]

    if re.search(r'^\d+', row[0]):
        reg = check_for_consumption(row[1])
        if reg:
            regexo = re.compile(r'\d+' + reg)
            consommation = regexo.findall(row[1])
            consommation = consommation[0]
        else:
            consommation = None
        Row = line(row[0], consommation, row[2], row[3], row[6])
    elif row[0] == '':
        if 'Four:' in row[1]:
            supplier = row[1].replace('Four:', '')
            Row.define_supplier(supplier)
            accounts.append(Row)

        elif 'Total' in row[1]:
            regexp = re.compile('\d+')
            account = regexp.findall(row[1])
            account = account[0]

            for elm in accounts:
                elm.define_account(account)

            List = List + accounts
            accounts = []


for i in List:
    print(vars(i), '\n')
