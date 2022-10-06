

### What we are building?
We are Building an API with high performance built with 
- FastAPI & SQLAlchemy, 
help to improve connection with your Backend Side to create a simple blog and Cruds with OAuth2PasswordBearer ⛏

Creating an API with high performance built with 
- FastAPI & SQLAlchemy, 
helps to improve connection with your Backend Side and stay relate using 
- SQLite3 & 
a secure Schema Based on Python-Jose a JavaScript Object Signing and Encryption implementation in Python.


### python-jose
The `JavaScript Object Signing and Encryption (JOSE)` technologies 
    - JSON Web Signature (JWS), 
    - JSON Web Encryption (JWE), 
    - JSON Web Key (JWK), and 
    - JSON Web Algorithms (JWA) - 
collectively can be used to encrypt and/or sign content using a variety of algorithms. While the full set of permutations is extremely large, and might be daunting to some, it is expected that most applications will only use a small set of algorithms to meet their needs.


### pipenv
Pipenv: Python Development Workflow for Humans

`Pipenv` is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world.

It automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile as you install/uninstall packages. It also generates the ever-important `Pipfile.lock`, which is used to produce deterministic builds.
 - sudo apt install pipenv


#### creating pipenv environment for python 3
 - $ pipenv --three

- activating the pipenv environment
 - $ pipenv shell

#### if you have multiple python 3 versions installed then
 - $ pipenv install -d --python 3.10.4

- install all dependencies (include -d for installing dev dependencies)
 - $ pipenv install -d


### Database :
To Provide a good and fast work, I choose 
- SQLAlchemy as a toolkit and performance, 
for the Database I choose 
- SQLite a High performance Database and full of Features.

If you want to configure the Database with an other Provider like 
- MySQL or 
- PostgreSQL you can change the Database_URL here in the `configuration.py` file:
#here you need to inster the  URI that should be used for the connection.
```SQLALCHEMY_DATABASE_URL = 'sqlite:///blog.db'```

for e.g
```SQLALCHEMY_DATABASE_URL = 'mysql://username:password@server/blog'```


### Models :
Here in the `models.py`, we are gonna create 2 tables based on the requirements related to this project blogs and users.


### Schemas
- Here we are declaring 
    - `Blogs` and 
    - `Users` and 
    - `Token models`, 
it will contain all format `int` or `string` or `bool`, lets code this on our `schemas.py`.


### API :
Now we need to code the Main API and create the Queries with a hashed Password for the Users using Bcrypt.
- `bcrypt` : bcrypt allows building a password security platform that can evolve alongside hardware technology to guard against the threats that the future may bring, such as attackers having the computing power to crack passwords twice as fast.


### Core :
In this folder we gonna Create 3 files 
- `Auth.py` and 
- `Blog.py` and 
- `User.py`, all of this files are the routes for our API.
We Start by User.py, where we Create a routes for create_user, get_users, get_user_by_id.


























