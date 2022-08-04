## running for development
```bash
python3 manage.py runserver
```

## Running for production
```bash
gunicorn -w 4 entekhab_vahed.wsgi
```