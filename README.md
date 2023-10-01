
#  Building A Small Example Of A Social Network
This project is similar to existing networks such as Twitter and Instagram, and currently it is supposed to develop only its backend.

#




## Installation
1- Install python-venv 
```
pip install python3-venv
```

2- Create a new environment
```
python3 -m venv env
```

3- Active environment
```
source env/bin/activate
```

4- Install dependencies for develop or setup server
```
pip install -r requirements_dev.txt
pip install -r requirements.txt
```

5- Setup database and create news tables
```
python manage.py migrate
```

6- Setup with docker : if you want !
```
docker-compose -f docker-compose.dev.yml up -d
#server mode
```

7- Run the project
```
python manage.py runserver

```

    
## Screenshots

![App Screenshot](https://i.postimg.cc/TPmLsk13/Screenshot-2023-10-01-085339.png)

