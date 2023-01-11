# Django + Aiogram

## 1. Using the template

- Create new repository using this template

![Use this template](./use-template.png)

- And clone your repository

```sh
git clone https://github.com/<username>/<repo_name>.git
```

- Go project path

```sh
cd <repo_name>
```

## 2. Create virtualenv and activate

```sh
python3 -m virtualenv venv
source venv/bin/activate
```

## 3. Install required packages

```sh
pip install -r requirements.txt
```

## 4. Create ```.env``` file using env template file and fill it

```sh
cp .env.template .env
```

## 5. Run django project

- Migrations

```sh
python manage.py migrate
```

- Run server

```sh
python manage.py runserver
```

## 6. Run aiogram project

```sh
python manage.py runbot
```
