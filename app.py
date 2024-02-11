import sqlite3
from flask import Flask, render_template, redirect, session, request, flash
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Routes
@app.route("/")
def homepage():
    try:
        if session["user_id"]:
            return redirect("/notes")
    except KeyError:
        return render_template("index.html")

@app.route("/notes")
def notes():
    try:
        if session["user_id"]:
            with sqlite3.connect("productive.db") as db:
                cr = db.cursor()
                notes = cr.execute("SELECT * FROM notes WHERE user_id = ?;", (session["user_id"],)).fetchall()
                for i in range(len(notes)):
                    # Convert it to list, Because tuple doesn't support items assigning.
                    notes[i] = list(notes[i])
                    notes[i][3] = notes[i][3].split("\r\n")
                return render_template("notes.html", notes=notes)

    except KeyError:
        return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    with sqlite3.connect("productive.db") as db:
        cr = db.cursor()
        users = cr.execute("SELECT * FROM users;")
        users = users.fetchall()
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")

            # Check if username and/or password weren't submitted someway.
            if not username or not password:
                flash("Must include username and password")
                return render_template("login.html", users=users)
            else:
                hash = cr.execute("SELECT hash FROM users WHERE username = ?;", (username,))
                hash = hash.fetchall()
                if (not check_password_hash(hash[0][0], password)):
                    flash("Password is not correct")
                    return render_template("login.html", users=users)

            # Log user in and redirect him to the app page
            session["user_id"] = cr.execute("SELECT id FROM users WHERE username = ?;", (username,)).fetchall()[0][0]
            return redirect("/notes")

        else:
            try:
                if session["user_id"]:
                    return redirect("/notes")
            except KeyError:
                return render_template("login.html", users=users)

@app.route("/signup", methods=["GET", "POST"])
def sign_up():
    with sqlite3.connect("productive.db") as db:
        cr = db.cursor()
        if request.method == "POST":
            # Get submitted values
            username = request.form.get("username")
            password = request.form.get("password")
            confirmation = request.form.get("confirmation")

            # Check if username, password and confirmation password weren't submitted someway.
            if not (username or password or confirmation):
                flash("Must include username, password and confirmation password.")
                return render_template("signup.html")
            else:
                # Add user to the database
                cr.execute("INSERT INTO users (username, hash) VALUES (?, ?);", (username, generate_password_hash(password)))
                id = cr.execute("SELECT id FROM users WHERE username = ?", (username,))
                session["user_id"] = id.fetchall()[0][0]
                return redirect("/notes")
        else:
            users = cr.execute("SELECT * FROM users;").fetchall()
            try:
                if session["user_id"]:
                    return redirect("/notes")
            except KeyError:
                return render_template("signup.html", users=users)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/new", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        with sqlite3.connect("productive.db") as db:
            cr = db.cursor()
            # Get submitted values
            title = request.form.get("title") # Title can be null
            note = request.form.get("note")

            # Check if the note is empty
            if note == "":
                flash("Note can't be empty")
                return render_template("new.html")

            # Add new note to user
            cr.execute("INSERT INTO notes (user_id, title, note) VALUES (?, ?, ?);", (session["user_id"], title, note))

            return redirect("/notes")

    else:
        try:
            if session["user_id"]:
                return render_template("new.html")
        except KeyError:
            return redirect("/login")  

@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        with sqlite3.connect("productive.db") as db:
            cr = db.cursor()
            # Get note id
            note_id = request.form.get("id")
            cr.execute("DELETE FROM notes WHERE id = ? AND user_id = ?", (note_id, session["user_id"]))
            return redirect("/notes")
        
    else: 
        return redirect("/notes")

note = ()

@app.route("/edit", methods=["GET", "POST"])
def edit():
    with sqlite3.connect("productive.db") as db:
        cr = db.cursor()
        if request.method == "POST":
            note_id = request.form.get("id")
            # that means the form was submitted from /edit
            if note_id:
                note = cr.execute("SELECT * FROM notes WHERE id = ? AND user_id = ?;", (note_id, session["user_id"])).fetchall()[0]
                return render_template("edit.html", note=note)

            # That means the form was submitted from /notes
            else:
                # Update note
                title = request.form.get("title")
                note = request.form.get("note")
                note_id = request.form.get("note_id")
                cr.execute("UPDATE notes SET title = ?, note = ? WHERE id = ? AND user_id = ?;", (title, note, note_id, session["user_id"]))
                return redirect("/notes")

        else:
            return redirect("/notes")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")