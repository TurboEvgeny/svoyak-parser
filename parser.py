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
        maxDepth = 4
        currentSibling = element.next_sibling;
        # для логирования запоминаем все строки на каждой итерации
        logStrings = []
        # ищем текст вопроса
        for i in range (maxDepth):
            nextTag = currentSibling.next_sibling
            logStrings.append(nextTag.get_text())
            if (nextTag.name == 'p'):
                #print(logStrings)
                #print("%s- %s" % (theme, value))
                #print("-question-")
                #print(nextTag.get_text())
                break
            else:
                if (i == (maxDepth - 1)):
                    print("%s- %s" % (theme, value))
                    print("fail")
                    print(logStrings)
                currentSibling = nextTag
        #print("-question-")
        #print(nextTag.next_sibling)
        #print("---")
