# TODO: LOG ERROR AND WARNINGS TO LOG FILE

from config import *
import logging

import mysql.connector
from mysql.connector import errorcode

def connectDB():
    """
    :returns: db connection
    """
    try:
        db = mysql.connector.connect(**db_config)
        print("connected to db successfully")
        return db
    except mysql.connector.Error as err:
        print("ERROR CONNECTING TO DB")
        print(err.msg)

def getDBCursor(db_cnx):
    """
    :returns: db cursor
    """
    if db_cnx:
        return db_cnx.cursor(prepared=True)
    else:
        print("ERROR GETTING CURSOR")

def getErrorInfo(err_exception, /):
    """
    :param mysql.connector.errors err_exception: db error exception
    :returns: error info
    """
    return {
        'err_code': err_exception.errno,
        'err_msg': err_exception.msg,
        'sql_state': err_exception.sqlstate
    }

def closeDB(db):
    """
    :param mysql.connector.connect db: db connection
    """
    print("closing db")
    db.close()