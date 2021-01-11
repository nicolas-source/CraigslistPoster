import ezgmail, os
import re


unreadThreads = ezgmail.unread()
ezgmail.summary(unreadThreads)
# print(unreadThreads[0].messages[0].body)


def FindLink(string):
    # findall() has been used
    # with valid conditions for urls in string
    # Source: https://www.geeksforgeeks.org/python-check-url-string/#:~:text=To%20find%20the%20URLs%20in,returned%20in%20the%20order%20found.
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]


# for emails in

# print("Urls in email: ", FindLink(unreadThreads[0].messages[0].body))


print(unreadThreads)