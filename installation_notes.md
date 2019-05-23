# Installation Notes #

These are all the steps it took to get NEMO up and running on Ubuntu with PostgresSQL. Many thanks to [@SolitonMan](https://github.com/SolitonMan/) for all his help.

---

1. Created a new VM, installed Ubuntu 18.04.2 LTS
1. During installation selected option to install Docker
1. Installed PostgreSQL with `sudo apt install postgresql postgresql-contrib`
1. Changed to postgres user with `sudo su - postgres` and created a database and user (see: https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04) and exited out of postgres user.
1. Modified /etc/postgresql/10/main/postgresql.conf, set `listen_addresses = '0.0.0.0'` (see: https://www.postgresql.org/docs/current/runtime-config-connection.html)
1. Modified /etc/postgresql/10/main/pg_hba.conf, added lines for host connection to 10.0.0.70/32 (current public IP) and 127.17.0.0/24 (IP range used by docker) (see: https://www.postgresql.org/docs/9.1/auth-pg-hba-conf.html)
1. In my home directory (~) cloned the repo with `git clone https://github.com/lurienanofab/NEMO.git` (forked from the original NIST repo), which created the NEMO directory in my home folder
1. Replaced ~/NEMO/Dockerfile with https://github.com/SolitonMan/NEMO/blob/master/Dockerfile, which is slightly modified from the original NIST version for using PostgreSQL
1. Created directory ~/nemo_runtime. Here I created the folder structure and settings.py file as described in the wiki (https://github.com/usnistgov/NEMO/wiki/Installation-with-Docker)
1. Copied the settings.py from the NIST wiki to ~/nemo_runtime/settings.py, changing appropriate values (emails, ldap and email hosts, etc) and modified the DATABASES setting to:
```python
DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'xxxxx',
                'USER': 'xxxxx',
                'PASSWORD': 'xxxxx',
                'HOST': '10.0.0.70',
                'PORT': '5432',
        }
}
```
11. In ~/NEMO (repository root) I ran the command `sudo docker build -t lnf/nemo -f Dockerfile .`
12. Ran the following commands according to the NIST wiki:
* Collect static files: `sudo docker run --volume ~/nemo_runtime:/nemo lnf/nemo django-admin collectstatic`
* Create the database: `sudo docker run --volume ~/nemo_runtime:/nemo lnf/nemo bash -c "django-admin makemigrations NEMO && django-admin migrate"`
* Create a super user: `sudo docker run --interactive --tty --volume ~/nemo_runtime:/nemo lnf/nemo django-admin createsuperuser`
* Running NEMO in Docker: `sudo docker run --detach --publish 8000:8000 --volume ~/nemo_runtime:/nemo lnf/nemo`
13. Coming soon... configure ngnix reverse proxy
