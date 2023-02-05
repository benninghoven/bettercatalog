import requests
from bs4 import BeautifulSoup

# URL of the PetSmart homepage
url = "https://catalog.fullerton.edu/preview_program.php?catoid=75&poid=35650&hl=%22CPSC%22&returnto=search"

def getsoup(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, "html.parser")

soup = getsoup(url)

# find all product links on the page
divs = soup.findAll("div", attrs={"class":"custom_leftpad_20"})

# print the names and URLs of the products
#class="price-sales"

for div in divs:
    for span in div.findAll("span"):
        #print(span.text)
        href = span.find("a")
        if href:
            print(href.attrs["href"])
        

    

