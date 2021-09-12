# import library 
# import requests 
from requests import get
# import beautifulsoup 
from bs4 import BeautifulSoup
# import urllib  
import urllib
# import sys to take the input from the user from the command line 
import sys
# import json for making it json form to sent as rest api to the website 
import json

# url of the news channel 
# sample url 'https://edition.cnn.com/travel/article/india-beautiful-places/index.html'
'''
How to use 
----------
type :: 
> python app.py --url--
example :: 
> python app.py https://edition.cnn.com/travel/article/india-beautiful-places/index.html
----------
NOTE : the url must be from cnn website, for scrapping the website.
'''
url = sys.argv[1]
# read the raw form of url 
raw = urllib.request.urlopen(url).read()

# using BeautifulSoup 
soup = BeautifulSoup(raw, "html.parser")

# find the title 
# tit = soup.find("h1", {"class": "Article__title"})
tit = soup.find("h1", {"class": "pg-headline"})
# print the title of the page 
print('------------------------------------------------------------------------')
print("TITLE")
print('------------------------------------------------------------------------')
print(tit.text)
print('------------------------------------------------------------------------')

# break line 
print('\n')

# find the content of the page 
# cont = soup.find_all("div", {"class" : "Article__body"})
# cont = soup.find("div", {"class" : "Article__body"})
cont = soup.find_all("div", {"class" : "zn-body__paragraph"})
# more = soup.find_all("div", {"class" : "zn-body__"})
print('------------------------------------------------------------------------')
print("CONTENT")
print('------------------------------------------------------------------------')
# print the content of the page 
# print(cont.text)
content = ""
for i in cont:
    print(i.text)
    content += i.text + "\n"
    print('\n')
print('------------------------------------------------------------------------')

# making the json to send as api 
result = json.loads(
    json.dumps(
        {
            "title" : tit.text,
            "content" : content
        }
    )
)

'''
testing the json format
-----------------------
print(type(result))
print(result["title"])
print(result["content"])
'''
