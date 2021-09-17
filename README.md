# Python-scraping

Scrap all products from the website: [www.plazavea.com.pe Libreria y Oficina](https://www.plazavea.com.pe/libreria-y-oficina)

## Requirements: 

Download and install in your local machine: 

 1. [Chrome download page](https://www.google.com/chrome/)  
 2. [Chrome driver binary](https://sites.google.com/a/chromium.org/chromedriver/downloads) download and copy here  

Software:

	google chrome (v92)
	chromedriver (v92)

Packages:

	python 3
	pip
	virtualenv

## Development

Once inside the folder  <project-name>  
Execute the follow comands:

	virtualenv -p python3 virtualenv
	source virtualenv/bin/active
	pip install -r requirements.txt # install all packages

## Execute scrap helper

	#01. Get all categories (this generate the file: 01.categories)
	python3 main5.py

	#02. Get category and subcategories
	python3 main6.py

## Execute Main scrap dynamic for all products

	# Get all products
	python3 main7.py

The result is saved in the file named **03.categories.json** `there are all all products`

## image reference

![thumbnail](./docs/Screenshot_20210821_153849.png)




Source: [scrapingbee](https://www.scrapingbee.com/blog/selenium-python/)

