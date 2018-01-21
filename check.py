import time
import sys
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
display = Display(visible=0, size=(1366, 768))
display.start()
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1366x768")
chrome_options.add_argument('no-sandbox')
chrome_options.add_argument('disable-infobars')
chrome_driver = "/home/jrmtzar/jrm/chromedriver"
def iter_login():
    browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
    browser.get('http://111.93.164.202:8282/CampusPortalSOA/index#/')
    try:
        try:
            time.sleep(1)
            user = browser.find_element_by_xpath("/html/body/div[3]/ng-view/div/div/div/div[2]/form/div[1]/input")
            user.send_keys('1641012112')
        except:
            time.sleep(1)
            user = browser.find_element_by_xpath("//input[@ng-model='ctrl.user.username']")
            user.send_keys('1641012112')
        try:
            time.sleep(1)
            passw = browser.find_element_by_xpath("/html/body/div[3]/ng-view/div/div/div/div[2]/form/div[2]/input")
            passw.send_keys('sikujyoti')
        except:
            time.sleep(1)
            passw = browser.find_element_by_xpath("//input[@ng-model='ctrl.user.password']")
            passw.send_keys('sikujyoti')
        try:
            time.sleep(1)
            but = browser.find_element_by_xpath("/html/body/div[3]/ng-view/div/div/div/div[2]/form/md-input-container/div/button")
            but.click()
        except:
            time.sleep(1)
            but = browser.find_element_by_xpath("//button[@type='submit']")
            but.click()
        try:
            time.sleep(1)
            infbt = browser.find_element_by_xpath("/html/body/div[3]/ng-view/md-content/md-grid-list/md-grid-tile[1]/figure/md-icon")
            infbt.click()
        except:
            time.sleep(1)
            infbt = browser.find_element_by_xpath(
                "/html/body/div[3]/ng-view/md-content/md-grid-list/md-grid-tile[1]/figure")
            infbt.click()
        try:
            time.sleep(1)
            myinfo = browser.find_element_by_xpath(
                "/html/body/div[3]/ng-view/md-content/md-grid-list/md-grid-tile/figure/md-icon")
            myinfo.click()
        except:
            time.sleep(1)
            myinfo = browser.find_element_by_xpath("//md-icon[@md-svg-icon='static/images/MyInfo.svg']")
            myinfo.click()
        try:
            time.sleep(1)
            regnoe = browser.find_element_by_xpath("/html/body/div[3]/ng-view/div[1]/form/md-card[1]/div/div[2]/input")
            regno = regnoe.get_attribute("value")
            namee = browser.find_element_by_xpath("/html/body/div[3]/ng-view/div[1]/form/md-card[1]/div/div[3]/input")
            name = namee.get_attribute("value")
            print("Name : " + name)
        except:
            time.sleep(1)
            regnoe = browser.find_element_by_xpath("//input[@ng-model='StudentInfo.enrollmentno']")
            regno = regnoe.get_attribute("value")
            namee = browser.find_element_by_xpath("//input[@ng-model='StudentInfo.name']")
            name = namee.get_attribute("value")
            print("Name : " + name)
    except:
        print("hauni")




iter_login()



