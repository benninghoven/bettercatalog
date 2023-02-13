import requests
from bs4 import BeautifulSoup
from course import Course


def GetLetter(input_string):
    letter = ""
    for char in input_string:
        if not(char.isdigit()):
            letter += char
    return letter 

def GetNumber(input_string):
    number = ""
    for char in input_string:
        if char.isdigit():
            number += char
    return number 



url = "https://catalog.fullerton.edu/preview_program.php?catoid=75&poid=35650&returnto=9871"

# Make a request to the website
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the table rows with class 'table_default'
listitems = soup.find_all('li', {'class': 'acalog-course'})

# Loop through each row and extract the class and prerequisites
for listitem in listitems:
    course = Course()
    line = listitem.text
    lines = line.split()
    #print(lines)
    course.deptcode = lines[0]
    course.coursenum = GetNumber(lines[1])
    tempLine1 = line.split("-")
    tempLine2 = line.split("(")
    print(tempLine1)
    print(tempLine2)
    list3 = [item for item in tempLine1 if item in tempLine2]

    print(list3)
    exit()

    course.coursename = "bob"
    course.courseletter = GetLetter(lines[1])

    """
    self.deptcode = ""
    course.coursenum = 123
    course.coursename = ""
    course.courseletter = ""
    course.coursedescription = ""
    course.credits = 1000
    course.gradcredit = True
    course.majminreq = True
    """
    
    print(course)
