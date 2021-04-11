sudo add-apt-repository ppa:deadsnakes/ppa && sudo apt update && sudo apt install python3.6 && sudo rm /usr/bin/python3 && sudo ln -s /usr/bin/python3.6 /usr/bin/python3
curl "https://bootstrap.pypa.io/ez_setup.py" -o "ez_setup.py" && curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py" && sudo python3 ez_setup.py && sudo python3 get-pip.py
sudo -H /usr/local/bin/pip3 install --upgrade django==3.1

sudo apt-get install python3.6-dev libmysqlclient-dev

sudo python3 -m pip install mysqlclient
