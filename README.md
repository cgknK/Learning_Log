# Learning_Log
Eric Matthes, Python Crash Course 2/e

--------
e-mail ve robot kontrolü ile spam veya bot kayıtlarına önlem al.
--------
En son projeye; base.html'e json.dump butonu ekle ve veri tabanını indir, 
yapılabiliniyor ise dosyayı geri db'ye çevir.
--------
NOTE
You can simply reset the database instead of migrating, but that will lose all
existing data. It’s good practice to learn how to migrate a database while
maintaining the integrity of users’ data. If you do want to start with a fresh
database, issue the command python manage.py flush to rebuild the database
structure. You’ll have to create a new superuser, and all of your data will be
gone.
--------
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