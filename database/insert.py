import json
import mysql.connector
import datetime

from db_config import *

# Open a connection to the database
connection = mysql.connector.connect(
    host=DB_SERVER,
    port=DB_PORT,
    user=DB_USERNAME,
    password=DB_PASSWORD,
    database=DB_DATABASE
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Load data from courses_test.json -> subset of courses.json
with open(COURSES_JSON) as courses:
    course_data = json.load(courses)

for course, course_info in course_data.items():
    dept_code = course_info["DEPTCODE"]
    course_num = course_info['COURSENUM']
    course_letter = course_info['COURSELETTER']
    course_name = course_info['COURSENAME']
    course_description = course_info['COURSEDESCRIPTION']
    credits = course_info['CREDITS']
    grad_credits = 0 if course_info['GRADCREDIT'] == "False" else 1
    maj_min_req = ','.join(list(course_info['MAJMINREQ']))

    try:
        # Execute the INSERT statement
        query = "INSERT INTO COURSE (DEPTCODE, COURSENUM, COURSELETTER, COURSENAME, COURSEDESCRIPTION, CREDITS, GRADCREDIT, MAJMINREQ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        data = (dept_code, course_num, course_letter, course_name, course_description, credits, grad_credits, maj_min_req)
        cursor.execute(query, data)
    except Exception as e:
        with open(DATABASE_ERROR_LOG, 'a') as f:
            log_time = datetime.datetime.now()
            f.write(str(log_time) + ': ' +  str(e) + '\n')
            exit()

# Commit the changes and close the connection
connection.commit()
connection.close()