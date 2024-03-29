#required packages (use pip): mysql, mysql-connector, mysql-connector-python-rf, mysql-connector-python
import mysql.connector
import sys
import json


#database connection
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="MySQLWorkbench",
    database="COURSECATALOG"
)
cursor = db.cursor(prepared=True)

#CLA[1] = number of steps to preform, CLA[2] is dept code, CLA[3] is course num, CLA[4] is course letter
numSteps = int(sys.argv[1]) if len(sys.argv) > 1 else 1     #Note: number less than 1 are function the same as 1 does
queryVals = [sys.argv[2], sys.argv[3], sys.argv[4][:1]] if len(sys.argv) > 4 else ([sys.argv[2], sys.argv[3]] if len(sys.argv) > 3 else ['CPSC', 131])
hasLetter = True if len(sys.argv) > 4 else False
#default run with no CLAs is 1 step and ['CPSC', 131]


#functions

#shows only the last layer of results for a given input
def RecursiveSearch(inputlist, currStep):
    #because this is a one function recursive system, the input needs to be a nested list to work correctly
    for e in inputlist:
        if e != []:
            #need to reassert if there is a course letter every time
            if len(e) > 2 and len(e[2]) != 0:
                hasLetter = True
            else:
                hasLetter = False

            #if a course letter is provided as a CLA. These needed to be split since you cannot pass an empty string using %s to mysql
            if hasLetter:
                #print("SELECT * FROM COURSEPREREQ AS P WHERE P.PREREQDEPT = '%s' AND P.PREREQNUM = %s AND P.PREREQCOURSELETTER = '%s';" % (e[0], e[1], e[2]))
                query = "SELECT * FROM COURSEPREREQ AS P WHERE P.PREREQDEPT = %s AND P.PREREQNUM = %s AND P.PREREQCOURSELETTER = %s;"
                #print(e[0] + ' ' + str(e[1]) + e[2])
                cursor.execute(query, [e[0], e[1], e[2]])
            else:
                #print("SELECT * FROM COURSEPREREQ AS P WHERE P.PREREQDEPT = %s AND P.PREREQNUM = %s AND P.PREREQCOURSELETTER = '';" % (e[0], e[1]))
                query = "SELECT * FROM COURSEPREREQ AS P WHERE P.PREREQDEPT = %s AND P.PREREQNUM = %s AND P.PREREQCOURSELETTER = '';"
                #print(e[0] + ' ' + e[1])
                cursor.execute(query, [e[0], e[1]])
            
            #If you are not yet at the last level, make a recursive call
            if currStep < numSteps:
                #print(cursor.fetchall())
                RecursiveSearch(cursor.fetchall(), currStep+1)
            else:
                #at the last level
                for i in cursor.fetchall():
                    if i != []:
                        print(i[0] + ' ' + str(i[1]) + i[2])

#shows an indented view of the classes 
def RecursiveSearchFormattedOutput(input, currStep=1, FirstRun=True, hasCourseLetter=False):
    
    if FirstRun:
        print(input[0] + ' ' + str(input[1]) + input[2] if len(input) > 2 else input[0] + ' ' + str(input[1]))      #comment out to remove display
        
        #tree set up
        global root
        global currentNode
        root = dict()
        root = {queryVals[0] + ' ' + str(queryVals[1]) + queryVals[2] if len(queryVals) > 2 else\
                queryVals[0] + ' ' + str(queryVals[1]): dict()}
        
        currentNode = root

    
    #hasLetter already calculated in the recursive call
    if hasLetter:
        query = "SELECT * FROM COURSEPREREQ AS P WHERE P.PREREQDEPT = %s AND P.PREREQNUM = %s AND P.PREREQCOURSELETTER = %s;"
        cursor.execute(query, input[:3])
    else:
        query = "SELECT * FROM COURSEPREREQ AS P WHERE P.PREREQDEPT = %s AND P.PREREQNUM = %s AND P.PREREQCOURSELETTER = '';"
        cursor.execute(query, input[:2])
    result = cursor.fetchall()
    
    cNode = currentNode #due to recursive calls you need a way to go back up to last level

    for i in result:
        if i != []:
            currentNode = cNode
            newNode = dict()

            *_, last = iter(currentNode)
            currentNode[last].update({i[0] + ' ' + str(i[1]) + i[2]: dict()})
            #print(root)
            newNode = currentNode[last]#[i[0] + ' ' + str(i[1]) + i[2]]
            currentNode = newNode

            print('\t' * currStep + i[0] + ' ' + str(i[1]) + i[2] if len(i) > 2 else '')    #comment out to remove display
            if currStep < numSteps:
                RecursiveSearchFormattedOutput(i, currStep+1, False, False if len(i) < 3 else True)



print(f"Searching through {numSteps} levels of postrequisites using {queryVals}\n")
#just get (arg1) layer of classes above specified:
RecursiveSearch([queryVals,], 1)
#because this /\ is a one function recursive system, the input needs to be a nested list to work correctly
print('\n\nNow showing the formatted output from the tree:\n')

#get all classes up to (arg1) layers abovein a formatted, indented print

RecursiveSearchFormattedOutput(queryVals, 1, True, hasLetter)

#except:
#    print("CurrnetNode", currentNode)

print(json.dumps(root))
#t.printPOT(t, root)

#print("test json dump to be passed to front-end")
#implement here

#tidying up
cursor.close()
db.close()
