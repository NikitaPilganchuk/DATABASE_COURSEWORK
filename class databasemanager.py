import psycopg2
class DBMager:
    '''
    Класс DBMager для работы с Базой данных
    '''
    def get_companies_and_vacancies_count(self):
        '''
         получает список всех компаний и количество вакансий у каждой компании.
        :return:
        '''

        with psycopg2.connect(
            host="localhost",
            database="KURSACH",
            user="postgres",
            password='A5A4A3a2a1'
        ) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT company_name, COUNT(vacancy_name) FROM hhru GROUP BY DISTINCT company_name")
                data = cur.fetchall()
                print(data)

    def get_all_vacancies(self):
        '''
        получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
        :return:
        '''
        with psycopg2.connect(
            host="localhost",
            database="KURSACH",
            user="postgres",
            password='A5A4A3a2a1'
        ) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM hhru")
                data = cur.fetchall()
                print(data)

    def get_avg_salary(self):
        '''
        получает среднюю зарплату по вакансиям.
        :return:
        '''
        with psycopg2.connect(
            host="localhost",
            database="KURSACH",
            user="postgres",
            password='A5A4A3a2a1'
        ) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT ROUND(AVG(salary), 0) FROM hhru")
                data = cur.fetchall()
                print(data)

    def get_vacancies_with_higher_salary(self):
        '''
        получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        :return:
        '''
        with psycopg2.connect(
            host="localhost",
            database="KURSACH",
            user="postgres",
            password='A5A4A3a2a1'
        ) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM hhru WHERE salary > (SELECT AVG(salary) FROM hhru)")
                data = cur.fetchall()
                print(data)

    def get_vacancies_with_keyword(self, word):
        '''
        получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python.
        :param word:
        :return:
        '''
        with psycopg2.connect(
            host="localhost",
            database="KURSACH",
            user="postgres",
            password='A5A4A3a2a1'
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM hhru WHERE vacancy_name LIKE '%{word}%'")
                data = cur.fetchall()
                print(data)
