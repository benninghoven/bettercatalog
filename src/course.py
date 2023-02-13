class Course():
    def __init__(self):
        self.deptcode = ""
        self.coursenum = 123
        self.coursename = ""
        self.courseletter = ""
        self.coursedescription = ""
        self.credits = 1000
        self.gradcredit = True
        self.majminreq = True

    def __str__(self):
        return (f"""{self.deptcode}|{self.coursenum}|{self.courseletter}""")
