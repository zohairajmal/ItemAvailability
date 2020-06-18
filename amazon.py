# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

# Import smtplib (to allow us to email)
import smtplib

from datetime import datetime


from getpass import getpass
# This is a pretty simple script. The script downloads the homepage of VentureBeat, and if it finds some text, emails me.
# If it does not find some text, it waits 60 seconds and downloads the homepage again.

# while this is true (it is true by default),


def my_main_function(password):

    while True:
        url = "https://www.amazon.com/dp/B07GNNXW4Z"
        # set the headers like we are a browser,
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        # download the homepage
        try:
            response = requests.get(url, headers=headers)
        except requests.exceptions.ConnectionError:
                time.sleep(10)
        # parse the downloaded homepage and grab all text, then,
        soup = BeautifulSoup(response.text, "lxml")


        # if the number of times the word "unavailable" occurs on the page is > 0
        if str(soup).find("Currently unavailable.") > 1:
            time.sleep(30)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Unavailable,", "Current Time =", current_time)   
            # continue with the script,
            continue
            
        # but if the word "unavailable" occurs any other number of times,
        else:
            # create an email message with just a subject line,
            msg = 'Subject: Case Available! https://www.amazon.com/dp/B07GNNXW4Z'
            # set the 'from' address,
            fromaddr = 'zohairajmal1@gmail.com'
            # set the 'to' addresses,
            toaddrs  = ['z.ajmal@jacobs-university.de','zohairajmal1@gmail.com', 'A_THIRD_EMAIL_ADDRESS']
            
            # setup the email server,
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            # add my account login name and password,
            server.login("zohairajmal1@gmail.com", password)
            
            # Print the email's contents
            print('From: ' + fromaddr)
            print('To: ' + str(toaddrs))
            print('Message: ' + msg)
            
            # send the email
            server.sendmail(fromaddr, toaddrs, msg)
            # disconnect from the server
            server.quit()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Available,", "Current Time =", current_time) 
            time.sleep(600)
            continue

if __name__=='__main__':
    
    password = getpass()
    try:
        my_main_function(password)
    except:
        my_main_function(password)
