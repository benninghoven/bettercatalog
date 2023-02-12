import requests
from bs4 import BeautifulSoup

url = "https://catalog.fullerton.edu/preview_program.php?catoid=75&poid=35650&returnto=9871"

# Make a request to the website
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the table rows with class 'table_default'
listitems = soup.find_all('li', {'class': 'acalog-course'})

# Loop through each row and extract the class and prerequisites
for listitem in listitems:
    line = listitem.text
    courseID = line.split('-')[0]
    courseName = ""
    courseCredits = ""

    print(f"ID {courseID}\nName {courseName}\nCredits {courseCredits}")
