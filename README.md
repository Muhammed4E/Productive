# Productive
#### Video Demo:  <URL https://www.youtube.com/watch?v=xOnC_2b-YC0>
#### Description: The app is a web app makes your more productive (Hopefully!) by storing your notes, ideas and thoughts
## Technologies
The app uses Flask framework in python and sqlite3 in the database as well as HTML, CSS, JS
and some Bootstrap framework.

## Pages
### Homepage
The homepage is pretty simple it's just divided into two parts an image and a description of 
the application, as well as a simple navigation bar that leads you to login and sign up page.

### Login
The login has a form that let's you login to the web app, If you are signed in it will redirect you
to the /notes route.

The form uses client side form validation using JS, As well as, Backend form validation using python.

To log in your data should meet the below conditions:
1. You should type a username.
2. You should type a password.
3. Your username should be exists.
4. Your password should be correct (Matches with the username).

After typing your data right, You will be redirected to the app main page, The notes page.

### Signup
The sign up page is pretty much like login page, With just another field, Confirmation password.

The form uses client side and backend form validation, too.

To sign up to the app, Your inputted data should meet the below conditions.
1. You should type a username.
2. You should type a password.
3. You should type the password again to confirm it.
4. Your username should not be already exists.
4. Your username length should be from 8 to 20 characters.
5. Your username SHOULD NOT contain any special characters, 
Just alphanumeric characters and underscore allowed.
6. Your password length should be from 8 to 30 characters.
7. Your confirmation password should match with the first password.

If you met the below instructions, You would have a new account on the application and
be redirected to the /notes route.

### Logout
This is not a page, It's just a route that clear the handed session from the browser.

### Notes
In this page you are able to see your existing notes, The notes container is `display: grid;`,
It stretch and shrink to be responsive on any device.

You can see your notes and notes' titles, If the note is more than 12 lines, The rest of the note will be hidden and three dots will show up at the end of the 12th line.

There is a tool bar at the top of each note your from it delete, edit and view the note.

You can from this route add a new note by pressing a plus icon, That will redirect you to /new route, Or logout by pressing a button that will redirect to /logout route.

The tool bar contains:
1. Delete icon that redirect you to /delete route and pass the id of the note to it.
2. Edit icon that redirect you to /edit route and also pass the id of the note to it.
3. View icon that is the same as edit but it were added to improve the user experience, Since a long note will not be showen completely.

### New
This page is a form that has two fields note and title, Note is required but title not, If you typed a long note a styled scroll bar will be showen.
You can submit and save the note or cancle and be redirected to /notes route.
When saving the new line you entered will be saved without any trouple.

### Delete
This is not a page it's just a route that will be visited when pressing the delete icon in the note's tool bar, It will delete the note and redirect you to /notes.

### Edit
This page is a form that has two field exactly like /new route, Note and title, They will be automatially filled with the note's data.
Then, when you submit it will update the data in the database.

## More information
The app uses flask_session to keep you logged in forever, It stores sessions in system fils.

Your password hash will be stored in the database not the password itself using the function `generate_password_hash(password)`, When signing you in, The app uses `check_password_hash(password, hash)` to check password.