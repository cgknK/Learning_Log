# Learning_Log
Eric Matthes, Python Crash Course 2/e



    A decorator is a directive placed just before a function definition that 
Python applies to the function before it runs, to alter how the function code 
behaves. 
--------
ll_admin 1234
ll_user 1234user
--------
users/template/registiration/ndefault_logged_out.html'i kullanamadım, django'nun
    default views func değiştirmeden
---------
pip freeze > requirements.txt
pip install -r requirements.txt

Biz bağımlılıkları güncellediğimizde bunu tekrar mı oluşturmamız gerekiyor?

---------
python<version> -m venv <virtual-environment-name>

source <virtual-environment-name>/bin/activate
source <virtual-environment-name>/Scripts/activate
source <virtual-environment-name>/Scripts/Activate

deactivate
---------
Kurulum,
 pip install django
 pip install django==2.2*

Proje Oluşturmak,
 django-admin startproject learning_log .

DB Oluşturmak,
 python manage.py migrate
 python manage.py makemigrations

Viewing the Project,
 python manage.py runserver
 python manage.py runserver 8001
 python manage.py runserver 8002
 ... _Neden yukarı doğru deniyoruz?

Starting an App,
 python manage.py startapp learning_logs

Setting Up a Superuser,
 python manage.py createsuperuser

Django Shell,
 python manage.py shell
----------------------------------