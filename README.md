# Python-scraping

Link source: [scrapingbee](https://www.scrapingbee.com/blog/selenium-python/)
Download and install in your local machine:

[Chrome download page](https://www.google.com/chrome/)
[Chrome driver binary](https://sites.google.com/a/chromium.org/chromedriver/downloads) download and copy here

	cp ~./Downloads/chromedriver .

## Requirements: 

	google chrome (v92)
	chromedriver (v92)

	python 3.
	pip
	virtualenv

## Development
Once inside the folder  <project-name>  
Execute the follow comands:

	virtualenv -p python3 virtualenv
	source virtualenv/bin/active
	pip install -r requirements.txt # install all packages

## Execute scrap

	#01. Get all categories (this generate the file: 01.categories)
	python3 main5.py

	#02. Get category and subcategories
	python3 main6.py

	#03. Get all products
	python3 main7.py


The usefull files for consume are:
	
* 01.categories.json `list of all categories`
* 02.categories.json `list of all categories and subcategories`
* 03.categories.json `list of all products`

## image reference

![thumbnail](./docs/Screenshot_20210821_153849.png)

