#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import requests
import numpy as np


DRIVER_PATH = './chromedriver'
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

# 01. read websites
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
# driver.get("https://www.plazavea.com.pe/libreria-y-oficina")

f = open ('01.categories.json', "r")
data = json.load(f)

##########################
## 2 READ SUBCATEGORy
##########################
# 01. read websites
newData = {}
for firstIndex, category in enumerate(data):
	driver.get(category["url"])
	scriptText = driver.execute_script("return document.querySelector('head > script:nth-child(43)').text;")
	stringJSON = scriptText[9:-1];
	jsonData = json.loads(stringJSON)
	categoryId = jsonData['categoryId']

	# 03. build URL JSON
	URLJSONCategory = 'https://www.plazavea.com.pe/files/' + categoryId + '_data.json'
	print(firstIndex)
	print(URLJSONCategory)

	response = requests.get(URLJSONCategory)
	categoryJsonData = json.loads(response.text)
	listSubCategories = categoryJsonData['content'][1]['values']

	newData[firstIndex] = {"name": category['name'], "url": category['url'], "image": category['image'], "subcategories": {}}
	
	for secondIndex, category in enumerate(listSubCategories):
		urlIMG = "https://plazavea.vteximg.com.br/arquivos/" + category['image'] + '.' + category['image_format']
		newData[firstIndex]["subcategories"][secondIndex] = {"name": category['name'], "url": category['url'], "image": urlIMG}


# create file
# 04. write all categories into file JSON: 01.categories.json
with open("02.categories.json", "w") as write_file:
	json.dump(newData, write_file, ensure_ascii=False)


# close browser
driver.close();


