
# Sistema OMAPED | MPSM

Sistema de gestion de beneficiarios de la oficina de omaped de la Municipalidad Provincial de San Martin

Desarrollado con python en el framework Django, usando plantillas Argon

## 🚀 About Me
I'm a full stack developer in python, django
ronald_perez86@hotmail.com


Tarapoto - Peru - 2023


usuario: admin

password: Admin2023@

## Deployment

To deploy this project run

git clone https://github.com/eperezd/omaped-mpsm2023.git


Virtualenv modules installation (Windows based systems)

virtualenv env

.\env\Scripts\activate

Install modules - SQLite Storage

pip3 install -r requirements.txt

Create tables

python manage.py makemigrations


python manage.py migrate

Access the web app in browser: http://127.0.0.1:8000/