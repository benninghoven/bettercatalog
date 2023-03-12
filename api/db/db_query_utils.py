from db.db_utils import *

def fetchAllCourses():
    db = connectDB()
    cursor = getDBCursor(db)
    cursor.execute("SELECT * FROM COURSE")
    data = cursor.fetchall()
    closeDB(db)
    return data

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