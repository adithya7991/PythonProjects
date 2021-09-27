# Store API Project
## Installation
### Using PIP
```
1. pip install Flask
2. pip install Flask-Restful
3. pip install Flask-JWT
4. pip install Flask-SQLAlchemy
```
### Using requirements.txt
```
pip install -r requirements.txt
```
## Description
This is a Store API project created based on REST principles and flask-jwt is used for user authentication and session management.
For database, SQlite 3 is used and Object relational mapper is used to perform operations on DB.
Below are the list of APIs exposed:

Method | Endpoint
------ | --------
POST   | /register
POST   | /login
POST   | /store
GET    | /store/name
GET    | /stores
DEL    | /store/name
POST   | /item
PUT    | /item/name
GET    | /item/name
GET    | /items
DEL    | /item/name

## Run
```
python app.py
```
