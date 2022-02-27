import requests
from statistics import mean
from salary_predictor import predict_rub_salary_for_superJob, predict_rub_salary_for_hh


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

    vacancies_found = requests.get(url, params=payload).json()['found']

    while page < pages:
        payload['page'] = page
        page_response = requests.get(url, params=payload)
        page_response.raise_for_status()
        pages = page_response.json()['pages']
        page += 1
        vacancies_on_page.append(page_response.json()['items'])

    vacancies = [j for i in vacancies_on_page for j in i]
    salaries_processed = []
    for vacancy in vacancies:
        if predict_rub_salary_for_hh(vacancy):
            salaries_processed.append(predict_rub_salary_for_hh(vacancy))
    average_salary = mean(salaries_processed)

    hh_language_dataset = {
                "vacancies_found": vacancies_found,
                "vacancies_processed": len(salaries_processed),
                "average_salary": int(average_salary),
    }

    return hh_language_dataset


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

    next_page = True

    vacancies_found = 0

    while next_page:
        page_response = requests.get(url, headers=headers, params=payload)
        vacancies_found = page_response.json()['total']
        page_data = page_response.json()['objects']
        vacancies_on_page.append(page_data)
        next_page = page_response.json()['more']
        page += 1
        payload['page'] = page

    vacancies = [j for i in vacancies_on_page for j in i]
    salaries_processed = []
    for vacancy in vacancies:
        if predict_rub_salary_for_superJob(vacancy):
            salaries_processed.append(predict_rub_salary_for_superJob(vacancy))
    average_salary = mean(salaries_processed)

    superJob_language_dataset = {
        "vacancies_found": vacancies_found,
        "vacancies_processed": len(salaries_processed),
        "average_salary": int(average_salary),
    }

    return superJob_language_dataset
