# Сравниваем вакансии программистов

Программа позволяет с помощью Python проводить анализ данных по зарплатам вакасний разрабочтиков на различных языках программирования.
Вывод осуществляется в терминал/консоль среды разработки в виде таблицы.
Проект использует данные с сайтов https://hh.ru, https://superjob.ru и анализирует данные по зарплатам программистов в Москве.

## Как установить

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Для начала работы Вам потребуется токен для доступа к API SuperJob

Регистрируемся и получаем токен по адресу: https://api.superjob.ru/. Полученный токен сохраните в переменную `API_KEY_SJ` файла `.env` проекта:
```
API_TOKEN_SJ='YOUR_SUPERJOB_API_KEY'
```
Пример токена:
```
v3.r.116856937.a1a0369a8e4355c6aa16cae9db178ccd99b792b2.4e704c029630604c4b8020c1cea583e0592b2fde
```
### Как запустить программу 

Запускаем скрипт из терминала стандартно, командой `main.py`: 


```  
your-computer:~/your-directory/this-project-name$ main.py
```  
Результат работы программы:

<img src="https://i.postimg.cc/mDDX3Z6T/2022-02-27-23-01-23.png" width="450" height="400">

### Дополнительные возможности

Программа использует API веб-сервисов https://hh.ru, https://superjob.ru. 
С информацией о данных API можно ознакомиться здесь: https://api.superjob.ru/
и здесь: https://dev.hh.ru/.
В случае, если Вы хотите скорректировать те либо иные параметры запроса и/или добавит иные параметры запроса, это возможно сделать в файле `language_dataset_getter.py` в словарях `payload` функций `get_language_dataset_hh` и `get_language_dataset_superJob` для API HeadHunter и SuperJob, соответственно:

```python

def get_language_dataset_hh(language_name, api_token_hh=None):

    vacancies_on_page = []
    page, pages = 0, 1
    url = 'https://api.hh.ru/vacancies'
    payload = {
        'text': f'программист {language_name}',
        'area': '1',
        'period': '30',
        'per_page': '100',
        'page': page,
    }
    ...
```

```python

def get_language_dataset_superJob(language_name, api_token_sj):

    vacancies_on_page = []
    page = 0
    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {
        'X-Api-App-Id': api_token_sj,
    }

    payload = {
        'keyword': f'программист {language_name}',
        'date_published_from': '1642896000',
        'town': '4',
        'count': '100',
        'page': page
    }


```



Список языков программирования, по которым осуществляется подбор вакансий передается в качестве списка `language_names` файла `main.py`.
По умолчанию:

```python

language_names = [
    'js',
    'java',
    'python',
    'ruby',
    'php',
    'c++',
    'c#',
    'c:',
    'go:',
    'shell',
]
```
Данный список, соответственно, можно изменить по Вашему желанию. 

### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
