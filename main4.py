from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains

DRIVER_PATH = './chromedriver'

options = Options()
# options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://www.plazavea.com.pe/libreria-y-oficina")
# time.sleep(2)
# wait = WebDriverWait(driver, 10)


## Select path > html
h2 = driver.find_element_by_xpath('//*[@id="root"]/header/div[3]/div/div/div[1]/div')
h2.click()

# time.sleep(2)

sub = driver.find_element_by_xpath('//*[@id="root"]/header/section/div/div[2]/div[2]/ul/li[14]/a')
# actions.moveToElement(sub);

actions = ActionChains(driver)
actions.move_to_element(sub)
actions.click(sub)
actions.perform()

# sub.click()

subsub = driver.find_element_by_xpath('//*[@id="root"]/header/section/div/div[2]/div[4]/div[2]')


# print values
# print(dir(h1));
# print(dir(driver));

print("######## WEBSITE  SCRAPING ########")
print("URL: " + driver.current_url)
print("###################################")
print(".")
print("..")
print("...")
print(sub.text)
print("...")
print(subsub.text)
# print(dir(h2))


# print(driver.page_source)
# print(driver.title)
# driver.quit()

