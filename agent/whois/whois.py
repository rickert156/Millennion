import requests, os
from bs4 import BeautifulSoup
from agent.generateAgent import head

REPORT = 'WHOIS_REPORT'

def createReportDir():
    if not os.path.exists(REPORT):os.makedirs(REPORT)

def whois(domain):
    createReportDir()
    params = {'domain':{domain}}
    site = 'https://whois.ru/'
    response = requests.get(site, params=params, headers=head())
    if response.status_code == 200:
        response = response.text
        bs = BeautifulSoup(response, 'lxml')
        try:
            for information in bs.find_all(class_='raw-domain-info-pre'):
                print(information.get_text())
            print('\n')
        except Exception as ex:
            print(f'Error: {ex}')
