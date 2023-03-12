from init import app
from db import *

from flask import Response
import json

@app.route('/fetchall-courses', methods=['GET'])
def fetchAll():
    courses = fetchAllCourses()
    # courses = fetchCoursePrereq("CPSC", "240")
    # print(courses)
    return Response(json.dumps(courses), status=200, content_type='application/json')