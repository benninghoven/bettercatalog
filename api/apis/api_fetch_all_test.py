# YE - THIS IS TO BE USED FOR API BUTTON TESTING FOR DEVON

from init import app
from db import *

from flask import Response
import json

@app.route('/fetchall-test', methods=["GET"])
def fetchAllTest():
    courses = fetchAllCoursesToArray()
    print(courses)

    return Response(json.dumps(courses), status=200, content_type='application/json')