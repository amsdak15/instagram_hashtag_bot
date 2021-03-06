from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
from fake_useragent import UserAgent
import random

username_list = ["@gmail.com'];
username=random.choices(username_list)
password=""

opt = Options()
ua = UserAgent()
userAgent = ua.random
print(userAgent)
opt.add_argument(f'user-agent={userAgent}')
opt.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
driver = webdriver.Chrome(options=opt)

def login() :
    # Goto login page
    driver.get("https://www.instagram.com/accounts/login/")
    driver.implicitly_wait(10)
    # Enter username
    user=driver.find_element_by_name("username")
    user.send_keys(username)
    # Enter password
    passwd=driver.find_element_by_name("password")
    passwd.send_keys(password)
    time.sleep(1)
    # Click login
    login_button_ = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div")
    login_button_.click()
    time.sleep(3)
    driver.save_screenshot("./login.png")

def logout():
    try:
        # Click profile icon
        driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]').click()
        time.sleep(3)
        # Click logout
        driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div').click()
        time.sleep(3)
        driver.save_screenshot("./logout.png")
    except:
        # Click profile icon
        driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]').click()
        time.sleep(3)
        # Click logout
        driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div').click()
        time.sleep(3)
        driver.save_screenshot("./logout.png")

login()
df = pd.read_excel('./normal.xlsx')

for i in range(len(df)):
    link= "https://www.instagram.com/explore/tags/" + df['Tags'][i] + "/"
    driver.get(link)
    driver.implicitly_wait(10)
    try:
        search_bar = driver.find_element_by_class_name("g47SY ").text
        df.loc[i,"Counts"]= search_bar
    except:
        df.loc[i,"Counts"]= 0

logout()
df.to_excel ('./normal.xlsx', index = False, header=True)
driver.delete_all_cookies()
driver.close()
