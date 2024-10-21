import requests, os, time
from bs4 import BeautifulSoup
from agent.generateAgent import head

DIR_ROBOTS = 'Robots'

def writeRobots(domain, robotsFile):
    if not os.path.exists(DIR_ROBOTS):os.makedirs(DIR_ROBOTS)
    if 'http://' in domain or 'https://' in domain:
        domain = domain.split('://')[1]
        if '/' in domain:domain = domain.split('/')[0]
    date = time.strftime("%H.%M.%S  %d/%m/%Y")
    with open(f'{DIR_ROBOTS}/{domain}.txt', 'w') as file:
        write = file.write(f'{date}\n\n{domain}\n\n{robotsFile}\n')

def requestDomain(domain):
    robots = '../../../robots.txt'
    response = requests.get(f'{domain}/{robots}', headers=head())
    if response.status_code == 200:
        response = response.text
        bs = BeautifulSoup(response, 'lxml')
        robotsFile = bs.body.get_text()
        print(robotsFile)
        writeRobots(domain, robotsFile)
    else:print(f'Status Code: {response.status_code}')


def searchRobots(domain):
    domain = domain
    if 'http://' in domain or 'https://' in domain:domain = domain
    else:domain = f'http://{domain}'
    requestDomain(domain)

