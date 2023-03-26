# Django + Aiogram

## 1. Create virtualenv and activate

```sh
python3 -m virtualenv venv
source venv/bin/activate
```

## 2. Install required packages

```sh
pip install -r requirements.txt
```

## 3. Create ```.env``` file using env template file and fill it

```sh
cp .env.template .env
```

## 4. Run django project

- Migrations

```sh
python manage.py migrate
```

- Run server

```sh
python manage.py runserver
```

## 5. Run aiogram project

```sh
python manage.py runbot
```
