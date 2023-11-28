    # def get_today_cash_remained(self, currency):
    #     remainder = self.limit - self.get_today_stats()
    #     if remainder > 0:
    #         if currency == RUB:
    #             return f'На сегодня осталось {remainder} руб'
    #         elif currency == USD:
    #             return f'На сегодня осталось {(remainder / CashCalculator.USD_RATE):.2f} USD'
    #         elif currency == EURO:
    #             return f'На сегодня осталось {(remainder / CashCalculator.EURO_RATE):.2f} Euro'
    #         else:
    #             return 'Вы ввели некорректную валюту. Доступные валюты: rub, usd, eur.'
    #     elif remainder == 0:
    #         return 'Денег нет, но вы держитесь.'
    #     else:
    #         if currency == RUB:
    #             return f'Денег нет, держись: твой долг - {-remainder} руб'
    #         elif currency == USD:
    #             return f'Денег нет, держись: твой долг - {-(remainder / CashCalculator.USD_RATE):.2f} USD'
    #         elif currency == EURO:
    #             return f'Денег нет, держись: твой долг - {-(remainder / CashCalculator.EURO_RATE):.2f} Euro'
    #         else:
    #             return 'Вы ввели некорректную валюту. Доступные валюты: rub, usd, eur.'