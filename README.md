# Python-scraping

Link source: [scrapingbee](https://www.scrapingbee.com/blog/selenium-python/)
Download and install in your local machine:

[Chrome download page](https://www.google.com/chrome/)
[Chrome driver binary](https://sites.google.com/a/chromium.org/chromedriver/downloads)
selenium package

Scraping with selenium package.  
Requirements: 

	google chrome (v92)
	chromedriver (v92)

	python 3.
	pip
	virtualenv

## development

1. Create virtual enviroment

	virtualenv virtualenv
	source virtualenv/bin/active

2. Create requirements about Current project

	pip3 freeze > requirements.txt  # Python3
	pip freeze > requirements.txt  # Python2

## Execute scrap

	#01. Get all categories (this generate the file: 01.categories)
	python3 main5.py


	#02. Get category and subcategories
	python3 main6.py


The usefull files for consume are:
	
* 01.categories.json `list of all categories`
* 02.categories.json `list of all categories and subcategories`

## image reference

![thumbnail](./docs/Screenshot_20210821_153849.png)

