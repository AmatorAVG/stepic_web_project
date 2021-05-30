sudo /etc/init.d/mysql start
mysql -uroot -e "create database stepic_web;" && mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"
sudo apt-get -y install lynx
python3 manage.py makemigrations qa
python3 manage.py migrate
python3 manage.py createsuperuser