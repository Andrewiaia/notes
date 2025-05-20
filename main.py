from flask import Flask, request, render_template , url_for, redirect, flash, session

app = Flask(__name__)
app.secret_key="hi"

logins = {
    "Andrew":"Hi"
}

notes =  {
    "Andrew" : ["I love balls", "Suck my dick"]
}

current_user = ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in logins and password in logins[username]:
            session['user'] = username
            return redirect(url_for('notes'))
        else:
            error = "Account not found"
    return render_template('login.html', error = error)


@app.route('/sign-up', methods =['GET', 'POST'])
def signup():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password"]
        password2 = request.form["confirm-password"]  
        if password1 == password2:
            logins[username] = password1
            flash("Account Created!")
            return redirect(url_for('login'))
        else:
            error = "Please Try Again" 
    return render_template('sign-up.html', error=error)   

@app.route('/notes', methods=['GET', 'POST'])  
def notes():
    user = session['user']
    return render_template('notes.html' , current_user = user, notes = notes)




if __name__ == "__main__":
    app.run(debug=True)