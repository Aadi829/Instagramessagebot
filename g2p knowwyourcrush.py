import argparse
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pyperclip

messages = pyperclip.paste()
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
sleep(2)

browser.find_element_by_name('username').send_keys('username')
browser.find_element_by_name('password').send_keys('password')
login_button = browser.find_element_by_xpath(
    "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div")
# login_button = browser.find_element_by_css_selector('.sqdOP.L3NKy.y3zKF')
login_button.click()
sleep(6)

browser.get("https://www.instagram.com/direct/inbox/")
sleep(3)
not_now = browser.find_element_by_xpath(
    "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
not_now.click()
count = 0
first_try = True
while True:
    try:
        # new changes
        get_name = browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[3]/div/div/div/div/div[1]/a/div[1]/div/div/div[2]/div/div/span[1]/span/div/div/span")
                                               # "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[3]/div/div/div/div/div[1]/div/a/div/div[2]/div[1]/div/div/div/div")
        name = get_name.text
        print(name)
        if first_try:
            sleep(3)
            first_try = False
        else:
            sleep(1)
        first_div = browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[3]/div/div/div/div/div[1]/a/div[1]")
                                                # "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[3]/div/div/div/div/div[1]/div/a/div")
        first_div.click()
        print("clicked")
        sleep(2)
        # try:
        #     get_name = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/div[2]/button/div/div[1]/div")
        #     name = get_name.text
        # except:
        #     name = ""

        msg = "Just last step buddy " + name + "!!  " + messages
        pyperclip.copy(msg)
        browser.find_element_by_tag_name("textarea").send_keys(Keys.CONTROL, "v")
        sleep(2)
        send_button = browser.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/div")
        send_button.click()
        sleep(2)
        info = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[1]/div/div/div[3]/button[3]").click()
        # info = browser.find_element_by_tag_name("polyline").click()
        move_to_general = browser.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div[2]")
        move_to_general.click()
        primary_button = browser.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/div[2]/div/div[1]/nav/div[2]/a/span")
        primary_button.click()
    except:
        count += 1
        if count == 1000:
            browser.refresh()
            # browser.get("https://www.instagram.com/direct/inbox/")
            count = 0
