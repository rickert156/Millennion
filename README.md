# Fake User Agent

Создайте виртуальное окружение
```sh
python3 -m venv venv
```

Активируйте виртуальное окружение
```sh
source venv/bin/activate
```

Установите необходимые модули для работы
```sh
pip install -r requirements.txt
```
## Работа с модулем Head

Пример использования(Requests):
```sh
from utils.generateAgent import head
import requests

site = 'https://example.com/'

response = requests.get(site, headers=head())
```

Пример использования(Selenium)
```sh
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.generateAgent import head
import time

options = Options()
options.add_argument(f'user-agent={head()}')

site = 'https://example.com/'

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(site)
time.sleep(5)
```
## Логирование с моделем Loger

```sh
from utils.loger import Loger

dataServer = response.headers
Loger(site, dataServer)
```

## Использование модуля Whois
В модуле уже подключен user-agent
```sh
from whois.whois import whois

whois('site.com')
```
