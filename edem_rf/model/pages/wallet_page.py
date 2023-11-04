from selene.support.shared import browser
from selene import be, have


class Wallet:

    def get_balance(self):
        balance = browser.driver.find_element('.balance - board_current').get_attribute("innerHTML")
        return balance
