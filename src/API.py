import requests
import json
from abc import ABC, abstractmethod

class AbstractAPI(ABC):
    @abstractmethod
    def get_vacancies(self):
        pass

class Get_vacancies(AbstractAPI):
    def __init__(self, vacancy_name):
        self.vacancy_name: str = vacancy_name
        self.base_url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self):
        keys_response = {'text': f'NAME:{self.vacancy_name}', 'area': 113, 'per_page': 100, }
        info = requests.get(self.base_url, keys_response)
        return json.loads(info.text)['items']