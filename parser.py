#! /use/bin/env/python
# -*- coding: utf-8 -*-
import sys
import re
import requests
from bs4 import BeautifulSoup

if (len(sys.argv) < 2):
    print("не введен адрес страницы")
    exit()
url = sys.argv[1]
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
tags = soup.find_all("h4")
questionsData = []
for element in tags:
    question = element.find('span', {"class" : "mw-headline"})
    # узнаем тему и количество баллов
    #print(question.text)
    match = re.search(r"\((.*)\)", question.text)
    if (match):
        valueStr = match.group(1)
        theme = re.sub(r"\((.*)\)", "", question.text)
        value = int(valueStr.replace(" ", ""))
        print("%s- %s" % (theme, value))
        print("-question-")
        nextTag = element.next_sibling.next_sibling
        if (nextTag.name == 'p'):
            print(nextTag.get_text())
        #print("-question-")
        #print(nextTag.next_sibling)
        #print("---")
