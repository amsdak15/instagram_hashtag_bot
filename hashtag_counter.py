from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

username="hashtaginstagram1@gmail.com";
password="zaq.12345"

opt = Options()
opt.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' 
driver = webdriver.Chrome(options=opt)

driver.get("https://www.instagram.com/accounts/login/")
driver.implicitly_wait(10)
user=driver.find_element_by_name("username")
user.send_keys(username)
passwd=driver.find_element_by_name("password")
passwd.send_keys(password)
time.sleep(1)
login_button_ = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div")
login_button_.click()
time.sleep(3)
driver.save_screenshot("./pic1.png")

# df = pd.read_csv('./normal.csv')
# for i in range(len(df)):
#     link= "https://www.instagram.com/explore/tags/" + df['Tags'][i] + "/"
#     driver.get(link)
#     driver.implicitly_wait(10)
#     search_bar = driver.find_element_by_class_name("g47SY ").text  #g47SY 
#     df.loc[i,"Counts"]= search_bar
# df.to_csv ('./normal.csv', index = False, header=True)

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
df.to_excel ('./normal.xlsx', index = False, header=True)

driver.close()