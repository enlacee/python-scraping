## development

1. Create virtual enviroment

	virtualenv -p python3 virtualenv

	virtualenv virtualenv
	source virtualenv/bin/active

	# install all packages
	pip install -r requirements.txt

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