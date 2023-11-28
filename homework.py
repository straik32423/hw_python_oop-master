import datetime as dt

DATE_FORMAT = '%d.%m.%Y'


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
    RUB_RATE = 1.0

    def get_today_cash_remained(self, currency):
        RUB = 'rub'
        EURO = 'eur'
        USD = 'usd'
        rename = {
            RUB: 'руб',
            USD: 'USD',
            EURO: 'Euro',
        }
        currency_exchange_rates = {
            RUB: CashCalculator.RUB_RATE,
            EURO: CashCalculator.EURO_RATE,
            USD: CashCalculator.USD_RATE,
        }

        if currency not in currency_exchange_rates:
            return f'Вы ввели неправильную валюту. Доступные валюты: {', '.join(currency_exchange_rates)}.'

        remainder = self.limit - self.get_today_stats()
        remainder = remainder / currency_exchange_rates[currency]
        if remainder == 0:
            return 'Денег нет, держись'
        elif remainder > 0:
            return f'На сегодня осталось {remainder:.2f} {rename[currency]}'
        else:
            return f'Денег нет, держись: твой долг - {abs(remainder):.2f} {rename[currency]}'


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


my_money = CashCalculator(10_000)
r1 = Record(500, 'Hooker', '28.11.2023')
r2 = Record(600, 'Second hooker', '28.11.2023')
r3 = Record(8900, 'Cocaine', '18.11.2023')
my_money.add_record(r1)
my_money.add_record(r2)
my_money.add_record(r3)
print(my_money.get_today_cash_remained('rub'))
