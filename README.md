# Galleria

###  Author
Carol Gitonga

### Description
Galleria project allows users to add images and view different images on the main page that interest them. It allows a user to search for a picture depending on the category and location the image was taken. It also allows them to copy the image link.

### User Stories
* View different photos that interest me.
* Click on a single photo to expand it and also view the details of the photo. 
* Search for different categories of photos. (ie. Travel, Food)
* Copy a link to the photo to share with my friends.
* View photos based on the location they were taken.
* Add an image with your preferred location and category.

### Technologies Used
1. HTML and CSS
2. Python
3. Django
1. Postgres
1. Heroku for deployment

## Set up and Installation
### Prerequisites
The user will require git, django, postgres and python3 installed in their machine.
To install these two, you can use the following commands
```
#git
$ sudo apt install git-all

#python3
$ sudo apt-get install python3

#django
$ pip install django

#postgres
$ sudo apt-get install postgresql postgresql-contrib libpq-dev
```

### .ENV file
1. SECRET_KEY='<SECRET_KEY>'
1. DEBUG=True #set to false in production
1. DB_NAME='galleria'
1. DB_USER='user'
1. DB_PASSWORD='password'
1. DB_HOST='127.0.0.1'
1. MODE='dev' #set to 'prod' in production
1. ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
1. DISABLE_COLLECTSTATIC=1

### Installation
1. To access this application on your command line, you need to clone it 
`git clone git@github.com:carol-profile/Galleria.git`
1. Create a requirements.txt in the root folder and copy the requirements above.
1. Install the required technologies with
`pip install -r requirements.txt`
1. Create a .env file and copy the .env code above
1. You can then run the server with:
`python3 manage.py runserver`
1. You can make changes to the db with
`python3 manage.py makemigrations photos`
`python3 manage.py migrate`
4. You can run tests:
`python3 manage.py test photos`

### Django Admin
Username: carol


### Live link
You can view the live site [here](https://carolgalleria.herokuapp.com/)

## License
* *MIT License:*

Copyright (c) 2022 Carol Gitonga
