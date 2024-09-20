#!/usr/bin/python3
#Генерирование User Agent

import requests
from bs4 import BeautifulSoup
from utils.generate import head

def ParseResult(response):
    bs = BeautifulSoup(response, 'lxml')
    resultParse = bs.find(['h1']).get_text()
    print(resultParse)
    #print(bs.body.get_text())

def InitRequest():
    site = 'https://n5m.ru/usagent.html'
    response = requests.get(site, headers=head())
    response = response.text
    ParseResult(response)

InitRequest()
