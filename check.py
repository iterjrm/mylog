import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1366x768")
chrome_driver = "chromedriver"
def iter_login():
    browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
    browser.get('http://111.93.164.202:8282/CampusPortalSOA/index#/')
    try:
        user = browser.find_element_by_xpath("/html/body/div[3]/ng-view/div/div/div/div[2]/form/div[1]/input")
        user.send_keys('1641012112')
        passw = browser.find_element_by_xpath("/html/body/div[3]/ng-view/div/div/div/div[2]/form/div[2]/input")
        passw.send_keys('sikujyoti')
        but = browser.find_element_by_xpath("/html/body/div[3]/ng-view/div/div/div/div[2]/form/md-input-container/div/button")
        but.click()
        time.sleep(2)
        infbt = browser.find_element_by_xpath("/html/body/div[3]/ng-view/md-content/md-grid-list/md-grid-tile[1]/figure/md-icon")
        infbt.click()
        time.sleep(1)
        myinfo = browser.find_element_by_xpath("/html/body/div[3]/ng-view/md-content/md-grid-list/md-grid-tile/figure/md-icon")
        myinfo.click()
        time.sleep(1)
        regnoe = browser.find_element_by_xpath("/html/body/div[3]/ng-view/div[1]/form/md-card[1]/div/div[2]/input")
        regno = regnoe.get_attribute("value")
        namee = browser.find_element_by_xpath("/html/body/div[3]/ng-view/div[1]/form/md-card[1]/div/div[3]/input")
        name = namee.get_attribute("value")
        print("Name : "+name)



    except:
        user = browser.find_element_by_xpath("/html/body/div[3]/ng-view/div/div/div/div[2]/form/div[1]/input")
        user.send_keys('1641012112')
        passw = browser.find_element_by_xpath("/html/body/div[3]/ng-view/div/div/div/div[2]/form/div[2]/input")
        passw.send_keys('sikujyoti')
        time.sleep(1)
        but = browser.find_element_by_xpath("/html/body/div[3]/ng-view/div/div/div/div[2]/form/md-input-container/div/button")
        but.click()
        time.sleep(2)
        infbt = browser.find_element_by_xpath("/html/body/div[3]/ng-view/md-content/md-grid-list/md-grid-tile[1]/figure/md-icon")
        infbt.click()
        time.sleep(1)
        myinfo = browser.find_element_by_xpath("/html/body/div[3]/ng-view/md-content/md-grid-list/md-grid-tile/figure/md-icon")
        myinfo.click()
        time.sleep(1)
        regnoe = browser.find_element_by_xpath("/html/body/div[3]/ng-view/div[1]/form/md-card[1]/div/div[2]/input")
        regno=regnoe.get_attribute("value")
        namee= browser.find_element_by_xpath("/html/body/div[3]/ng-view/div[1]/form/md-card[1]/div/div[3]/input")
        name = namee.get_attribute("value")



    



iter_login()
