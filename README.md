README.md
=========

This is a web server used to control and monitor the op-box remotely. Idealy, this machine would be air-gapped. But if telemetry is necessary, and you can not run cables to the experiment room, you could run this on a secure wifi network. There is no reason to ever connect this to the internet while the server is running. 

Install Django
--------------
https://docs.djangoproject.com/en/1.9/topics/install/

Clone this Repository
---------------------

    git clone https://github.com/BlazigatorBros/OpBoxWebsite.git
    cd OpBoxWebsite
    
Update Submodules
-----------------
    cd OpBoxWebsite/OpBoxLib
    git pull
    cd ../..

Create Admin User
-----------------
only superusers can run arbitraty scripts

    python manage.py createsuperuser

Run Server
----------
    python manage.py runserver
