import ezgmail, os
import re
from selenium import webdriver
from os.path import abspath
from inspect import getsourcefile

"""
Understanding of Structure:

email -> GmailThread Object
replies in email -> Gmailthread.messages[]
details of i'th reply -> Gmailthread.messages[i].attribute
    where attribute can be sender, timestamp, subject, body

"""

unreadGmailThreads = ezgmail.unread()
# ezgmail.summary(unreadGmailThreads)
# print(unreadThreads[0].messages[0].body)


def FindLink(string):
    # findall() has been used
    # with valid conditions for urls in string
    # Source: https://www.geeksforgeeks.org/python-check-url-string/#:~:text=To%20find%20the%20URLs%20in,returned%20in%20the%20order%20found.
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    # return [x[0] for x in url]
    return url[0][0]

# for emails in

# print("Urls in email: ", FindLink(unreadThreads[0].messages[0].body))

def confirmationEmailCheck(GmailThread):
    message = "To edit or delete your ad"
    if message in GmailThread.message[0].body:
        GmailThread.markAsRead()

linkAddress = "https://www.google.ca/"

file_path = abspath(getsourcefile(lambda _: None))
file_dir = os.path.normpath(file_path + os.sep + os.pardir)
chromedriver = file_dir + "/chromedriver"
# driver = webdriver.Chrome(chromedriver)
# driver.get(linkAddress)


i = 0
for x in unreadGmailThreads:
    sender = "<robot@craigslist.org>"
    if sender in x.messages[0].sender:
        messageKeyPhrase = "log in and publish"
        if messageKeyPhrase in x.messages[0].body:
            i += 1
            print("--------------Message--------------", i)
            # print(x.messages[0].body)
            emailBody = x.messages[0].body
            linkAddress = FindLink(emailBody)
            print(linkAddress)
            driver = webdriver.Chrome(chromedriver)
            driver.get(linkAddress)


