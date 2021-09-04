#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import requests


DRIVER_PATH = './chromedriver'
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

# 01. read websites
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://www.plazavea.com.pe/libreria-y-oficina")

# 02. read content (search ID category)
scriptText = driver.execute_script("return document.querySelector('head > script:nth-child(43)').text;")
stringJSON = scriptText[9:-1];

jsonData = json.loads(stringJSON)
categoryId = jsonData['categoryId']

# 03. build URL JSON
URLJSONCategory = 'https://www.plazavea.com.pe/files/' + categoryId + '_data.json'
response = requests.get(URLJSONCategory)
categoryJsonData = json.loads(response.text)
listCategories = categoryJsonData['content'][1]['values']
data = []
for category in listCategories:
	urlIMG = "https://plazavea.vteximg.com.br/arquivos/" + category['image'] + '.' + category['image_format']
	data.append({"name": category['name'], "url": category['url'], "image": urlIMG})

# 04. write all categories into file JSON: 01.categories.json
with open("01.categories.json", "w") as write_file:
	json.dump(data, write_file, ensure_ascii=False)


# close browser
driver.close();