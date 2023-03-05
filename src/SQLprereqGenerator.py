import json

f = open("sql_prereq_statements.txt", "w+")

with open('jsoncoursedata.txt', 'r') as json_file:
    data = json.load(json_file)

    f.write("INSERT INTO COURSEPREREQ (COURSEDEPT, COURSENUM, COURSELETTER, PREREQDEPT, PREREQNUM, PREREQCOURSELETTER, ISCOREQ) VALUES\n")
    for k, v in data.items():
        for i in v["MAJMINREQ"]:
            iscoreq = False
            if(i[-1] == '$'):
                i = i[:-1]
                iscoreq = True
            if len(i) > 7:  #if there is a course letter
                s = f"""('{v["DEPTCODE"]}', {v["COURSENUM"]}, '{v["COURSELETTER"]}', '{i[:4]}', {i[4:7]}, '{i[7]}', {iscoreq}),\n""".format(**v)    #cannot detect coreqs rn
                f.write(s)
            else:
                s = f"""('{v["DEPTCODE"]}', {v["COURSENUM"]}, '{v["COURSELETTER"]}', '{i[:4]}', {i[4:7]}, '', {iscoreq}),\n"""    #cannot detect coreqs rn
                f.write(s)

        #f.write(s)
        # **** NOTE: Last line will have a commae when it should not, must edit the file to remove

f.write(';')

f.close()