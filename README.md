# Simple Pizza ordering application

## Installation
* Clone repository  
* Install requirements  
* Create database user 'django'  
* Create database(if not exist) 'pizza_db' or update settings.py  
* Enjoy :tada:

## --NOTE--
Create superuser and add some pizzas from admin panel  


# Models

## Pizza
*Name(charfield): name of pizza, e.g. Pepperoni, Margarita, Quattro Formagio

## Customer
*first_name(charfield): customer first name, e.g. John  
*last_name(charfield): customer last name, e.g. Smith  
*email(unique charfield): customers email, e.g john.smith@gmail.com  

## Order
*customer(ForeignKey): foreign key on Customer model  
*pizza(ForeignKey): foreign key on Pizza model  
*address(charfield): address of delivery, e.g. "21 Jump Street"  
*size(choicefield): the size of ordere pizza, e.g. large(50cm) or small(30cm)  

# API
*Customers(CRUD), example: localhost:8000/customers/  
*Orders(CRUD), example: localhost:8000/orders/  
