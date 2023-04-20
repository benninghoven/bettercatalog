from init import app
from db import *

from flask import Response, request
import json

@app.route('/fetchprereqs', methods=['GET'])
def fetchPrereqs():
    req_dept_code = request.args.get("dept_code")
    req_course_num = request.args.get("course_num")
    req_course_letter = str(request.args.get("course_letter"))

    courses = fetchCoursePrereqRecursive(req_dept_code, req_course_num, req_course_letter)

    return Response(json.dumps(courses), status=200, content_type='application/json')