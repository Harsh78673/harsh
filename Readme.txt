DATE: 5-6-2023
    Web Application Framework
        Login, Logout, Store, Fetch, Update, Delete, Enquiry, Session, Management, Uploading, Server Side Validation, etc.


        DJANGO, FLASK, BOTTLE etc. These are some famous Web Application Frameworks .


        DJANGO MODULE
            How to install django module 
            <<------ pip install django ------>>

        With this django will be installed then run this command to create Project
            <<------ django-admin startproject cms . ------>> 
            -> "cms means name of your folder" and a fullstop at the end is important othervise django will create a cms folder inside folder 

            create app inside Project
            <<------ python manage.py startapp blog ------>>

            Now go to cms -> folder then seetings.py and under installed_apps list mention name of the django app you creted inside the django Project
            
        Now run this command to convert models to migrations
            <<------ python manage.py makemigrations ------>>

        Now run this command to convert migrations to table
            <<------ python manage.py migrate ------>>
        
        Now run this command to create a new user
            <<------ python manage.py createsuperuser ------>>

        Now run this command to run the server
            <<------ python manage.py runserver ------>>

        Now run this command to access website go to 127.0.0.1:8000
        Now to go to dashbord go to 127.0.0.1:8000/admin


DATE: 6-6-2023
     Today you start with models.py make a model and then run command 
        <<------ python manage.py makemigrations ------>> and after this command run this command
        <<------ python manage.py migrate ------>> 
      Now remember if you make any changes inside the [models.py] file you need to run these two commad again !important

      Download DB Browser for SQLite to read migrate file "db.sqlote3"   you can see title & content inside blog_post folder there

      Now go to [admin.py] add post there {Post is created inside admin you can see there}
      Then go to [views.py] add post inside home {It is added there you can see there}
      Now go to [home.html] add a for loop there {Loop is already added please check there to see} and add 'post.title and post.content' 
      there after that add a DELETE button with 'anchor' tag {Delete button is also already added there you can see there}
      Now after adding delete inside home.html go to [views.py] {Make delete function there with def there that is also added there you can see there}
      Now go to [urls.py] add the path for delete there {That is also added there you can see it there} 

      Now you can run the server to see the result and add a Post from admin dashbord 
      You can also run the server after just adding the title & content but you have to add delete button after that to see it


DATE: 7-6-2023 
    Step one first make [forms.py] file inside blog folder make a postForm class there
    Step two now go to [views.py] and add 'createPost' function there and also import postform there from blog there
    Step three now you need to create [insert.html] file for createPost then add method form there
    Step four go to [urls.py] and path for createPost there to excess createPost page
    Step five go to [home.html] and add slice there then add view in anchor tag there to see the remaining post in a single page 
    Step six now create [single.html] file to see the full post on a single page
    Step seven now add single function inside [views.py] 
    Step eight now add the path od single inside [urls.py]
    Step nine now create [nav.html] to seprate the code of nav and use it on any page you Watchin
    Step ten create folder {static} inside blog folder and create css & img folder inside static folder you can add css files & imgs inside these folders and use it inside html files 

DATE: 8-6-2023
    Step one go to [models.py] add dated there
    Step two go to [home.html] add dated there and run {makemigrations command & migrate} command
    Step three go to [models.py] add user there
    Step four go to [home.html] add user there
    Step five go to [models.py] add image there
    Step six go to [home.html] add image there
    Step seven goto [models.py] add active there    