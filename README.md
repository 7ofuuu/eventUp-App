# EventUp SMK Negeri 4 Bandung

<div>
<img src="https://i.ibb.co/MnCQZS4/eventup4.png" width=427px>
</div>

<br><br>

### Clone it locally via cmd/git bash... just don't powershell
*must use python version 3.8.10
```cmd
# clone
git clone https://github.com/7ofuuu/eventUp-app.git
git checkout development

# create and activate virtual environment
python -m venv venv
venv\Scripts\activate           #windows

# install dependencies
pip install -r requirements.txt

# set environment variable
copy .env.template .env         #cmd
cp .env.example .env            #git bash
configure .env file

# skip it if not change the database
python manage.py makemigrations
python manage.py migrate

# run project
python manage.py runserver
```

<br>
the passwords of all sample users are:

```
Zp2a-SrJ
```
