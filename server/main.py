from multiprocessing import Pool
from loguru import logger
import sys
from workers import workers_a, workers_b
from Py import SCRIPT, SCRIPT2


consommation = SCRIPT2.consommation
pos_date = SCRIPT2.pos_date
pos_bill = SCRIPT2.pos_bill
amount = SCRIPT2.amount
vta = SCRIPT2.vta
line = SCRIPT2.line

ROW = line(pos_date, consommation,
           pos_bill, amount, vta)

ROOTER = SCRIPT.ROOTER
print(ROW)
worker_a = workers_a.Worker
worker_b = workers_a.Worker
print(ROW.consumption)
print(ROW.bill_number)
print(ROW.date)


''' 
NOTE:

generator -> methode = __next__()
-> row 1
-> row 2
...
'''

if __name__ == "__main__":

    logger.remove()
    logger.add("./log/file.log", enqueue=True)

    worker = workers_a.Worker()
    with Pool(4, initializer=worker_a.set_logger, initargs=(logger, )) as pool:
        resuts = pool.map(worker.work, [ROOTER, ROOTER])

    # with Pool(4, initializer=workers_b.set_logger, initargs=(logger, )) as pool:

     #   results = pool.map(worker_b.work, )

    logger.info("Done")
