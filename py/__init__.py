import os
from PDF_extract import PDF_extract
import tabula


directory = '/Users/louispuyo/PGT-DATA/data-jupyter/pdf'


def read_budgets(directory):
    #budgets = []
    
    for filename in os.listdir(directory):
        budget_tables = tabula.read_pdf(
            f"{directory}/{filename}",
            multiple_tables=True,
            pages='all'
        )
    
    return tabula.convert_into_by_batch(directory, output_format='csv', pages='all')


read_budgets(directory)
    