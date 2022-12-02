# turpial-djangorest-test

## Specifications and Develop Enviroment
- python: v3.10.8 <br/>
- mysql manager (xampp): v8.0.11 <br/>
- postman: v10.5.2 <br/>
- commits standard: https://www.conventionalcommits.org/en/v1.0.0/

## Install

### Clone repo
```git
$ git clone https://github.com/GokoshiJr/turpial-djangorest-test.git
```

### Move to dir
```bash
$ cd turpial-djangorest-test
```

### Create python enviroment (Windows)
```bash
$ python -m venv env
```

### Activate enviroment (Windows)
```bash
$ env\Scripts\activate
```

### Install dependencies 
```bash
$ pip install -r requirements.txt
```

### Run your mysql service, in this case xampp, activate service in the control panel

### Create a empty database in mysql

### Create .env file in this route app/app/.env with this fields (example)
DB_NAME=your_db_name <br/>
DB_HOST=your_db_host <br/>
DB_PORT=your_db_port <br/>
DB_USER=your_db_user <br/>
DB_PASSWORD=your_db_password

### Make migrations (located in app/ to execute this command)
```bash
$ python manage.py makemigrations
```

### Migrate
```bash
$ python manage.py migrate
```

### Create superUser to ApiAuth requests
```bash
$ python manage.py createsuperuser --email admin@example.com --username admin
```

### Run server
```bash
$ python manage.py runserver
```
