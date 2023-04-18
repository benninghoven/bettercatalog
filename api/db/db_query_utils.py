from db.db_utils import *
from db.db_parser_utils import *

def fetchAllCourses():
    # connect to DB and get connection cursor
    # TODO: db connection error check
    db = connectDB()
    cursor = getDBCursor(db)
    
    # execute sql and fetch results
    # TODO: db execute error check
    cursor.execute("SELECT DEPTCODE, COURSENUM, COURSELETTER, COURSENAME, COURSEDESCRIPTION, CREDITS, GRADCREDIT, MAJMINREQ FROM COURSE")
    data = cursor.fetchall()

    # parse execute result and disconnect from db
    data_dict = coursesToArrayOfDict(data)
    closeDB(db)

    return data_dict

def fetchAllCoursesToArray():
    # connect to DB and get connection cursor
    # TODO: db connection error check
    db = connectDB()
    cursor = getDBCursor(db)
    
    # execute sql and fetch results
    # TODO: db execute error check
    cursor.execute("SELECT DEPTCODE, COURSENUM, COURSELETTER, COURSENAME FROM COURSE")
    data = cursor.fetchall()

    # parse execute result and disconnect from db
    data_dict = coursesToArray(data)
    closeDB(db)

    return data_dict

def fetchAllPreReqs():
    db = connectDB()
    cursor = getDBCursor(db)
    cursor.execute("SELECT * FROM COURSEPREREQ")
    data = cursor.fetchall()

def fetchCoursePrereq(course_dept, course_num):
    db = connectDB()
    cursor = getDBCursor(db)
    cursor.execute("SELECT CP.PREREQDEPT, CP.PREREQNUM, CP.PREREQCOURSELETTER \
                    FROM COURSE AS C, COURSEPREREQ AS CP \
                    WHERE C.COURSEDEPT = %s AND C.COURSENUM = %s AND C.COURSEDEPT = CP.PREREQDEPT AND C.COURSENUM = CP.PREREQNUM AND C.COURSELETTER = CP.PREREQCOURSELETTER", (course_dept, course_num))