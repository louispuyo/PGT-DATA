import SCRIPT
import os
import datetime
# import init
# import convertcoma as ConvertComa
import sys
import mysql.connector as mc
import mysql.connector
from mysql.connector import Error


# PATH DIRECTORY
pdf_dir = '/Users/louispuyo/PGT-DATA/data-jupyter/pdf'
csv_dir_temp = '/Users/louispuyo/PGT-DATA/data-jupyter/csv'
csv_final_dir = '/Users/louispuyo/PGT-DATA/data-jupyter/csv-2'


# SCRIPT
# INIT.read_budgets(pdf_dir)  # read_pdf ->() -> csv.sep = ],
# ConvertComa.converter_us()  # read_csv -> () csv sep = ;
SCRIPT.ROOTER()
# Object-Facture


connection = mysql.connector.connect(host='localhost',
                                     database='LS-PGT-DATA',
                                     user='root',
                                     password='puyolofr85')
