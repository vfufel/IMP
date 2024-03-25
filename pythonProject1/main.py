import datetime

from application.salary import calculate_salary as cs
from application.db.people import get_employees as ge


def date():
    today = datetime.date.today()
    return today


if __name__ == '__main__':
    print(cs())
    print(ge())
    print(date())
