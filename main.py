from src.API import Get_vacancies
from src.Vacancy import Vacancy
from src.WorkWithFile import Json_saver

def main():
    ''' Запрос названия вакансии и проверка на наличие найденных вакансий'''
    user_vacancy = input('Введите название вакансии: ')
    found_vacancies = Get_vacancies(user_vacancy).get_vacancies()
    if len(found_vacancies) == 0:
        print('Вакансии не найдены')
        exit()

    ''' Запрос на доп. критерии такие как город и кол-во вакансий для вывода'''
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

    sorted_vacancies = sorted(vacancy_formed, reverse=True)
    top_vacancies = sorted_vacancies[:user_top]
    Json_saver().add_vacancies(top_vacancies)
    print(f'Найденные вакансии: \n')
    for vacancy in top_vacancies:
        print(vacancy)

if __name__ == '__main__':
    main()