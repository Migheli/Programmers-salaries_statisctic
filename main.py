import os
from terminaltables import AsciiTable
from dotenv import load_dotenv
from language_dataset_getter import get_language_dataset_hh, get_language_dataset_superJob


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


def get_vacancies_table(get_language_dataset_func, language_names, title, api_token=None):
    table_data = [
        (
            'Язык программирования',
            'Вакансий найдено',
            'Вакансий обработано',
            'Средняя зарплата',
        )
    ]
    for language_name in language_names:
        language_vacancies_dataset = get_language_dataset_func(language_name, api_token)
        table_data.append(
            (
                language_name,
                language_vacancies_dataset['vacancies_found'],
                language_vacancies_dataset['vacancies_processed'],
                language_vacancies_dataset['average_salary'],
            )
        )

    table = AsciiTable(table_data, title)
    table.justify_columns[4] = 'left'
    table = table.table
    return table


def main():
    load_dotenv()
    api_token_sj = os.getenv('API_TOKEN_SJ')
    print(get_vacancies_table(get_language_dataset_hh, language_names, 'HeadHunter Moscow'))
    print(get_vacancies_table(get_language_dataset_superJob, language_names, 'SuperJob Moscow', api_token_sj))


if __name__ == '__main__':
    main()
