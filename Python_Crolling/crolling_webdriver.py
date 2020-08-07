# selenium은 webdriver api를 통해 browser를 control
# webdriver import
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pandas as pd
from bs4 import BeautifulSoup

# headless 설정을 추가 (phantomjs 지원안함)
options = Options()
options.add_argument('--headless')
options.add_argument('disable-gpu')
driver = webdriver.Chrome('c:/Users/uk0305/Desktop/Programming/crolling/chromedriver.exe')
#driver = webdriver.PhantomJS('/Users/uk0305/Desktop/Programming/crolling/phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver.implicitly_wait(3)

#url 접근
results = driver.get('https://etherscan.io/address/0xc9f5c896e398e4c5d682b687042795fe33f97ccf')
#results1 = [
#    ['Txn Hash', 'Block', 'Age', 'From', 'To', 'Value', '[Txn Fee]']
#]

#url 접근(Login)
#driver.get('https://etherscan.io/login')
# id/pw 
#driver.find_element_by_name('ctl00$ContentPlaceHolder1$txtUserName').send_keys('karas639')
#driver.find_element_by_name('ctl00$ContentPlaceHolder1$txtPassword').send_keys('ART8837type1@#')

#def clipboard_input(self, user_xpath, user_input):
#        pyperclip.copy(user_input) # input을 클립보드로 복사 
        #self.driver.find_element_by_xpath(user_xpath).click() # element focus 설정
        #ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform() # Ctrl+V 전달
        #time.sleep(1)

#driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnLogin"]').click()

#data = pd.DataFrame(results)

html = '<div class="card">' \
        '</div>'

def ex1():
    bs = BeautifulSoup(html, 'html.parser')
    print(bs, type(bs))

    tag = bs.div
    print(tag, type(tag))