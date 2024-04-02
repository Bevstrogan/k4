
class Vacancy:
    def __init__(self, name, experience, salary_min, salary_max, url):
        self.name = name
        self.experience = experience
        self.salary_min = salary_min
        self.salary_max = salary_max
        self.url = url

    def __lt__(self, other):
        if self.salary_min and other.salary_min:
            if isinstance(self.salary_min, int) and isinstance(other.salary_min, int):
                return self.salary_min < other.salary_min
        return 0

    def __gt__(self, other):
        return self.salary_min > other.salary_min

    def __str__(self):
        return (f'Название вакансии: {self.name}\n'
                f'Зарплата от: {self.salary_min}\n'
                f'Зарплата до:  {self.salary_max}\n'
                f'Опыт работы: {self.experience}\n'
                f'Ссылка: {self.url}\n')
