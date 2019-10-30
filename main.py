import bs4
import requests
import urllib3
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("https://kurs.kz")
soup = bs4.BeautifulSoup(browser.page_source, 'html.parser')

names = []
for x in soup.find_all('a', attrs={'class': 'tab'}):
    names.append(x.text)
buyPrice = []
for x in soup.find_all('span', attrs={'title': 'USD - покупка'}):
    buyPrice.append(x.text)
sellPrice = []
for x in soup.find_all('span', attrs={'title': 'USD - продажа'}):
    sellPrice.append(x.text)

browser.get("https://mail.ru")
time.sleep(5)

login = "stepjelion@mail.ru"
password = "TemirNeObmansik112"
to = "Zhauzhurek@bk.ru"
subject = "EVGENIY PAVLOV"

body = ""
body += "names: \n"
for x in names:
    body += x
    body += "\n"
body += "\n buyPrice: \n"
for x in buyPrice:
    body += x
    body += "\n"
body += "\n sellPrice: \n"
for x in sellPrice:
    body += x
    body += "\n"
print(body)

time.sleep(3)
loginElement = browser.find_element_by_id("mailbox:login")
loginElement.send_keys(login)
browser.find_element_by_xpath('//input[@value="Ввести пароль"]').click()

time.sleep(5)
passwordElement = browser.find_element_by_xpath('//input[@type="password"]')
passwordElement.send_keys(password)
browser.find_element_by_xpath('//input[@type="submit"]').click()

time.sleep(30)
# browser.find_element_by_xpath('//span[@title="Написать письмо"]').click()
browser.find_element_by_class_name("sidebar__compose-btn-box").click()
time.sleep(5)
toElement = browser.find_element_by_xpath("/html/body/div[15]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div/div/div[1]/div/div[2]/div/div/label/div/div/input")
toElement.send_keys(to)
subjectElement = browser.find_element_by_xpath("/html/body/div[15]/div[2]/div/div[1]/div[2]/div[3]/div[3]/div[1]/div[2]/div/input")
subjectElement.send_keys(subject)
bodyElement = browser.find_element_by_xpath("/html/body/div[15]/div[2]/div/div[1]/div[2]/div[3]/div[5]/div/div/div[2]/div[1]")
bodyElement.send_keys(body)
browser.find_element_by_xpath("/html/body/div[15]/div[2]/div/div[2]/div[1]/span[1]").click()
# search = browser.find_element_by_name('q')
# search.send_keys("HAHA")

# search.send_keys(Keys.RETURN)
