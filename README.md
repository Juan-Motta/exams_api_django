# EXAMS API

The application allows users to create and customize exams using a variety of 
question types such as multiple choice, true/false, short answer, and essay 
questions.

The application also provides functionality to manage the entire exam process 
from start to finish. This includes setting up exam schedules, registering 
students for exams, generating exam papers, and managing exam submissions.

## Installation

To install the application the following tools are required

* Python 3.11
* Docker
* PostgreSQL 14
* Redis

:::warning
Hola
:::
All the steps were designed for Linux/MacOS

### Installation without docker

1. Setup environments variables by creating a .env file using .env.example as 
an example and changing the variables according to the database configuration

```
# creates a .env file based on .env.example
cp .env.example .env
```

2. Create a virtual environment using python venv
```
python3 -m venv venv
```

3. Activate a virtual environment
```
source /venv/bin/activate
```

4. Install al the needed dependencies (choose betwen develop or production 
dependencies using develop.txt or production.txt)
```
pip install -r requirements/develop.txt
```

5. Run migrations
```
python3 manage.py migrate
```

6. Run server
```
python3 manage.py runserver
```