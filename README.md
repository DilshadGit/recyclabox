# recyclabox
Test

# Creat venv and install following 
	## pip install django==2.2.15
	## pip install djangorestframework
# Create Project and apps:
	## Create class for Item with following fields as in the assignment:
	### name, qty, price,  sku 


API Endpoints
	- CRUD 
	- List & Search

2. HTTP methods
	- GET, POST, PUT, PATCH, DELETE

3. Data Types & Validation
	- JSON --> Serializer
	- Validation --> Serializer

1. Register a product
	User can register product as item
	display list of the item 
	search item 
	Ordering all fields in both way ascending and descending using filder
2. Retrieve Product detail from SKU
	This is not done because not sue how to setup SKU like IEM number or select 3 digit or character from each field and be unique?
3. List all available product qty > 0 done using filter
4. List all product sold out or qty is 0, display products that 0 qty serach qty as ascending
5. Register qty change sku (-/+, values) not sure what they means?

Key Object:
1. Consistance in memory ?
2. Industry-complain API REST Endpoint done.
3. Dockerized envirement, have tried how to write docker but I am not expert.

Stretch Goal:
1. Automated Test Done but the post item get an error because of user is instance !
2. Documentation, Do you mean README file?
3. Data Presistance ?

Notce:
Create user and login to display API.