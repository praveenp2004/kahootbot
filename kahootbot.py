from selenium import webdriver
#import geckodriver_autoinstaller
import time
import random
from selenium.webdriver.firefox.options import Options
options = Options()
options.headless = True
#path = geckodriver_autoinstaller.install()
#driver = webdriver.Firefox(executable_path=path, options=options)
driver = webdriver.Firefox(options=options)



id = input("input ur id:")
driver.get('https://www.kahoot.it')
while True:
    time.sleep(3)
    i = str(random.randrange(1,100))
    search = driver.find_element_by_xpath('''//*[@id="game-input"]''')
    search.send_keys(id)
    btn = driver.find_element_by_xpath('''//*[@id="root"]/div/div/div/main/div/form/button''')
    btn.click()
    time.sleep(4)
    name = driver.find_element_by_xpath('''//*[@id="nickname"]''')
    name.send_keys("bots"+i)
    enter = driver.find_element_by_xpath('''//*[@id="root"]/div/div/div/main/div/form/button''')
    enter.click()
    driver.execute_script('''window.open("https://www.kahoot.it");''')
    driver.switch_to.window(driver.window_handles[-1])