import datetime as dt

DATE_FORMAT = '%d.%m.%Y'
RUB = 'rub'
EURO = 'eur'
USD = 'usd'


class Calculator:

    def __init__(self, limit: int) -> None:
        self.records: list[Record] = []
        self.limit = limit

    def add_record(self, record: 'Record') -> None:
        self.records.append(record)

    def get_today_stats(self) -> int:
        today = dt.date.today()
        today_amount = 0
        for record in self.records:
            if record.date == today:
                today_amount += record.amount
        return today_amount

    def get_week_stats(self) -> int:
        today = dt.date.today()
        week_ago = today - dt.timedelta(weeks=1)
        amount = 0
        for record in self.records:
            if record.date >= week_ago and record.date <= today:
                amount += record.amount
        return amount


class CashCalculator(Calculator):

    USD_RATE = 88.1
    EURO_RATE = 96.1

    def get_today_cash_remained(self, currency):
        remainder = self.limit - self.get_today_stats()
        if remainder > 0:
            if currency == RUB:
                return f'На сегодня осталось {remainder} руб'
            elif currency == USD:
                return f'На сегодня осталось {(remainder / CashCalculator.USD_RATE):.2f} USD'
            elif currency == EURO:
                return f'На сегодня осталось {(remainder / CashCalculator.EURO_RATE):.2f} Euro'
            else:
                return 'Вы ввели некорректную валюту. Доступные валюты: rub, usd, eur.'
        elif remainder == 0:
            if currency not in ('rub', EURO, USD):
                return 'Вы ввели некорректную валюту. Доступные валюты: rub, usd, eur.'
            return 'Денег нет, держись'
        else:
            if currency == RUB:
                return f'Денег нет, держись: твой долг - {abs(remainder)} руб'
            elif currency == USD:
                return f'Денег нет, держись: твой долг - {abs(remainder / CashCalculator.USD_RATE):.2f} USD'
            elif currency == EURO:
                return f'Денег нет, держись: твой долг - {abs(remainder / CashCalculator.EURO_RATE):.2f} Euro'
            else:
                return 'Вы ввели некорректную валюту. Доступные валюты: rub, usd, eur.'


class Record:

    def __init__(self, amount, comment, date=None):
        if date is None:
            date = dt.date.today()
        else:
            date = dt.datetime.strptime(date, DATE_FORMAT).date()
        self.date = date
        self.amount = amount
        self.comment = comment


class CaloriesCalculator(Calculator):

    def get_calories_remained(self) -> str:
        today_eaten: int = self.get_today_stats()
        if today_eaten < self.limit:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit - today_eaten} кКал'
        else:
            return 'Хватит есть!'
