'''
CPSC 120 - Introduction to Programming (3)
Introduction to the concepts underlying all computer programming: design and execution of programs; sequential nature of programs; use of assignment, control and input/output statements to accomplish desired tasks; design and use of functions. Structured and object-oriented methodologies. (1.5 hours lecture, 3 hours laboratory)
Corequisite: MATH 125.
CPSC 223C - C Programming (3)
Systems programming in the C language, including its syntax and semantics; essential idioms; important parts of the C11 and POSIX C APIs; security issues; and notable extensions libraries.
Prerequisite: CPSC 131.
Undergraduate Course not available for Graduate Credit
CPSC 240 - Computer Organization and Assembly Language (3)
Digital logic and architecture of a computer system, machine level representation of data, memory system organization, structure of low-level computer languages. Machine, assembly, and macro language programming. Principles of assembler operation, input-output programming, interrupt/exception handling. Laboratory programming assignments. (2 hours lecture, 2 hours laboratory)
Prerequisites: CPSC 131; MATH 170A or MATH 280.
Undergraduate Course not available for Graduate Credit
CPSC 335 - Algorithm Engineering (3)
Algorithm design using classical patterns: exhaustive search, divide and conquer, randomization, hashing, reduction, dynamic programming, and the greedy method. Asymptotic and experimental efficiency analysis. NP-completeness and decidability. Implementing algorithms to solve practical problems.
Prerequisites: MATH 170B, CPSC 131; Computer Science or Computer Engineering major or minor; or Computer Science or Computer Engineering graduate standing.
Undergraduate Course not available for Graduate Credit
'''

'''     \/ opt courseletter
TITL NUM - NAME OF CLASS (UNITS)
COURSE DESCRIPTION (all 1 line)
COREQUISITES OR PREREQUISITES, PARSE FOR GIVEN 4 LETTER DEPT CODES, THEN NUM AND LETTER, PARSE FOR "Computer Science major/minor"
GRAD CREDIT AVAILABLE Y/N
'''
class copreReqData():
    
    def __init__(self):
        self.dCode
        self.cNum
        self.cLetter
        self.iscoReq
        self.preDCode
        self.preCNum
        self.preCLetter
    

    def print(self):
        print(self.dCode + " " + self.cNum + " " + self.cLetter + " " + self.iscoReq + " " + self.preDCode + " " + self.preCNum + " " + self.preCLetter)

class courseStruct():
    
    def __init__(self):
        self.dCode
        self.cNum
        self.cLetter
        self.cName
        self.cDesc
        self.credits
        self.gradCred
        self.mmReq
    
    def print(self):
        print(self.dCode +  " " + self.cNum + " " + self.cLetter +  " " + self.cName +  " " + self.cDesc + " " + self.credits +  " " + self.gradCred + " " + self.mmReq)
        
    


courseStructList = list()
coPreReqList = list()


