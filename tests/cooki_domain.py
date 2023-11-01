from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://xn--d1abb2a.xn--p1ai/account/profile')

cookies = driver.get_cookies()

for cookie in cookies:
    domain = cookie['domain']
    print(f"Cookie Domain: {domain}")

driver.quit()