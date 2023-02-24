import json
import pprint

with open('./courses.json') as courses:
    data = json.load(courses)

pp = pprint.PrettyPrinter()
pp.pprint(data)