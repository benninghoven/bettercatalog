import json

def GetName(string):
    counter = 0
    for char in string:
        counter += 1
        if not char.isupper():
            return ""
    if counter != 4:
        return ""
    return string

def CheckCourseNum(string):
    counter = 0
    for char in string:
        counter += 1
        if counter < 4:
            if char.isalpha():
                return ""
        else:
            return string

DEPTCODE = ""
COURSENUM = ""
COURSELETTER = ""
COURSENAME = ""	
COURSEDESCRIPTION = ""
CREDITS = ""
GRADCREDIT = ""
MAJMINREQ = []
tempList = []

courses_dict = {}

count = 0

PATH = "../data/manualentery.txt"
file = open(PATH, "r")

for line in file.readlines():
    count += 1
    words = line.split()
    if GetName(words[0]):
        if DEPTCODE:
            courses_dict[f"{DEPTCODE}{COURSENUM}{COURSELETTER}"] = {
                "DEPTCODE" : DEPTCODE,
                "COURSENUM" : COURSENUM,
                "COURSELETTER" : COURSELETTER,
                "COURSENAME" : COURSENAME,
                "COURSEDESCRIPTION" : COURSEDESCRIPTION,
                "CREDITS" : CREDITS,
                "GRADCREDIT" : GRADCREDIT,
                "MAJMINREQ" : MAJMINREQ
            }
        # RESET VARS
        DEPTCODE = ""
        COURSENUM = ""
        COURSELETTER = ""
        COURSENAME = ""	
        CREDITS = ""
        count = 0
        tempList = []
        MAJMINREQ = []
        # DEPTCODE
        DEPTCODE = words[0]
        temp = words[1][-1]
        # COURSENUM & COURSELETTER
        if temp.isalpha():
            COURSELETTER = temp
            COURSENUM = words[1][:-1]
        else:
            COURSELETTER = ""
            COURSENUM = words[1]
        # COURSENAME 
        listOfNames = words[3:-1]
        for name in listOfNames:
            COURSENAME += name
            COURSENAME += " " 
        COURSENAME = COURSENAME[:-1]
        # CREDITS
        CREDITS = words[-1]
        CREDITS = CREDITS[1:-1]
        if len(CREDITS) > 1:
            x = CREDITS[0]
            y = CREDITS[-1]
            CREDITS = x if int(x) > int(y) else y
    # COURSEDESCRIPTION
    elif count == 1:
        COURSEDESCRIPTION = line
        COURSEDESCRIPTION = COURSEDESCRIPTION[:-1]

    # GRADCREDIT
    else:
        if "400-level" in line:
            GRADCREDIT = "True"
        else:
            GRADCREDIT = "False"
        # PREREQ OR COREREQ FIXME
        if "quisite" in line:
            #print(line)
            listOfClasses = line.split(":")[1]
            listOfClasses = listOfClasses.split()
            combo = 0
            for temp in listOfClasses:
                if GetName(temp):
                    combo += 1
                    tempList.append(temp)
                elif combo == 1:
                    if not temp[-1].isalpha() and not temp[-1].isdigit():
                        temp = temp[:-1]
                    MAJMINREQ.append(f"{tempList[0]}{temp}")
                    tempList = []
                    combo = 0


with open("../data/courses.json", "w") as outfile:
    json.dump(courses_dict, outfile, indent=0)

# TODO - write to the json file every 4 or 3 lines




print("ran")
