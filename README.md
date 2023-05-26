# Learning_Log
Eric Matthes, Python Crash Course 2/e

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