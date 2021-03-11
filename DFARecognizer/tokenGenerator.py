import os
import sys

sys.path.insert(1, os.getcwd() + "\\Lib")

# from dfa import *

accept_chars = ["==", "=", ":", "+", "-", "*", "/", "(", ")", ";", "+=", "-="]


def splitString_v1(s):
    strList = []
    strTemp = ""

    for i in range(len(s)):
        if s[i].isspace():
            if strTemp != "":
                strList.append(strTemp)
            strTemp = ""

        elif s[i] in accept_chars:
            if strTemp != "":
                strList.append(strTemp)

            if s[i] + s[i - 1] in accept_chars:
                strList[-1] = strList[-1] + s[i]
            else:
                strList.append(s[i])

            strTemp = ""

        else:
            if i == len(s) - 1:
                strTemp += s[i]
                strList.append(strTemp)

            strTemp += s[i]

    return strList


def splitString(s):
    s = s.split(" ")
    newS = []
    for word in s:
        if word.find(":") > 0:
            newS.append(word.replace(":", ""))
            newS.append(":")
        else:
            newS.append(word)

    return newS


s = "if shazum: == def:"

print(splitString(s))