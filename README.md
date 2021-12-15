# TheWasteHunter

## GETTING STARTED

- Install and set-up Virtual environment
```shell
python -m venv venv/
pip install -r requirements.txt

```
- Then set up environmental variable and required migrations

`For Linux Users`
```shell
export FLASK_APP=waste_hunter
export FLASK_ENV=development
flask db init
flask db migrate
flask db upgrade

```

`For Windows Users`
```shell
set FLASK_ENV=waste_hunter
set FLASK_ENV=development
flask db init
flask db migrate
flask db upgrade
```

- To run the app
```shell
flask run
```
NB:
For contributors to the `HTML,CSS,JS`, only access the `templates` and `static` folders