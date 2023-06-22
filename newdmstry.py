import argparse
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pyperclip

# messages = pyperclip.paste()

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
def login_insta():

        browser.get('https://instagram.com')
        sleep(2)
        browser.find_element_by_name('username').send_keys("crush_name_teller01")
        browser.find_element_by_name('password').send_keys("Aditya@8544")
        login_button = browser.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button")
        login_button.click()
def enter_request():
    sleep(5)
    browser.get('https://www.instagram.com/direct/inbox/')

def exception():
    try:
        browser.find_element_by_css_selector("._a9--._a9_1").click()
    except:
        pass
count = 0
def dig_message():
    global count
    try:

            # requests
            browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[1]/div/div[2]/div[3]/span/span").click()
            # browser.find_element_by_css_selector("._aacl._aaco._aacw._aad0._aad6._aade").click()
            sleep(4)
            #first_msg
            try:
                browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[1]/div/div/div/div[3]/div/div/div/div[2]").find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[1]/div/div/div/div[3]/div/div/div/div[2]/div/div[1]").click()
                print("mila ")
            except:
                browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[1]/div/div/div/div[3]/div/div/div/div[2]/div/div[1]").click()
                print("lele bhai")

            #allow
            sleep(5)
            browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/ul/li[5]/div").click()
            print("Not clicked")
            #primary
            browser.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/button[1]").click()
            print("primary clicked")
            #textarea
            sleep(5)
            # msg = "Hey " + name + "!!" + messages
            # pyperclip.copy(msg)
            # print(msg)
            try:
                browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]").send_keys(Keys.CONTROL, "v")
                # browser.find_element_by_tag_name("textarea").send_keys(Keys.CONTROL, "v")
                print("Nhi mila message box")
            except:
                browser.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(Keys.CONTROL, "v")
                print("avi v nhi mila")
            #send
            sleep(2)
            browser.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[3]").click()
            print("message send")


    except:
        exception()
        if count == 1000:
                count = 0
                browser.refresh()
                browser.get('https://www.instagram.com/direct/inbox/')
        else:
            count+=1

login_insta()
enter_request()
while True:
    try:
        dig_message()
    except:
        browser.refresh()
        browser.get('https://www.instagram.com/direct/inbox/')








