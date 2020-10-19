from selenium import webdriver
# import geckodriver_autoinstaller
import time
import random
from selenium.webdriver.firefox.options import Options
options = Options()
options.headless = True
# path = geckodriver_autoinstaller.install()
# driver = webdriver.Firefox(executable_path=path, options=options)
driver = webdriver.Firefox(options=options)




id = input("input ur id: ")
a = input("input a fake name: ") 
driver.get('https://www.kahoot.it')

while True:
    time.sleep(3)
    i = str(random.randrange(1,100))
    # time.sleep(2)
    search = driver.find_element_by_xpath('''//*[@id="game-input"]''')
    search.click()
    search.send_keys(id)
    btn = driver.find_element_by_xpath('''//*[@id="root"]/div/div/div/main/div/form/button''')
    btn.click()
    time.sleep(5)
    name = driver.find_element_by_xpath('''//*[@id="nickname"]''')
    name.click()
    name.send_keys(a+i)
    enter = driver.find_element_by_xpath('''//*[@id="root"]/div/div[1]/div/main/div/form/button''')
    enter.click()
    driver.execute_script('''window.open("https://www.kahoot.it");''') # to a start new tab
    driver.switch_to.window(driver.window_handles[-1]) # shifting focus to the new tab
