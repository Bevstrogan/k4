def sort_vacancies(vacancies):
    return sorted(vacancies, reverse=True)

def get_top_N(vacancies, Top_N):
    return vacancies[:Top_N]

def show_vacancies(vacancies):
    print('')
    for vacancy in vacancies:
        print(vacancy)