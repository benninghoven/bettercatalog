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
    closeDB(db)

    # parse execute result and disconnect from db
    data_dict = coursesToArrayOfDict(data)

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
    closeDB(db)

    # parse execute result and disconnect from db
    data_dict = coursesToArray(data)

    return data_dict

def fetchCoursePrereq(course_dept, course_num, course_letter, prereq_level):
    print()
    db = connectDB()
    cursor = getDBCursor(db)
    query = "SELECT PREREQDEPT, PREREQNUM, PREREQCOURSELETTER FROM COURSEPREREQ AS PR WHERE PR.COURSEDEPT=%s AND PR.COURSENUM LIKE %s AND PR.COURSELETTER LIKE %s;"
    print("query: " + query, (course_dept, course_num, course_letter))
    cursor.execute(query, (course_dept, course_num, course_letter))
    data = cursor.fetchall()
    print("query result: ", data)
    closeDB(db)

    if len(data) == 0 or not data: return False

    # append the prereq level to the prereq courses data
    # fetchall() returns an IMMUTABLE tuple, therefore, we have to use this workaround to append
    courses = []
    for course in data:
        prereq_course = []
        prereq_course.extend(course)
        prereq_course.append(prereq_level)
        courses.append(prereq_course)

    print()
    return courses

def checkDuplicatesAndRemove(course_list_1, course_list_2):
    _course_list_1 = course_list_1
    _course_list_2 = course_list_2

    for course1 in course_list_1:
        for course2 in course_list_2:
            if course1[0] == course2[0] and \
               course1[1] == course2[1] and \
               course1[2] == course2[2]:
                if course1[3] > course2[3]:
                    _course_list_2.remove(course2)
                elif course1[3] < course2[3]:
                    _course_list_1.remove(course1)

    return [_course_list_1, _course_list_2]

def fetchCoursePrereqRecursive(course_dept, course_num, course_letter):
    """
    :params: course_dept_code: string
    :params: course_num: int
    :params: course_letter: string

    :returns: list of courses
    """
    print()
    # list of courses - result to be returned
    prereqs = list()

    # level of the prereq - the lower the number, the more immediate the prereq is
    # for example, if the level is 0, then that course is an immediate prereq to the course provided
    prereq_level = 0
    
    # flag to monitor if there are any further prereqs
    prereq_flag = True

    # first query to get immediate prerequisites - if none, return False
    next_prereq_courses = fetchCoursePrereq(course_dept, course_num, course_letter, prereq_level)
    if not next_prereq_courses or next_prereq_courses == False: return False

    # append immediate prerequisites to result prereq list
    prereqs.extend(next_prereq_courses)

    # while prereq_flag:

        # prereq_courses_all: all prereq courses of the current list of prereqs being evaluated
    prereq_courses_all = list()

    # for each prerequisite course of the previous prerequisite course
    for prereq_course in prereqs:
        # increment prereq_level
        prereq_level+=1

        # list destructuring to get course attibutes
        prereq_course_dept, prereq_course_num, prereq_course_letter, *rest = prereq_course

        # fetch the preceding prerequisites of the prerequisite of current list of prereqs
        next_prereq_courses = fetchCoursePrereq(prereq_course_dept, prereq_course_num, prereq_course_letter, prereq_level)

        # if next set of prereq courses is empty, continue
        if next_prereq_courses == False:
            prereq_level -= 1
            continue
        # else
        else:
            # check for duplicates in prereqs
            prereqs, next_prereq_courses = checkDuplicatesAndRemove(prereqs, next_prereq_courses)

            print("current courses: ", prereqs)
            print("appending: ", next_prereq_courses)
            # append 
            # prereq_courses_all.extend(next_prereq_courses)

        # if len(prereq_courses_all) == 0:
        #     prereq_flag = False
            prereqs.extend(next_prereq_courses)

    prereqs = coursePrereqToArrayOfDict(prereqs)
    return prereqs