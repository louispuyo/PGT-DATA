import csv  # pas utilis encore mais potentiellement plus tard
import numpy as np
import pandas as pd
import sys
# import .
import cursor
import re
import datetime
filename = '/Users/louispuyo/PGT-DATA/data-jupyter/csv-2/Relevé_des_dépenses_8810_31-12-19.csv'
insertVariblesIntoTable = cursor.insertVariblesIntoTable


def ROOTER():

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
        supplier = 'NULL'

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

    regex = r"(\d+)-\d+.csv"

    matches = re.finditer(regex, filename, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        ei = match.group(1)

    List = []

    accounts = []
    tags = ['m3', 'KWH', 'mwh']
    Row = None
    # Pour chaque ligne (sauf la dernière qui est inutile)
    for i in np.arange(0, len(content)-3):

        row = content[i].split(';')
        pos_date = row[0].strip('_')
        pos_comsumption = row[0].strip('_')
        pos_vta = row[2].strip('_')
        pos_amount = row[1].strip('_')
        pos_bill = 1
        pos_supplier = row[4]

        if re.search(r'^\d+\/', pos_date):

            consommation = pos_comsumption

            reg = check_for_consumption(pos_comsumption)
            if reg:
                regexo = re.compile(r'\d+' + reg)
                consommation = regexo.findall(pos_comsumption)
                consommation = consommation[0]
            else:
                consommation = 'NULL'

            if pos_amount == '':
                amount = '0'
            else:
                amount = pos_amount

            if pos_vta == '':
                vta = '0'
            else:
                vta = pos_vta

            if pos_bill == '':
                pos_bill = 'NULL'
            else:
                pos_bill = pos_bill

            Row = line(pos_date, consommation, pos_bill, amount, vta)
            # print(pos_bill)

            accounts.append(Row)

            if 'Relevé' in pos_date:
                supplier = pos_comsumption.replace('Relevé', '')
                accounts[len(accounts)-1].define_supplier(supplier)

            if 'TOTAL  ' in pos_date:
                regexp = re.compile('\d+')
                account = regexp.findall(pos_comsumption)
                account = account[0]

                for elm in accounts:

                    elm.define_account(account)

                List = List + accounts

                accounts = []

    for i in List:

        # c = vars(i)
        # for elem in c:
        #     print(c, c[elem])
        # print(i.account)
        date = i.date.split('/')
        i.date = datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
        i.date = i.date.strftime("%Y-%m-%d")
        print(i.amount)

        insertVariblesIntoTable(
            ei,
            i.date,
            i.account,
            i.consumption,
            i.bill_number,
            i.amount,
            i.vta,
            i.supplier,
        )
    return line


res = ROOTER()
print(res.amount)
