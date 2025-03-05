import locale



class Currency:
    @staticmethod
    def format_currency(amount: float) -> str:
        locale.setlocale(locale.LC_ALL, 'en_GB')

        return locale.currency(amount, grouping=True)
