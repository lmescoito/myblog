estrutura do Projeto

mysite/
├── mysite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── blog/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py  # Ensure this file exists
│   ├── views.py
│   ├── templates/
│   │   └── home.html  # Ensure this exists if your view renders a template
│   └── migrations/
│       └── __init__.py
└── manage.py
