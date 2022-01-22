# Flask Tutoring Blog Site


### Part 1. basic Setup

`pip install flask`
to install flask with all necessary modules type:
`pip install flask[all]`

import Flask class from flask module
`From flask import Flask `

create instance of Flask class

`app = Flask(__name__)`

`__name__` means that app instance is in the same(current) module so
app instance will be only accessed in the same file.

while it also use for path reference like all the templates and static files etc will be 
referred from this(path where app instance file located) path.

### Part 2. Templates and Static Files
create `templates` folder in the same project directory.

create `htmls` files and render in from flask app.

Create `static` folder in the same project directory
and all the `css`, `javascripts` and `media` files will
be placed here.

### Part 3. Forms and Validation

### Part 4. Databases

`pip install flask-sqlalchemy`

provide some useful feature for flask

`SQLALCHEMY_DATABASE_URI`
where is database located

`///`   for relative path \
`////`  for absolute path

`def __repr__ ` \
dender method or magic method -> how our object will be printed when we return

`import datetime module for current time`

nullable false as evey post must have an author
relationship are not column, and it runs separate query in background

`backref` -> create another column named author in post table \
`lazy=True`  return the posts' data in one go 

`python` \
`from app import db` \
`db.create_all()` 

from app import User, Post #models
user_1 = User(username="Zubair", email="admin@gmail.com", password="password")

`db.session.add(user_1)`

user_2 = User(username="Zubair", email="admin@gmail.com", password="password")

`db.session.add(user_2)`

`db.session.commit()`

`User.query.all()`

`User.query.first()`

`User.query.filter_by(username='admin').all()`

`User.query.filter_by(username='admin').first()`
`user=User.query.filter_by(username='admin').first()`

`user.id`

`user.posts`
 
`User.query.get(1) # return data with id(condition)`

`user.posts`

`for post in user.posts:
        print(post.title)`
        
        
`post = Post.query.first()`
`post.user_id`

`post.author # backref concept`

`db.drop_all()`

`db.create_all()`

`User.query.all()`

`Post.query.all()`

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