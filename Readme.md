## Backend Setup with Django

This guide details setting up a Django backend for your web application.

### Prerequisites:

- Python 3.x installed (https://www.python.org/downloads/)
- A code editor or IDE of your choice (e.g., Visual Studio Code, PyCharm)
### 1. Activate Virtual Environment

### - Windows:
```Bash
.\venv\Scripts\activate
```

### Linux/macOS:
```Bash
source ./venv/bin/activate
```

Replace ./venv with the actual path to your virtual environment if it's located elsewhere.

### 2. Install Dependencies

- Ensure you have a requirements.txt file listing project  dependencies.

- Run the following command to install them:

```Bash
pip install -r requirements.txt
```

3. Set Up Models

- Navigate to the directory containing your Django project's manage.py file:

```Bash
cd backend
```
- Create or modify your models in the models.py file within your app directory.

### 4. Run Database Migrations

- Apply database schema changes based on model definitions:

```Bash
python manage.py makemigrations
python manage.py migrate
```
- makemigrations generates migration files reflecting model changes.
- migrate applies those changes to the database.
### 5. Start the Development Server

- Run the following command to launch the Django development server:

```Bash
python manage.py runserver
```
- This creates a local development server accessible by default at http://127.0.0.1:8000/ in your web browser.

### Frontend Setup

1. Navigate to your frontend project's directory.

2. Install dependencies using either npm or yarn:

### - npm:
```Bash
npm install
npm run dev
```
### - yarn:
```Bash
yarn install
yarn run dev
```


