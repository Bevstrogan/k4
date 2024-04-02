from src.API import Get_vacancies
from src.Vacancy import Vacancy
from src.Utils import *

def main():
    user_vacancy = input('Введите название вакансии: ')
    found_vacancies = Get_vacancies(user_vacancy).get_vacancies()
    if len(found_vacancies) == 0:
        print('Вакансии не найдены')
        exit()

    user_city = input('Введите название города: ')
    user_top = int(input('Введите колличесво вакансий для вывода: '))
    vacancy_formed = []
    for vacancy in found_vacancies:
        name = vacancy.get('name', 'Название не указано')
        experience_check = vacancy.get('experience')
        if experience_check:
            experience = experience_check.get('name', 'Опыт работы не указан')
        else:
            experience = 'Опыт работы не указан'
        salary_info = vacancy.get('salary')
        if salary_info:
            salary_from = salary_info.get('from', 'Не указано')
            salary_to = salary_info.get('to', 'Не указано')
        else:
            salary_from = 'Не указано'
            salary_to = 'Не указано'
        if salary_from == None:
            salary_from = 0
        if salary_to == None:
            salary_to = 'Не указано'
        url = vacancy.get('alternate_url', 'Ссылка не указана')
        address = vacancy.get('address')
        if address:
            city = address.get('city', 'Не указан')
        else:
            city = 'Не указан'
        if city == None:
            city = 'Не указан'
        if isinstance(salary_from, int) and isinstance(salary_to, int) and str(city.lower()) == user_city.lower():
            vacancy_formed.append(Vacancy(name, experience, salary_from, salary_to, url))

    sorted_vacancies = sort_vacancies(vacancy_formed)
    top_vacancies = get_top_N(sorted_vacancies, user_top)
    show_vacancies(top_vacancies)

if __name__ == '__main__':
    main()