
import csv
from pathlib import Path


folder_in = Path(r'/Users/louispuyo/PGT-DATA/data-jupyter/temp')
folder_out = Path(r'/Users/louispuyo/PGT-DATA/data-jupyter/csv-2')


def converter_us():

    for incsv in folder_in.iterdir():
        outcsv = folder_out.joinpath(incsv.name)
        with open(str(incsv), 'r') as fin, open(str(outcsv), 'w') as fout:
            reader = csv.DictReader(fin)
            writer = csv.DictWriter(fout, reader.fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows(reader)
