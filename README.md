# Flask Tutoring Blog Site


### Part 1. basic Setup

### Part 2. Templating

### Part 3. Forms and Validation

### Part 4. Databases

pip install flask-sqlalchemy

provide some useful feature for flask

SQLALCHEMY_DATABASE_URI
where is database located

///   for relative path
////  for absolute path

def __repr__ 
dender method or magic method -> how our object will be printed when you printed

import datetime module for current time

nullable false as evey post must have an author
relationship are not column and it run separate query in background

backref -> create another column named author in post table
lazy -> return the posts data in one go 

python
from app import db
db.create_all()

from app import User, Post #models
user_1 = User(username="Zubair", email="admin@gmail.com", password="password")

db.session.add(user_1)

user_2 = User(username="Zubair", email="admin@gmail.com", password="password")

db.session.add(user_2)

db.session.commit()

User.query.all()
User.query.first()
User.query.filter_by(username='admin').all()
User.query.filter_by(username='admin').first()
user=User.query.filter_by(username='admin').first()
user.id
user.posts
 
User.query.get(1) # return data with id (condition)

user.posts
for post in user.posts:
        print(post.title)
        
        
post = Post.query.first()
post.user_id

post.author # backref concept

db.drop_all()
db.create_all()

User.query.all()
Post.query.all()

Error
circular import error

tree module to print architecture of app




### Part 5. Package-Structure

circular error

just create models and it will show import error so it give error at User import

from __main__ import db gives error at db import



### Part 6. Login-Auth
pip install flask-login \
pip install email-validator \
from flask_login import LoginManager

### Part 7. User-Account-Profile-Picture

### Part 8. Posts

### Part 9. Likes and Comments

### Part 10. Pagination

### Part 11. Password-Reset-Email