with open(r"C:\Users\Admin\Documents\COLLEGE\Y3\S2\CPSC 362\CPSC_class_data.txt", "rt") as f:
    
    #used every iteration, declared here to reduce reinitialization
    hasLetter = False
    for textline in f:
        # go through one course at a time, not 1 line
        courseStructList.append(courseStruct)   #need to check if this will work

        #checking to see if the line follows the TITL NUM pattern
        if textline[0:4].isalpha() and textline[5:8].isnumeric():
            courseStructList[-1].dCode = textline[0:4]
            print(courseStructList[-1].dCode)
            courseStructList[-1].cNum = int(textline[5:8])
            print(courseStructList[-1].cNum)
            
            if textline[8].isalpha():
                courseStructList[-1].cLetter = textline[8]
                print(courseStructList[-1].cLetter)
                hasLetter = True
            else:
                #SQL recognises '' as empty string and not null, if there are issues with insertion try varchar(1)
                courseStructList[-1].cLetter = ''
                print("No course letter detected: " + textline[8])
                hasLetter = False
            courseStructList[-1].cName = textline[11 + int(hasLetter): textline.find('(')-1]
            print(courseStructList[-1].cName)
            #credit value is always 2 from back
            courseStructList[-1].credits = textline[-3]
            print(courseStructList[-1].credits)
            #All information obtained from current line, going to course description line
            courseStructList[-1].cDesc = f.readline()
            print(courseStructList[-1].cDesc)

            #Looking for prereq and course major/minor
            textline = f.readline()
            print("Prerequisite text line: " + textline)
            

            if 'Corequisite' in textline:
                coPreReqList.append(copreReqData)
                DEPTCODES = [
                    'CPSC', 'MATH', 'AFAM', 'AMST', 'ANTH', 'ARAB', 'ART ', 'ASAM', 'ASTR', 'BIOL', 'CHEM', 'CHIC', 
                    'CHIN', 'COMM', 'CTVA', 'DANC', 'EGGN', 'ENGL', 'FREN', 'GEOG', 'GEOL', 'GRMN', 'HCOM', 'HIST', 
                    'HONR', 'ITAL', 'JAPN', 'KORE', 'LBST', 'LING', 'PERS', 'PERS', 'PHIL', 'PHYS', 'PORT', 'POSC', 
                    'RLST', 'SPAN', 'THTR', 'VIET', 'WGST']
                pInd = 11
                
                while pInd != -1 and pInd < len(textline) - 1:
                    noLeft = True
                    for code in DEPTCODES:
                        if code in textline[pInd:]:
                            print("Found dept code: " + code)
                            noLeft = False
                            pInd += textline[pInd:].find(code)
                            #print(textline[pInd:])
                            #print(pInd)
                            coPreReqList[-1].dCode = courseStructList[-1].dCode
                            coPreReqList[-1].cNum = courseStructList[-1].cNum
                            coPreReqList[-1].cLetter = courseStructList[-1].cLetter
                            coPreReqList[-1].iscoReq = True
                            coPreReqList[-1].preDCode = textline[pInd:pInd+4]
                            pInd += 5
                            print(textline[pInd:pInd+3])
                            coPreReqList[-1].preCNum = int(textline[pInd:pInd+3])
                            pInd += 3   #may want to bounds check here if it becomes an issue, however it shouldn't be an issue because the line should end with a period
                            if textline[pInd].isalpha():
                                coPreReqList[-1].preCLetter = textline[pInd]
                            else:
                                coPreReqList[-1].preCLetter = ''
                            pInd += 2
                            break   #break here because otherwise it will not iterate through the deptcodes already covered
                    if noLeft:
                        break
            elif 'Prerequisites' in textline:
                coPreReqList.append(copreReqData)
                DEPTCODES = [
                    'CPSC', 'MATH', 'AFAM', 'AMST', 'ANTH', 'ARAB', 'ART ', 'ASAM', 'ASTR', 'BIOL', 'CHEM', 'CHIC', 
                    'CHIN', 'COMM', 'CTVA', 'DANC', 'EGGN', 'ENGL', 'FREN', 'GEOG', 'GEOL', 'GRMN', 'HCOM', 'HIST', 
                    'HONR', 'ITAL', 'JAPN', 'KORE', 'LBST', 'LING', 'PERS', 'PERS', 'PHIL', 'PHYS', 'PORT', 'POSC', 
                    'RLST', 'SPAN', 'THTR', 'VIET', 'WGST']
                pInd = 14
                
                while pInd != -1 and pInd < len(textline) - 1:
                    noLeft = True
                    for code in DEPTCODES:
                        if code in textline[pInd:]:
                            noLeft = False
                            pInd = textline[pInd:].find(code)
                            coPreReqList[-1].dCode = courseStructList[-1].dCode
                            coPreReqList[-1].cNum = courseStructList[-1].cNum
                            coPreReqList[-1].cLetter = courseStructList[-1].cLetter
                            coPreReqList[-1].iscoReq = False
                            coPreReqList[-1].preDCode = textline[pInd:pInd+4]
                            pInd += 5
                            coPreReqList[-1].preCNum = int(textline[pInd:pInd+3])
                            pInd += 3   #may want to bounds check here if it becomes an issue, however it shouldn't be an issue because the line should end with a period
                            if textline[pInd].isalpha():
                                coPreReqList[-1].preCLetter = textline[pInd]
                            else:
                                coPreReqList[-1].preCLetter = ''
                            pInd += 2
                            break   #break here because otherwise it will not iterate through the deptcodes already covered
                    if noLeft:
                        break
            else:
                print("Could not parse " + textline + " for pre/coreq")
            
            if "Computer Science or Computer Engineering major or minor" in textline or "Computer Science or Computer Engineering graduate standing" in textline or "Computer Science major" in textline:
                courseStructList[-1].mmReq = True
            else:
                courseStructList[-1].mmReq = False
            
            #now have to peek next line for grad credit availability
            
            currline = f.tell()
            textline = f.readline()
            if "Undergraduate Course available for Graduate Credit" in textline:
                courseStructList[-1].gradCred = True
            elif "Undergraduate Course not available for Graduate Credit" in textline:
                courseStructList[-1].gradCred = False
            else:
                f.seek(currline)    # need to go back one line since there is no mention of grad credit, which means it may have been ommitted (lower level classes) and the line is the start of the next class
                courseStructList[-1].gradCred = False



            #https://stackoverflow.com/questions/3505479/undo-a-file-readline-operation-so-file-pointer-is-back-in-original-state


    f.close()


print("All Course Data:")

for c in courseStructList:
    c.print()

for p in coPreReqList:
    p.print()