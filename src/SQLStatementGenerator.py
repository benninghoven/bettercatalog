import json

f = open("sql_statements.txt", "w+")

with open('jsoncoursedata.txt', 'r') as json_file:
    data = json.load(json_file)
    
    '''for k, v in data.items():
        print(k)
        for sk, sv in v.items():
            print(sk + ": ")
            print(sv)
'''

    f.write("INSERT INTO COURSE (DEPTCODE, COURSENUM, COURSELETTER, COURSENAME, COURSEDESCRIPTION, CREDITS, GRADCREDIT, MAJMINREQ) VALUES\n")
    for k, v in data.items():
        
        s = """('{DEPTCODE}', {COURSENUM}, '{COURSELETTER}', '{COURSENAME}', '{COURSEDESCRIPTION}', {CREDITS}, {GRADCREDIT}, TRUE),\n""".format(**v)
        f.write(s)
        # **** NOTE: Last line will have a commae when it should not, must edit the file to remove

f.write(';')

f.close()