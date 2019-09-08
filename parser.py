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
    match = re.search(r"\((.*)\)", question.text)
    if (match):
        value = int(match.group(1).replace(" ", ""))
        print(value)
    else:
        print("no match") 
