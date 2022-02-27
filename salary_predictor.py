from statistics import mean


def predict_salary(salary_from, salary_to):
    if salary_from and salary_to:
        average_salary = mean([salary_from, salary_to])
    elif salary_from:
        average_salary = salary_from * 1.2
    else:
        average_salary = salary_to * 0.8
    return average_salary


def predict_rub_salary_for_hh(vacancy):
    salary = vacancy['salary']
    if salary and salary['currency'] == 'RUR':
        salary_from, salary_to = salary['from'], salary['to']
        return predict_salary(salary_from, salary_to)


def predict_rub_salary_for_superJob(vacancy):
    salary = bool(vacancy['payment_from'] or vacancy['payment_to'])
    if salary and vacancy['currency'] == 'rub':
        salary_from, salary_to = vacancy['payment_from'], vacancy['payment_to']
        return predict_salary(salary_from, salary_to)
