#required packages (use pip): mysql, mysql-connector, mysql-connector-python-rf, mysql-connector-python
import mysql.connector
import sys

#default arguments
numSteps = 1
queryVals = ['CPSC', 131, '']

#CLA[1] = number of steps to preform, CLA[2] is dept code, CLA[3] is course num, CLA[4] is course letter
if len(sys.argv) > 1:
    numSteps = int(sys.argv[1])
if len(sys.argv) > 4:
    queryVals = [sys.argv[2], int(sys.argv[3]), sys.argv[4][:1]]
elif len(sys.argv) > 3:
    queryVals = [sys.argv[2], int(sys.argv[3]), '']

#database connection
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="DBPASSWORD",
    database="COURSECATALOG"
)
cursor = db.cursor()

#functions
def RecursiveSearch(inputlist, currStep):
    #because this is a one function recursive system, the input needs to be a nested list to work correctly
    for e in inputlist:
        if e != []:
            cursor.execute(f'''
            SELECT * FROM COURSEPREREQ AS P
            WHERE P.PREREQDEPT = '{e[0]}' AND P.PREREQNUM = {e[1]} AND P.PREREQCOURSELETTER = '{e[2]}';
            ''')
            #If you are not at the last level
            if currStep < numSteps:
                RecursiveSearch(cursor.fetchall(), currStep+1)
            else:
                #means we are at the last level
                for i in cursor.fetchall():
                    if i != []:
                        print(i[0] + ' ' + str(i[1]) + i[2])

def RecursiveSearchFormattedOutput(input, currStep, printInput=True):
    if printInput:
        print('\t' * (currStep-1) + input[0] + ' ' + str(input[1]) + input[2])
    
    cursor.execute(f'''
    SELECT * FROM COURSEPREREQ AS P
    WHERE P.PREREQDEPT = '{input[0]}' AND P.PREREQNUM = {input[1]} AND P.PREREQCOURSELETTER = '{input[2]}';
        ''')
    result = cursor.fetchall()

    for i in result:
        if i != []:
            print('\t' * currStep + i[0] + ' ' + str(i[1]) + i[2])
            if currStep < numSteps:
                RecursiveSearchFormattedOutput(i, currStep+1, False)
            

print('if everything is working correctly, the results from r1 should be the same as the most indented rows in r2\nr1:')
#just get (arg1) layer of classes:
RecursiveSearch((queryVals, []), 1)
#because this /\ is a one function recursive system, the input needs to be a nested list to work correctly

print('\n\nr2:')

#get all classes up to (arg1) layers abovein a formatted, indented print
RecursiveSearchFormattedOutput(queryVals, 1)



#tidying up
cursor.close()
db.close()