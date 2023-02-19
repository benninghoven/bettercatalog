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

DEPTCODE = ""
COURSENUM = ""
COURSELETTER = ""
COURSENAME = ""	
COURSEDESCRIPTION = ""
CREDITS = ""
GRADCREDIT = ""
MAJMINREQ = ""		

courses_dict = {}

count = 0

PATH = "../data/manualentery.txt"
file = open(PATH, "r")

for line in file.readlines():
    count += 1
    words = line.split()
    if GetName(words[0]):
        # RESET VARS
        DEPTCODE = ""
        COURSENUM = ""
        COURSELETTER = ""
        COURSENAME = ""	
        CREDITS = ""
        count = 0
        # DEPTCODE
        DEPTCODE = words[0]
        temp = words[1][-1]
        # COURSENUM & COURSELETTER
        if temp.isalpha():
            COURSELETTER = temp
            COURSENUM = words[1][:-1]
        else:
            COURSELETTER = "N/A"
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
        if "quisite" in line:
            listOfClasses = line.split(":")[1]
            print(listOfClasses)

        

courses_dict[f"{DEPTCODE}{COURSENUM}{COURSELETTER}"] = {}
with open("../data/courses.json", "w") as outfile:
    json.dump(courses_dict, outfile)

# TODO - write to the json file every 4 or 3 lines




print("ran")
