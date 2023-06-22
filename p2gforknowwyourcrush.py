import argparse
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

global count
global browser
parser = argparse.ArgumentParser(prog="app", description="Options for customizing program")
parser.add_argument('-b', '--browser', type=str.lower, metavar="",
                    help="Browser to use Whatsapp Web on [Chrome is default]",
                    choices=['chrome', 'firefox', 'edge', 'ie'])


args = vars(parser.parse_args())
selected_browser = args['browser']
try:

    if (selected_browser is None) or (selected_browser == 'chrome'):
        browser = webdriver.Chrome(ChromeDriverManager().install())

    else:
        exit("Invalid choice. Quitting now...")

except:
    exit('Error! Make sure you\'re selecting the right browser! Chrome is required')


browser.get('https://www.instagram.com')
sleep(5)


browser.find_element_by_name('username').send_keys('username')
browser.find_element_by_name('password').send_keys('password')
login_button = browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div")
#login_button = browser.find_element_by_css_selector('.sqdOP.L3NKy.y3zKF')
login_button.click()
sleep(5)

browser.get("https://www.instagram.com/direct/inbox/")
sleep(3)
not_now = browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
not_now.click()
count = 0
first_try = True
while True:
   try:
    if first_try:
        sleep(3)
        first_try=False
    else:
        sleep(0.5)
    first_div = browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[3]/div/div/div/div/div[1]/div")
                                             #"/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[3]/div/div/div/div/div[1]/div/a/div")
    first_div.click()
    sleep(2)
    try:
        get_name = browser.find_element_by_css_selector("#f2b2da71564ea48 > div > div > div > div")
        # get_name = browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[3]/div/div/div/div/div[1]/div/a/div/div[2]/div[1]/div")
        print("got xpath")
        name = get_name.text
        print(name)
    except:
        print("try nhi chala")
        name = ""

    browser.find_element_by_tag_name("textarea").send_keys(Keys.CONTROL,"v")
    sleep(2)
    send_button = browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")
                                               #"/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")
    send_button.click()
    info = browser.find_element_by_tag_name("polyline").click()
    move_to_general = browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/button")
                                                   #"/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/button")
    move_to_general.click()
    sleep(2)
    primary_button = browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[2]/div/div[1]/nav/div[1]/a/span")
                                                  #"/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[2]/div/div[1]/nav/div[1]/a/span")
    primary_button.click()
   except:
       count+=1
       if count == 50:
           #browser.refresh()
           browser.get("https://www.instagram.com/direct/inbox/")
           count = 0
