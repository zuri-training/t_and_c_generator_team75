Duruaku Ebuka (Backend dev)'s Contributions
The backend of the entire application is built using Django. Django is a python framework.
Django needs the Custom user model to be created to provide a user that logs in with an email. The backend is done using Postgresql as that is the preferred database to use 
The Urls.py
The URL routing is done and designed for each page specifically. It points to the HTML file and the views that are to render it
The Forms.py
The forms in the backend are really important as it provides the field input. It is directly modeled after the models.py to fit save into the backend 
The Models.py
The model is designed and saved to the database. With it the entire schema field and it's ready to take the posts and store them. Allowing the user to view and edit them.

HTML Templates
Some HTML templates will have to be given dynamic data to easily fetch it from the database and insert it.
The templates showing the nav bar will have to show when the user is logged in by displaying the email and when not logged in it shows and print the user to log in 

The Dashboard 
Writing the views of the dashboard pages and handling all the pages required. Setting the logout link and making it work
The dashboard only shows the posts created by the users and not others
Adding an editing feature so users can edit the post they created
Added a delete feature so users can delete the post that wants to be deleted 
Added a view so to see the post

The Preview and Download
Added a preview page so you can see how it would look. Added a pdf feature so you can download it as pdf. 
Also Added a word document feature so you can download it as a word file.

