# foodieClub DRF-API - Backend

foodieClub project portfolio has been created for educational purposes only as the 5th project in the Code Institute’s full stack development program.

Using the principles of UX design and the agile development methodology, this project was developed using Django Rest Framework that handles all backend functionality including user profiles, posts, comments, likes, bookmark posts, followers, authentication, authorization and more.

# Preview

You can view the live deployed backend here: <a href="https://foodieclub-drf-api.herokuapp.com/" target="_blank"> foodieClub DRF-API </a>

You can view the live site here: <a href="https://foodieclub.herokuapp.com/" target="_blank"> foodieClub App </a>

The repository for the frontend application can be found here:  <a href="https://github.com/henryl74/foodieclub" target="_blank"> foodieClub React </a>

# Contents

* [Database Schema](<#database-schema>)
* [Agile Methodology](#agile-methodology)
* [User Stories](#user-stories)
* [Technologies Used](#technologies-used)
* [Testing](<#testing>)
  * [Bugs Fixed](#bugs-fixed)
* [Deployment](#deployment)
* [Credits](<#credits>)
* [Acknowledgements](<#acknowledgements>)

# Database Schema

The Database Schema contains the following model instances:

- Profiles
- Posts
- Ingredients
- Comments
- Likes
- Favorites
- Followers

[Back to top](<#contents>)

## Agile Methodology

The principles of agile methodology were utilized during the project. By assigning user stories to issues and taking advantage of the GitHub Kanban board functionality, the necessary goals and priorities throughout the project could be well defined. In addition, labels were used to further define the priority of each user story in the Kanban board.

[Back to top](<#contents>)

## User Stories

  -   #### First Time Visitor Goals
        - 
        -
        -

[Back to top](<#contents>)

* # Technologies Used

    * ## Languages Used

        * [Python](https://www.python.org/)

    * ## Libraries/Framework Used

        * [Django](https://www.djangoproject.com/)
        * [Django REST framework](https://www.django-rest-framework.org/)

    * ### Libraries/Module Installed

        * asgiref==3.6.0
        * cloudinary==1.32.0
        * dj-database-url==0.5.0
        * dj-rest-auth==2.1.9
        * Django==3.2.18
        * django-allauth==0.44.0
        * django-cloudinary-storage==0.3.0
        * django-cors-headers==3.14.0
        * django-filter==22.1
        * djangorestframework==3.14.0
        * djangorestframework-simplejwt==5.2.2
        * gunicorn==20.1.0
        * oauthlib==3.2.2
        * Pillow==9.4.0
        * psycopg2==2.9.5
        * PyJWT==2.6.0
        * python3-openid==3.2.0
        * pytz==2022.7.1
        * requests-oauthlib==1.3.1
        * sqlparse==0.4.3

    * ## Other Technologies

        * [Stackoverflow](https://stackoverflow.com/)
        * [Git](https://git-scm.com/)
        * [Github](https://github.com/)
        * [Gitpod workspace](https://gitpod.io/workspaces)
        * [Heroku](https://dashboard.heroku.com/apps)
        * [Flowchart](https://lucid.app/documents#/documents?folder_id=home)
        * [Cloudinary](https://cloudinary.com/)
        * [ElephantSQL](https://www.elephantsql.com/)
        * [CI Python Linter](https://pep8ci.herokuapp.com/)
        * [Slack](https://slack.com/intl/en-gb/)

[Back to top](<#contents>)

# Testing

I have included testing details in a separate document called [Testing.md](./docs/testing.md)

[Back to top](<#contents>)

## Bugs Fixed

- Register page for laptops had a css issue with the container, I fixed it by removing the width, margin-left, and added margin: 0 7% within the css file.

![Register Page Bug](./docs/readme-testing-images/register_bug.jpeg)

- Menu, the images were not displaying, I fixed it by changing the path to absolute on each image in the html file.

![Menu Page Bug](./docs/readme-testing-images/menu_images_bug.jpeg)

- Home Page rendiring error, I fixed it by udating the path under urls.py

![Home Page Bug](./docs/readme-testing-images/home_error_template.jpeg)

- Update Booking rendiring error, I fixed it by udating the path under urls.py

![Update Booking Bug](./docs/readme-testing-images/edit_booking.jpeg)

[Back to top](<#contents>)

## Deployment

Git and GitHub are used for version control. Python is the backend language, and can't be displayed with GitHub alone, To live preview my project, I used Heroku.

<h3 id="setting-up-json-web-tokens">Setting Up JSON Web Tokens</h3>

1. Install JSON Web Token authentication
```
pip install dj-rest-auth
```
2. In settings.py add the following to the 'INSTALLED_APPS' list
```
'rest_framework.authtoken'
'dj_rest_auth'
```
3. In the main urls.py file add the relevant url path
```
path('dj-rest-auth/', include('dj_rest_auth.urls')),
```
4. Migrate the database using the terminal command
```
python manage.py migrate
```
5. Install all_auth for user authentication
```
pip install 'dj-rest-auth[with_social]'
```
6. In settings.py add the following to the 'INSTALLED_APPS' list
```
'django.contrib.sites',
'allauth',
'allauth.account',
'allauth.socialaccount',
'dj_rest_auth.registration',
```
7. Add the following declaration in settings.py
```
SITE_ID = 1
```
8. In the main urls.py file add the registration url path
```
 path(
        'dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')
    ),
```
9. Install the JSON tokens with the *simple jwt* library
``` 
pip install djangorestframework-simplejwt
```
10. In env.py set DEV to 1 to check whether the environment is development or production
```
os.environ['DEV'] = '1'
```
11. In settings.py add the following if else statement
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
```
12. Add the following declarations in settings.py
```
REST_USE_JWT = True # enables token authentication
JWT_AUTH_SECURE = True # tokens sent over HTTPS only
JWT_AUTH_COOKIE = 'my-app-auth' #access token
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token' #refresh token
```
13. Create a serializers.py file in the drf_api (project file name)
14. Utilize the code from the Django documentation UserDetailsSerializer as follows:
```
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """Serializer for Current User"""
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        """Meta class to to specify fields"""
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )
```
15. In settings.py overwrite the default User Detail serializer
```
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'drf_api.serializers.CurrentUserSerializer'
}
```
16. Run the migrations for database again
```
python manage.py migrate
```
17. Update the requirements file with the following terminal command
```
pip freeze > requirements.txt
```
18. Make sure to save all files, add and commit followed by pushing all updates to Github.

## Deployment to Heroku

### 1. Creating the Django Project
* If development if being done locally: Activate your virtual environment
* To ensure the virtual environment is not tracked by version control, add .venv to the .gitignore file.
* Install Django and gunicorn: `pip install django gunicorn`
* Install supporting database libraries dj_database_url and psycopg2 library: `pip install dj_database_url psycopg2`
* Install Cloudinary libraries to manage static files: `pip install dj-3-cloudinary-storage`
* Create file for requirements: `pip freeze --local > requirements.txt`
* Create project:`django-admin startproject project_name .`
* Create app: `python manage.py startapp app_name`
* Add app to list of `installed apps` in settings.py file: `'app_name'`
* Migrate changes: `python manage.py migrate`
* Test server works locally: `python manage.py runserver`



### 2. Create your Heroku app
* Navigate to the Heroku website
* Create a Heroku account by entering your email address and a password (or login if you have one already).
* Activate the account through the authentication email sent to your email account
* Click the **new button** on the top right corner of the screen and select create a new app from the dropdown menu.
* Enter a unique name for the application.
* Select the appropriate region for the application.
* Click create app
* In the Heroku dashboard click on the Resources tab
* Scroll down to Add-Ons, search for and select 'Heroku Postgres' / Now replaced by 'ElephantSQL'
* In the Settings tab, scroll down to 'Reveal Config Vars' and copy the text in the box beside DATABASE_URL.

### 3. Set up Environment Variables
* In you IDE create a new env.py file in the top level directory
* Add env.py to the .gitignore file
* In env.py import the os library
* In env.py add `os.environ["DATABASE_URL"]` = "Paste in the text link copied above from Heroku DATABASE_URL"
* In env.py add `os.environ["SECRET_KEY"] = "Make up your own random secret key"`
* In Heroku Settings tab Config Vars enter the same secret key created in env.py by entering 'SECRET_KEY' in the box for 'KEY' and your randomly created secret key in the 'value' box.

### 5. Heroku Deployment: 
* Click Deploy tab in Heroku
* In the 'Deployment method' section select 'Github' and click the 'connect to Github' button to confirm.
* In the 'search' box enter the Github repository name for the project
* Click search and then click connect to link the heroku app with the Github repository. The box will confirm that heroku is connected to the repository.

### 6. Final Deployment
In the IDE: 
* When development is complete change the debug setting to: `DEBUG = False` in `settings.py` 
* In Heroku settings config vars change the DISABLE_COLLECTSTATIC value to 0
* Because DEBUG must be switched to True for development and False for production it is recommended that only manual deployment is used in Heroku. 
* To manually deploy click the button 'Deploy Branch'. The default 'main' option in the dropdown menu should be selected in both cases. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser.

[Back to top](<#contents>)

## Credits

- [Code Institute walkthrough](https://codeinstitute.net/) as inspiration and code examples, the code institute walkthroughs "Django REST Framework" was referenced during the development cycle of this API.

- [Django Documenation](https://www.djangoproject.com/) was used to provide examples of code solutions and Django functionality.

- [Django YouTube Tutorial on how to create a Blog](https://www.youtube.com/watch?v=n-FTlQ7Djqc&list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc)

- [Python Django Web Framework - Full Course for Beginners](https://www.youtube.com/watch?v=F5mRW0jo-U4)

- [Python Django 7 Hour Course](https://www.youtube.com/watch?v=PtQiiknWUcI)

- [Stackoverflow](https://stackoverflow.com/)

- [Slack](https://slack.com/intl/en-gb/) community support.

- Code Institute - Tutor Assistance, BIG THANK YOU for all your support, suggestions and help!


[Back to top](<#contents>)

## Acknowledgements

- Again, the online tutors for all their help.
- The Code Institute slack community.
- All my classmates for constantly sharing new ideas in our dedicated slack channel.
- Stack Overflow question and answer website.
- My mentor for this project Marcel Mulders, thank you for all your all your guidance and support given, I learned a lot throughout our sessions.
- My family, THANK YOU for being always part of the team and this journey.
- Last but not least Code Institute student support team, for being there for us.

[Back to top](<#contents>)
