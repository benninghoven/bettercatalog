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
    db = connectDB()
    cursor = getDBCursor(db)
    query = "SELECT PREREQDEPT, PREREQNUM, PREREQCOURSELETTER FROM COURSEPREREQ AS PR WHERE PR.COURSEDEPT=%s AND PR.COURSENUM LIKE %s AND PR.COURSELETTER LIKE %s;"
    print(query, (course_dept, course_num, course_letter))
    cursor.execute(query, (course_dept, course_num, course_letter))
    data = cursor.fetchall()
    closeDB(db)
    print(data)

    if len(data) == 0 or not data: return False

    # append the prereq level to the prereq courses data
    # fetchall() returns an IMMUTABLE tuple, therefore, we have to use this workaround to append
    courses = []
    for course in data:
        prereq_course = []
        prereq_course.extend(course)
        prereq_course.append(prereq_level)
        courses.append(prereq_course)

    return courses

def checkDuplicatesAndRemove(course_list_1, course_list_2):
    _course_list_1 = course_list_1
    _course_list_2 = course_list_2

    for i1, course1 in enumerate(course_list_1):
        for i2, course2 in enumerate(course_list_2):
            if course1[0] == course2[0] and \
               course1[1] == course2[1] and \
               course1[2] == course2[2]:
                if course1[3] <= course2[3]:
                    _course_list_1.remove(course1)
                else:
                    _course_list_2.remove(course2)

    return [_course_list_1, _course_list_2]

def fetchCoursePrereqRecursive(course_dept, course_num, course_letter):
    """
    :params: course_dept_code: string
    :params: course_num: int
    :params: course_letter: string

    :returns: list of courses
    """
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

    while prereq_flag:
        # increment prereq_leve
        prereq_level+=1
        prereq_courses_all = list()

        # for each prerequisite course of the previous prerequisite course
        for prereq_course in next_prereq_courses:
    
            # list destructuring to get course attibutes
            prereq_course_dept, prereq_course_num, prereq_course_letter, _prereq_level = prereq_course

            # fetch the preceding prerequisites of the prerequisite of the prior call - if none, go next
            next_prereq_courses = fetchCoursePrereq(prereq_course_dept, prereq_course_num, prereq_course_letter, prereq_level)
            if not next_prereq_courses or next_prereq_courses == False: continue
            else:
                # check if the prereq courses already exists and if it exists remove the duplicates.
                prereq_courses_all, next_prereq_courses = checkDuplicatesAndRemove(prereq_courses_all, next_prereq_courses)

                # append 
                prereq_courses_all.extend(next_prereq_courses)

        if len(prereq_courses_all) == 0: prereq_flag = False
        prereqs.extend(prereq_courses_all)

    # prereqs = coursePrereqToArrayOfDict(prereqs)

    return prereqs