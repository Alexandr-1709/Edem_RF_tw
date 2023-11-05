from selene.support.shared import browser


class Wallet:

    def __init__(self):
        self.balance = None

    def get_balance(self):
        self.balance = browser.element('.balance-board_current').locate().text
        return int(''.join(filter(str.isdigit, self.balance)))



