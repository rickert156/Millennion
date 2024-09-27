import requests
from bs4 import BeautifulSoup
from agent.generateAgent import head

def whois(domain):
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
