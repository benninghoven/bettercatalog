from init import app

from flask import Response

@app.route('/test', methods=['GET'])
def testroute():
    return Response('test request successfull', status=200, content_type='text/plain')