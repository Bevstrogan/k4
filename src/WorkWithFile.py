from abc import ABC, abstractmethod
import json

class AbstractVacancySaver(ABC):
    @abstractmethod
    def add_vacancies(self, vacancy_list):
        pass

    @abstractmethod
    def print_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass

class Json_saver(AbstractVacancySaver):
    ''' Класс для работы с  JSON файлом '''
    def add_vacancies(self, vacancy_list):
        list_vacancies = []
        for vacancy in vacancy_list:
            name = vacancy.name
            experience = vacancy.experience
            salary_from = vacancy.salary_min
            salary_to = vacancy.salary_max
            url = vacancy.url
            vacancy_info = {
                'Название вакансии:': name,
                'Опыт работы:': experience,
                'Зарплата от:': salary_from,
                'Зарплата до:': salary_to,
                'Ссылка:': url
            }
            list_vacancies.append(vacancy_info)

        with open('data/vacancies.json', 'w', encoding='utf-8') as file:
            json.dump(list_vacancies, file, ensure_ascii=False, indent=4)
    def delete_vacancies(self):
        with open("data/vacancies.json", "w") as f:
            pass

    def print_vacancies(self):
        with open("data/vacancies.json", 'r') as f:
            f = json.dumps(json.load(f), ensure_ascii=False, indent=4)
            print(f)