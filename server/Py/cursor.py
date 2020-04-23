import sys
import mysql.connector as mc
import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host='localhost',
                                     database='LS-PGT-DATA',
                                     user='root',
                                     password='puyolofr85')


def insertVariblesIntoTable(ei, date, account, consumption, bill_number, amount, vta, supplier):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='LS-PGT-DATA',
                                             user='root',
                                             password='puyolofr85')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO Depenses (building_ei ,date, account, consumption, bill_number, amount, vta, supplier)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """

        # mySql_insert_query = "INSERT INTO Depenses (Id, date, consumption, bill_number, amount, vta, supplier)"
        # mySql_insert_query += "VALUES ("
        # mySql_insert_query += date + ", "
        # if consumption is not None:
        #     mySql_insert_query += consumption + ", "
        # else :
        #     mySql_insert_query += "NULL, "
        # if bill_number is not None:
        #     mySql_insert_query += bill_number + ", "
        # else :
        #     mySql_insert_query += "NULL, "
        # mySql_insert_query += amount + ", "
        # mySql_insert_query += vta + ", "
        # if bill_number is not None:
        #     mySql_insert_query += bill_number + ") "
        # else :
        #     mySql_insert_query += "NULL) "
        # print(mySql_insert_query)
        recordTuple = (ei, date, account, consumption,
                       bill_number, amount, vta, supplier)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        #print("Record inserted successfully into Laptop table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            #print("MySQL connection is closed")
