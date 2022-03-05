import os
from terminaltables import AsciiTable
from dotenv import load_dotenv
from language_dataset_getter import get_language_dataset_hh, get_language_dataset_sj


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

table_data_headers = (
    (
        'Язык программирования',
        'Вакансий найдено',
        'Вакансий обработано',
        'Средняя зарплата',
    )
)


def get_vacancies_data(table_data, language_name):
    vacancies_table = (
        (
            language_name,
            table_data['vacancies_found'],
            table_data['vacancies_processed'],
            table_data['average_salary'],
        )
    )
    return vacancies_table


def get_vacancies_table(table_data, title):
    table = AsciiTable(table_data, title)
    table.justify_columns[4] = 'left'
    table = table.table
    return table


table_data_hh = [table_data_headers]
table_data_sj = [table_data_headers]


def main():

    load_dotenv()
    api_token_sj = os.getenv('API_TOKEN_SJ')

    for language_name in language_names:
        hh_dataset = get_language_dataset_hh(language_name)
        sj_dataset = get_language_dataset_sj(language_name, api_token_sj)
        table_data_hh.append(get_vacancies_data(hh_dataset, language_name))
        table_data_sj.append(get_vacancies_data(sj_dataset, language_name))

    print(get_vacancies_table(table_data_hh, 'HeadHunter Moscow'))
    print(get_vacancies_table(table_data_sj, 'SuperJob Moscow'))


if __name__ == '__main__':
    main()
