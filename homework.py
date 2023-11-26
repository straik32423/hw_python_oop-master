import datetime as dt

DATE_FORMAT = '%d.%m.%Y'
USD_RATE = 88
EURO_RATE = 96
RUB = 'rub'
EURO = 'eur'
USD = 'usd'


class Calculator:

    def __init__(self, limit: int) -> None:
        self.records: list[Record] = []
        self.limit = limit

    def add_record(self, record: 'Record') -> None:
        self.records.append(record)
        print('Record added!')

    def get_today_stats(self) -> int:
        today = dt.datetime.today()
        today_amount = 0
        for record in self.records:
            if record.date.date() == today.date():
                today_amount += record.amount
        return today_amount

    def get_week_stats(self) -> int:
        pass


class CashCalculator(Calculator):

    def get_today_cash_remained(self, currency: str) -> str:
        total_today = self.get_today_stats()
        remainder = self.limit - total_today
        if remainder > 0:
            if currency == RUB:
                return f'На сегодня осталось {remainder} руб'
            elif currency == USD:
                return f'На сегодня осталось {remainder / USD_RATE} USD'
            else:
                return f'На сегодня осталось {remainder / EURO_RATE} Euro'
        elif remainder == 0:
            return 'Денег нет, но вы держитесь.'
        else:
            if currency == RUB:
                return f'Денег нет, держись: твой долг - {-remainder} руб'
            elif currency == USD:
                return f'Денег нет, держись: твой долг - {-round(remainder / USD_RATE, 2)} USD'
            else:
                return f'Денег нет, держись: твой долг - {-round(remainder / EURO_RATE, 2)} Euro'


class Record:

    def __init__(self, amount: int, date: str, comment: str) -> None:
        self.amount: int = amount
        self.date: dt.datetime = dt.datetime.strptime(date, DATE_FORMAT)
        self.comment: str = comment


my_money = CashCalculator(10_000)
r1 = Record(500, '26.11.2023', 'Hooker')
r2 = Record(600, '26.11.2023', 'Second hooker')
r3 = Record(8900, '18.11.2023', 'Cocaine')
my_money.add_record(r1)
my_money.add_record(r2)
my_money.add_record(r3)
print(my_money.get_today_cash_remained(RUB))
print(my_money.get_week_stats())
