#! /usr/bin/python
#Goal: Download and format university course schedules
#using beautifulsoup4
from bs4 import BeautifulSoup
#and requests
import requests

#scrape HTML text from target URLs
def getArticles():
    # Fill in your details here to be posted to the login form.
    payload = {
        'inUserName': 'usrnm',
        'inUserPass': 'passwd'
    }   

    # Use 'with' to ensure the session context is closed after use.
    with requests.Session() as s:
        p = s.post('https://paul.uni-paderborn.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=EXTERNALPAGES&ARGUMENTS=-N000000000000001,-N000435,-Awelcome', data=payload)
        # print the html returned or something more intelligent to see if it's a successful login page.

#        print p.text

        # authorised request1.
        r1 = s.get('https://paul.uni-paderborn.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=COURSEDETAILS&ARGUMENTS=-N768007036239507,-N000459,-N361945407733618,-N361015343842044,-N361015343898045,-N0,-N0')
#        print r1.text
        rc1 = r1.content
        soup = BeautifulSoup(rc1, 'html.parser')
        print(soup.prettify())
#call HTML text scraping function
getArticles()

