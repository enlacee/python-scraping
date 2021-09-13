#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ###################
# Read all products from subcategorie
# ###################


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import requests
import sys
# sys.exit()

DRIVER_PATH = './chromedriver'
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

f = open ('02.categories.json', "r")
data = json.load(f)
# print(data)

def generateURLPaginate(IDURL, counter =1):
	itemXpage = 50 # = 50 items
	# start = 0
	limit = (itemXpage*counter) - 1
	start = (limit - itemXpage) + 1

	theURL = "https://www.plazavea.com.pe/api/catalog_system/pub/products/search?fq=C:/" + IDURL + "/&_from="+  str(start) +"&_to=" + str(limit) + "&O=OrderByScoreDESC&"
	return theURL

def buscarTodosLosProductos(IDURL):
	dataStorage = []
	i = 1
	centinela = True
	while centinela == True:
		# recorriendo URL
		theURLJSON = generateURLPaginate(IDURL, i)
		response = requests.get(theURLJSON)
		jsonData = json.loads(response.text)
		# print(len(jsonData))
		print(str(i) + " reading... " + theURLJSON)
		dataStorage.append(jsonData)
		i += 1
		# if i == 2:
		if len(jsonData) == 0:
			centinela = False
	return dataStorage


##########################
## 2 READ SUBCATEGORy
##########################
# 01. read websites

# Each categories
newData = {}
for firstIndex, category in enumerate(data):
	# print(data[str(firstIndex)]["id"])
	category = data[str(firstIndex)];

	newData[firstIndex] = {"id": category['id'],"name": category['name'], "url": category['url'], "image": category['image'], "subcategories": {}}
	listSubCategories = category['subcategories']
	# print(listSubCategories)
	# break

	for secondIndex, category in enumerate(listSubCategories):
		print(secondIndex)
		category = listSubCategories[str(secondIndex)];
		print(category["url"])
		newData[firstIndex]["subcategories"][secondIndex] = {"name": category['name'], "url": category['url'], "image": category['image'], "products": {}}

		# NOW READ PAGE SUBCATEGORIE : WHERE ARE ALL PRODUCTS:
		# theURL = "https://www.plazavea.com.pe/api/catalog_system/pub/products/search?fq=C:/666/906/904/&_from=0&_to=47&O=OrderByScoreDESC&
		driver.get(category["url"])
		scriptText = driver.execute_script("return document.querySelector('head > script:nth-child(43)').text;")
		stringJSON = scriptText[9:-1]; # clean string remove variable=> vtxctx = 
		jsonData = json.loads(stringJSON)
		# categoryId = jsonData['categoryId']
		# print(jsonData)
		buildIDURL = jsonData["departmentyId"] + '/' + data[str(firstIndex)]["id"] + '/' + jsonData["categoryId"]
		# theURL = "https://www.plazavea.com.pe/api/catalog_system/pub/products/search?fq=C:/666/906/904/&_from=0&_to=20&O=OrderByScoreDESC&"
		allProducts = buscarTodosLosProductos(buildIDURL); # print(allProducts)
		newData[firstIndex]["subcategories"][secondIndex]["products"] = allProducts
		# break
	# break

# create file
# 04. write all categories into file JSON: 01.categories.json
with open("03.categories.json", "w") as write_file:
	json.dump(newData, write_file, ensure_ascii=False)


# close browser
driver.close();