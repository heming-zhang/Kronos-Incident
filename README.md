# testdemo (flask running test)

## 1. Environment Setting
### 1.0 If you get all installation without a package venv, just
```
virtualenv venv
python3 app.py
```

### 1.1 python3, pip3
```
$ python3 --version
$ pip3 --version
```

### 1.2 virtual environment
```
$ sudo pip3 install virtualenv
$ virtualenv venv
$ source venv/bin/activate
```

### 1.3 flask installation
```
$ sudo pip3 install Flask
```

### 1.4 running flask
```
# on remote server
$ flask run --host=0.0.0.0
# a simple way 
$ python3 app.py
```

### 1.5 Connection with MySQL through flask_sqlalchemy
```
sudo pip3 install flask_sqlalchemy
```

## 2 Data Processing
### 2.1 Import csv files into mysql
```
$ mysql -u root -p pok_origin < ./sql/pok_origin.sql
$ mysql -u root -p pattern_origin < ./sql/patterns_origin.sql
```

### 2.2 Convert sql tables into regularized mode
