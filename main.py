''' '''
import requests
import psycopg2
from dotenv import load_dotenv
import os


load_dotenv()
def get_employers(params):
    ''' Получение списка всех компаний'''
    employers_id = []
    response = requests.get('https://api.hh.ru/vacancies', params=params)
    if response.status_code == 200:
        print('Запрос получен успешно')
    else:
        print(f"Request failed with status code: {response.status_code}")
    for i in response.json()['items']:
        employers_id.append(i['employer']['id'])
    return employers_id


def get_vacancies(employers_id):
    ''' Получение всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию'''
    params = {'only_with_salary': True}
    data = []
    for employer in employers_id[:15]:
        params['employer_id'] = employer
        response = requests.get('https://api.hh.ru/vacancies', params=params)
        for vacancy in response.json()['items']:
            middle = 0
            if vacancy['salary']['from'] and vacancy['salary']['to']:
                middle = vacancy['salary']['from']
            elif vacancy['salary']['from'] and not vacancy['salary']['to']:
                middle = vacancy['salary']['from']
            elif vacancy['salary']['to'] and not vacancy['salary']['from']:
                middle = vacancy['salary']['to']
            elif vacancy['salary'] == None:
                middle = 0
            i = {
                'salary': middle,
                'company_name': vacancy['employer']['name'],
                'vacancy_name': vacancy['name'],
                'url': vacancy['alternate_url']
            }
            data.append(i)
    print('Возвращаем данные')
    return data
def append_data_to_db(data):
    ''' Добавление данных в БД'''
    with psycopg2.connect(
        host=os.getenv('host'),
        database=os.getenv('database'),
        user=os.getenv('user'),
        password=os.getenv('password')
    ) as conn:
        with conn.cursor() as cur:
            for vacancy in data:
                cur.execute(
                    "INSERT INTO hhru VALUES(%s, %s, %s, %s)", (vacancy['company_name'], vacancy['vacancy_name'], vacancy['salary'], vacancy['url']))
    print('Данные добавлены в БД')



def create_table():
    ''' Создание таблицы hhru в БД'''
    with psycopg2.connect(
        host=os.getenv('host'),
        database=os.getenv('database'),
        user=os.getenv('user'),
        password=os.getenv('password')
    ) as conn:
        with conn.cursor() as cur:
            cur.execute("CREATE TABLE hhru (company_name VARCHAR(255), vacancy_name VARCHAR(255), salary INTEGER, url VARCHAR(255))")
    print('Таблица создана')

def delete_table():
    ''' Удаление таблицы hhru из БД'''
    with psycopg2.connect(
        host=os.getenv('host'),
        database=os.getenv('database'),
        user=os.getenv('user'),
        password=os.getenv('password')
    ) as conn:
        with conn.cursor() as cur:
            cur.execute("DROP TABLE hhru")
    print('Таблица удалена')