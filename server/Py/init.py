import os

import tabula

import pandas as pd


directory = '/Users/louispuyo/PGT-DATA/src/temp'


def read_budgets(directory):
    #budgets = []

    for filename in os.listdir(directory):
        budget_tables = tabula.read_pdf(
            f"{directory}/{filename}",
            multiple_tables=True,
            pages='all'
        )
        print('skk')

    return tabula.convert_into_by_batch('/Users/louispuyo/PGT-DATA/src', output_format='csv', pages='all')


read_budgets(directory)
