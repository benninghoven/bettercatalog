def fetchAllCoursesParser(courses):
    """
    :params: tuple courses: tuple of courses
    :returns: dictionary of courses
    """
    response_arr = []

    for i, course in enumerate(courses):
        courses_dict = dict()

        courses_dict['DEPTCODE'] = course[0]
        courses_dict['COURSENUM'] = course[1]
        courses_dict['COURSELETTER'] = course[2]
        courses_dict['COURSENAME'] = course[3]
        courses_dict['COURSEDESCRIPTION'] = course[4]
        courses_dict['CREDITS'] = course[5]
        courses_dict['GRADCREDIT'] = course[6]
        courses_dict['MAJMINREQ'] = course[7]

        response_arr.append(courses_dict);

    return response_arr

def coursesToArray(courses):
    response_arr = []

    for course in courses:
        response_arr.append(" ".join([str(course[0]), str(course[1]), " - ", str(course[2])]))

    return response_arr
