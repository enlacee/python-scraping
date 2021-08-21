from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = './chromedriver'

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://anibalcopitan.com/#/")

## Select path > html
h2 = driver.find_element_by_xpath('//*[@id="head-svg-man"]/h2') 

# print values
# print(dir(h1));
# print(dir(driver));

print("######## WEBSITE  SCRAPING ########")
print("URL: " + driver.current_url)
print("###################################")
print(".")
print("..")
print("...")
print(h2.text)

# print(driver.page_source)
# print(driver.title)
driver.quit()

