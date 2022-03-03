from statistics import mean


def predict_salary(salary_from, salary_to):
    if salary_from and salary_to:
        average_salary = mean([salary_from, salary_to])
    elif salary_from:
        average_salary = salary_from * 1.2
    elif salary_to:
        average_salary = salary_to * 0.8
    else:
        average_salary = None
    return average_salary


def predict_rub_salary_for_hh(vacancy):
    salary = vacancy['salary']
    if salary and salary['currency'] == 'RUR':
        return predict_salary(salary['from'], salary['to'])


def predict_rub_salary_for_superJob(vacancy):
    if vacancy['currency'] == 'rub':
        return predict_salary(vacancy['payment_from'], vacancy['payment_to'])
