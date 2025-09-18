# SKTaskMgmt-BackEnd
Python Backend for SimonChaela Task Mgmt. Built using Django.

PYTHON VERSION: 3.13.7

---
To Update Requirements.txt:
pip freeze > requirements.txt

To Run DB Migrations:
python manage.py makemigrations
python manage.py migrate

---
Steps to Run:
1. Create and activate virtual environment
    - python -m venv venv
    - source venv/bin/activate (Linux/Mac)
    - .\venv\Scripts\activate (Windows PowerShell)

2. Install dependencies
   - pip install -r requirements.txt

3. Run migrations (sets up the database)
   - python manage.py migrate

4. Start the development server
    - python manage.py runserver

5. When finished
    - deactivate
