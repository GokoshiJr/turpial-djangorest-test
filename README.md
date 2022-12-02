# turpial-djangorest-test

## Specifications and Develop Enviroment
- python: v3.10.8 <br/>
- mysql manager (xampp): v8.0.11 <br/>
- postman: v10.5.2 <br/>
- commits standard: https://www.conventionalcommits.org/en/v1.0.0/

## Install

### 1. Clone repo
```git
git clone https://github.com/GokoshiJr/turpial-djangorest-test.git
```

### 2. Move to dir
```bash
cd turpial-djangorest-test
```

### 3. Create python enviroment (Windows)
```bash
python -m venv env
```

### 4. Activate enviroment (Windows)
```bash
env\Scripts\activate
```

### 5. Install dependencies 
```bash
pip install -r requirements.txt
```

### 6. Run your mysql service, in this case xampp, activate service in the control panel

### 7. Create a empty database in mysql

### 8. Create .env file in this route app/app/.env with this fields (example)
DB_NAME=your_db_name <br/>
DB_HOST=your_db_host <br/>
DB_PORT=your_db_port <br/>
DB_USER=your_db_user <br/>
DB_PASSWORD=your_db_password

### 9. Migrate (located in app/ to execute this command)
```bash
python manage.py migrate
```

### 10. Create superUser to ApiAuth requests
```bash
python manage.py createsuperuser --email admin@example.com --username admin
```

### 11. Run server
```bash
python manage.py runserver
```
### 12. (IMPORTANT) To fill the database, do a GET request in this url localhost:8000/seed/
