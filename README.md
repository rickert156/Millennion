# Fake User Agent

Создайте виртуальное окружение
```sh
python3 -m venv venv
```

Активируете виртуальное окружение
```sh
source venv/bin/activate
```

Установите необходимые модули для работы
```sh
pip install -r requirements.txt
```
Пример использования:
```sh
from utils.generateAgent import head
import requests

site = 'https://example.com/'

response = requests.get(site, headers=head())
```
