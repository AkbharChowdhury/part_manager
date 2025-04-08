import sqlite3
from contextlib import closing


class Database:
    def __db_name(self):
        return 'hr.db'

    def fetch_employees(self):
        with sqlite3.connect(self.__db_name()) as con:
            con.row_factory = sqlite3.Row
            with closing(con.cursor()) as cur:
                cur.execute('SELECT employee_id, firstname, lastname FROM employees')
                return [dict(row) for row in cur.fetchall()]

    def add_employees(self, data: list[tuple['str', 'str']]):
        with sqlite3.connect(self.__db_name()) as con:
            with closing(con.cursor()) as cur:
                cur.executemany("INSERT INTO employees(firstname, lastname) VALUES(?, ?)", data)

    def add_employees_dict(self, data: list[dict['str', 'str']]):
        with sqlite3.connect(self.__db_name()) as con:
            with closing(con.cursor()) as cur:
                cur.executemany("INSERT INTO employees(firstname, lastname) VALUES(:firstname, :lastname)", data)


def main():
    db = Database()
    # db.add_employees([
    #     ('John','Smith'),
    #     ('Joe','Smith')
    # ])

    # db.add_employees_dict([
    #     {'firstname': 'Barry', 'lastname': 'Smith'},
    #     {'firstname': 'Amy', 'lastname': 'Larson'},
    # ])
    print(db.fetch_employees())
    employees = db.fetch_employees()
    print('list of employees'.capitalize())
    print('--------------------------------')
    for emp in sorted(employees, key=lambda x: x['firstname']):
        print(f'{emp.get('firstname')} {emp.get('lastname')}'.title())


if __name__ == '__main__':
    main()