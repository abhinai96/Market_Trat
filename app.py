#Importing the necessary Libraries
from flask import Flask, render_template, request

from bs4 import BeautifulSoup
import requests

import re

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/",methods=["POST"])
def getdata():
    name=request.form["name"]
    url = "https://google.com/search?q=" + name          #search the name in  google
    res = requests.get(url).text.strip()
    soup = BeautifulSoup(res, "html.parser") #parsing the results of the google search
    #print(soup.prettify())
    search = soup.find_all("span", class_="BNeawe tAd8D AP7Wnd")
    email_pattern = re.compile("[-A-Za-z0-9._]+@[-a-zA-Z0-9._]+")  #Using regular expressions for extracting the email address
    emails = re.findall(email_pattern, res)
    if len(emails) == 0:
        print("email id is not found")
    else:
        print("emailid:", emails)

    if len(search[1:3]) == 0:
        print(" phone number not found")     #Extracting the phone number from the google search results
    else:
        for i in search[1:3]:
            phone = i.text
            print("phone number", phone)

    if len(search[:1]) == 0:
        print("address not found")
    else:

        for i in search[:1]:
            address = i.text
            print("Address", address)     #Extracting the address of the organisation from the google search results
    c=["email_id:",str(emails),
       "phone:",phone,
       "address:",address]


    return render_template("pass.html",name=c)


if __name__=="__main__":
    app.run(debug=True)
