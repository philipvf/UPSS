#! /usr/bin/python
#Goal: Download and format university course schedules
#using beautifulsoup4 and requests
from bs4 import BeautifulSoup
import requests

def scrape1():
    ################
    ##post request##
    ################
    # Fill in your details here to be posted to the login form. 
    login_url = 'https://paul.uni-paderborn.de/scripts/mgrqispi.dll'
    payload = {'logIn_btn' : 'Anmelden' , 'APPNAME' : 'CampusNet' , 'PRGNAME' : 'LOGINCHECK' , 'usrname' : 'philipvf' , 'pass' : '********' , 'ARGUMENTS' : 'clino,usrname,pass,menuno,menu_type,browser,platform' , 'clino' : '000000000000001' , 'menuno' : '000435' , 'menu_type' : 'classic' , 'browser' : '' , 'platform' : '' }

    # Fill in header details from browser in order to no look like robot
    headers = {'Host' : 'paul.uni-paderborn.de', 'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Encoding' : 'gzip, deflate, br', 'Upgrade-Insecure-Requests' : '1', 'Accept-Language' : 'en-US,en;q=0.5' , 'User-Agent' : 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0', 'Referer' : 'https://paul.uni-paderborn.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=EXTERNALPAGES&ARGUMENTS=-N000000000000001,-N000435,-Awelcome', 'Content-Type' : 'application/x-www-form-urlencoded' }

    s = requests.Session()

    p = s.post(login_url, data = payload, allow_redirects = True, headers=headers)

    ##extract url param authentication token##
    encodedheader = p.headers['REFRESH']
    sencodedheader = str(encodedheader)

    split1,split2 = sencodedheader.split("S=")
    #split2 is full authentication token (not always required)

    split3,split4,split5 = split2.split(",")
    #authentication is split into 3 variables for later use (because full token is not always required in url querys)


    ###############
    ##get request##
    ###############
    url1 = 'https://paul.uni-paderborn.de/scripts/mgrqispi.dll?APPNAME=CampusNet&PRGNAME=COURSEDETAILS&ARGUMENTS=' + split3 + ',-N000616,-N0,-N364713350531466,-N364713350554467,-N0,-N0,-N0'
    r = s.get(url1, headers=headers)
#    print r.url
    #to make sure url is correct# print r.url

    ##extract web page contents##
    soup = BeautifulSoup(r.content, 'html.parser')
#    print(soup.get_text())  #prints text from webpage
#    print(soup.prettify())  #prints beautifulsoup parsed html page
    body = soup.find_all(class_="courseListCell numout")
    print body
scrape1()
