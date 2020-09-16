# Movie_restapi
1)Install the requiremnets


2)Run commands to make migratiosn and create superuser credentials - username:admin pass: admin

  *)python manage.py makemigrations
  
  *)python manage.py migrate
		
		
3)run app using python manage.py runserver


4)Access th efollowing links to work with the api

    *)127.0.0.1/Movie/ ---> To view all movie list and perform post and get operation
    
    *)127.0.0.1/detail/<id> (pass id like 1,2,3) ---> To view each movie  and perform put,delete and get operation
    
    *)Similarly 127.0.0.1/cust/ and 127.0.0.1/detail/<id> (pass id like 1,2,3) for customers
    
