# Burgerzilla Hamburger Ordering System Project for Yemeksepeti
## Overview

Taking orders from hamburger restaurants, with the order, which can view the status of the order Transactions under the authority of the relevant customer/restaurant A REST-API microservice that enables.

### Most Common Python and Flask Libraries
```
- Flask-SQLAlchemy

- Flask-Migrate

- flask-restx

- Werkzeug

- psycopg2-binary

- flask-marshmallow
```
Before we begin, kindly install following on your system:-

-   [python3.x](http://www.python.org)
-   [Virtualenv](https://virtualenv.pypa.io/en/stable/)

How to Run the App?
-------------------

-   Git clone 
```
<https://github.com/Yemeksepeti-Python-Bootcamp/BurgerZilla_onurakyol.git>
```
-   Open the terminal and run,
```
docker build -t burgerzilla-main:latest .
```
-   After that run this code,
```
docker compose up --build web
```
-   You can reach all API documentation from Postman Collection

Everything should be ready. In your browser open
<http://127.0.0.1:5000/>

Customer Endpoints
-------------------

|Method|Endpoint|Description|      
|----|-----|-------|      
|GET|127.0.0.1:5000/client/Restaurants|Get all restaurants| 
|GET|127.0.0.1:5000/client/Menu/menuId|Get menu with menuId|
|POST|127.0.0.1:5000/client/createOrder|Create an hamburger order|
|POST|127.0.0.1:5000/client/watchOrders|Watch the order|
|GET|127.0.0.1:5000/client/getAllOrder/userid|Shows order with <userid>|
|GET|127.0.0.1:5000/client/cancelOrder/orderid|Cancel your order with <orderid>|

Restaurant Endpoints
-------------------
|Method|Endpoint|Description|      
|----|-----|-------|      
|GET|127.0.0.1:5000/admin/getAllOrder/restaurant_id|Get all orders| 
|GET|127.0.0.1:5000/admin/getOrderDetail/order_id|Get order details|
|GET|127.0.0.1:5000/admin/cancelOrder/order_id|Cancel selected order|
|POST|127.0.0.1:5000/admin/updateContent/selected_order_id|Update the status of order| 
|GET|127.0.0.1:5000/admin/getMenu/restaurant_id|Get the menu content| 
|GET|127.0.0.1:5000/admin/getSelectedContent/content_id|Get details of the selected content| 
|POST|127.0.0.1:5000/admin/updateSelectedContent/content_id|Update the menu| 
|POST|127.0.0.1:5000/admin/addContent/restaurant_id|Add new element to the menu| 
|POST|127.0.0.1:5000/admin/deleteContent/content_id|Delete any element of the menu| 

Authentication Endpoints
-------------------
|Method|Endpoint|Description|      
|----|-----|-------|      
|POST|127.0.0.1:5000/auth/Register|Register the new user| 
|POST|127.0.0.1:5000/auth/Login|Login for user| 
|GET|127.0.0.1:5000/api/username|Show datas for user| 

DB Schema
-------------------
![alt text](https://imgyukle.com/f/2022/02/14/EoiPzc.png)

Folders
-------------------
```
burgerzilla-main
├─ app
│  ├─ api
│  │  ├─ datasets
│  │  │  ├─ controller.py
│  │  │  ├─ dto.py
│  │  │  ├─ service.py
│  │  │  ├─ utils.py
│  │  │  └─ __init__.py
│  │  ├─ musteri
│  │  │  ├─ clientService.py
│  │  │  ├─ controller.py
│  │  │  └─ dto.py
│  │  ├─ restorant
│  │  │  ├─ controller.py
│  │  │  ├─ dto.py
│  │  │  └─ restorantService.py
│  │  ├─ user
│  │  │  ├─ controller.py
│  │  │  ├─ dto.py
│  │  │  ├─ service.py
│  │  │  ├─ utils.py
│  │  │  └─ __init__.py
│  │  └─ __init__.py
│  ├─ auth
│  │  ├─ controller.py
│  │  ├─ dto.py
│  │  ├─ service.py
│  │  ├─ utils.py
│  │  └─ __init__.py
│  ├─ extensions.py
│  ├─ models
│  │  ├─ dataset.py
│  │  ├─ schemas.py
│  │  ├─ user.py
│  │  └─ __init__.py
│  ├─ utils.py
│  ├─ Yemeksepeti.postman_collection.json
│  └─ __init__.py
├─ boot.sh
├─ config.py
├─ data-dev.sqlite
├─ docker-compose.yml
├─ Dockerfile
├─ README.md
├─ requirements.txt
├─ runservice.py
└─ tests
   ├─ test_auth_api.py
   ├─ test_client_api.py
   ├─ test_config.py
   ├─ test_restaurant_db.py
   ├─ test_user_api.py
   ├─ test_user_model.py
   └─ utils
      ├─ base.py
      ├─ common.py
      └─ __init__.py
```# BurgerOrderSystem
