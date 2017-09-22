#! /usr/bin/python
#Goal: Download and format university course schedules
#using beautifulsoup4
from bs4 import BeautifulSoup
#and requests
import requests
from requests.auth import HTTPBasicAuth

#scrape HTML text from target URLs
def getArticles():
    # Fill in your details here to be posted to the login form. 
    #    headers = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0'}

    # Use 'with' to ensure the session context is closed after use.
    with requests.Session() as s:
#        headers = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0'}
        payload = { 'usrname' : 'philipvf' , '****' : '****' , 'APPNAME' : 'CampusNet' , 'PRGNAME': 'LOGINCHECK',}
        # print the html returned or something more intelligent to see if it's a successful login page.
        p = s.post('https://paul.uni-paderborn.de/scripts/mgrqispi.dll' , data = payload, )
#        print p.text
        print p.status_code
        soup = BeautifulSoup(p.text , 'html.parser')
        print(soup.get_text())  #prints text from webpage

#        print p.headers
#        print p.cookies
#        print p.content
#        print p.text
        # authorised request1.
#        r1 = requests.get('https://paul.uni-paderborn.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=EXTERNALPAGES&ARGUMENTS=-N915670715903050,-N000455,-ASemesterverwaltung%20STUD%5Fmain')
#        print r1.text
#        print r1.status_code
#        print r1.headers
#        print r1.cookies
#        rc1 = r1.content
#        soup1 = BeautifulSoup(rc1, 'html.parser')
#        print(soup1.prettify()) #prints beautiful soup formatted html text
#        print(soup1.get_text())  #prints text from webpage


#call HTML text scraping function
getArticles()

