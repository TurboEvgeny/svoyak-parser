#! /use/bin/env/python
# -*- coding: utf-8 -*-
import sys
import requests

if (len(sys.argv) < 2):
    print("не введен адрес страницы")
    exit()
url = sys.argv[1]
r = requests.get(url)
print (r.text)
