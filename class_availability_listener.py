from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
from bs4 import BeautifulSoup
import datetime
import sys

options = Options()
options.headless = True

search_url = 'https://padlock.idm.uab.edu/cas/login?service=https%3A%2F%2Fuab.instructure.com%2Flogin%2Fcas'

browser = Firefox(options=options)

x = True


def get_classes_num():
    print("Please wait. Fetching data...")
    browser.get(search_url)

    time.sleep(1)

    data = BeautifulSoup(browser.page_source, "html.parser")
    table = data.find('table', {'id': 'CatalogList'})
    if table is not None:
        tbody = table.find('tbody')
        return len(tbody.find_all('tr'))
    else:
        print("No classes found. They're all gone!!")
        sys.exit()


initialNum = get_classes_num()
print("Currently there are " + str(initialNum) + " classes open")

while x:
    currentNum = get_classes_num()

    if currentNum > initialNum:
        print("Just opened! " + str(currentNum) + " open class found at " + str(datetime.datetime.now()))
        options.headless = False
        browser = Firefox(options=options)
        browser.get(search_url)
        x = False
    else:
        print("Still only " + str(currentNum) + " open classes at " + str(datetime.datetime.now()))

    time.sleep(10 * 60)  # checks every 10 minutes
