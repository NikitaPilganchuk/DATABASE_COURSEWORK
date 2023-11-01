from main import *
from class_dbmanager import DBMager



def user_interaction():
    print("В базе данных хранятся вакансии Python разработчика\nВыберите нужное действие:")
    user_input = input('''1 - получить список всех компаний и количества вакансий у каждой компании
    2 - получить список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
    3 - среднюю зарплату по вакансиям
    4 - список всех вакансий, у которых зарплата выше средней по всем вакансиям
    5 - получить вакансии по названию
    ''')
    append_data_to_db(get_vacancies(get_employers({'text': 'Python'})))
    dbm = DBMager()
    if user_input == '1':
        dbm.get_companies_and_vacancies_count()
    elif user_input == '2':
        dbm.get_all_vacancies()
    elif user_input == '3':
        dbm.get_avg_salary()
    elif user_input == '4':
        dbm.get_vacancies_with_higher_salary()
    elif user_input == '5':
        user_input = input('Введите название вакансии: ')
        dbm.get_vacancies_with_keyword(user_input)

user_interaction()