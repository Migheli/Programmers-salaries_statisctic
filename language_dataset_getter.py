import requests
from itertools import count
from statistics import mean, StatisticsError
from salary_predictor import predict_rub_salary_for_sj, predict_rub_salary_for_hh


def get_language_dataset_hh(language_name):

    url = 'https://api.hh.ru/vacancies'
    payload = {
        'text': f'программист {language_name}',
        'area': '1',
        'period': '30',
        'per_page': '100',
        'page': 0,
    }

    vacancies_pages = []

    for page in count():
        payload['page'] = page
        page_response = requests.get(url=url, params=payload)
        page_response.raise_for_status()
        page_data = page_response.json()
        vacancies_found = page_data['found']
        vacancies_pages.append(page_data['items'])
        if (page >= page_data['pages']) or (page >= 19):
            break

    vacancies = [vacancie for vacancie_page in vacancies_pages for vacancie in vacancie_page]
    salaries_processed = []
    for vacancy in vacancies:
        salary = predict_rub_salary_for_hh(vacancy)
        if salary:
            salaries_processed.append(salary)
            try:
                average_salary = int(mean(salaries_processed))
            except StatisticsError:
                average_salary = None

    hh_language_dataset = {
                "vacancies_found": vacancies_found,
                "vacancies_processed": len(salaries_processed),
                "average_salary": average_salary,
    }

    return hh_language_dataset


def get_language_dataset_sj(language_name, api_token_sj):

    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {
        'X-Api-App-Id': api_token_sj,
    }

    payload = {
        'keyword': f'программист {language_name}',
        'date_published_from': '1642896000',
        'town': '4',
        'count': '100',
        'page': 0
    }

    vacancies_pages = []

    for page in count():
        payload['page'] = page
        page_response = requests.get(url=url, headers=headers, params=payload)
        page_response.raise_for_status()
        page_data = page_response.json()
        vacancies_found = page_data['total']
        vacancies_pages.append(page_data['objects'])
        if not page_data['more']:
            break

    vacancies = [vacancie for vacancie_page in vacancies_pages for vacancie in vacancie_page]
    salaries_processed = []
    for vacancy in vacancies:
        salary = predict_rub_salary_for_sj(vacancy)
        if salary:
            salaries_processed.append(salary)
            try:
                average_salary = int(mean(salaries_processed))
            except StatisticsError:
                average_salary = None

    sj_language_dataset = {
        "vacancies_found": vacancies_found,
        "vacancies_processed": len(salaries_processed),
        "average_salary": average_salary,
    }

    return sj_language_dataset
