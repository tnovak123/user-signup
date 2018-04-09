from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

un = ""
pw = ""
vpw = ""
email = ""
unerror = ""
pwerror = ""
vpwerror = ""
emailerror = ""

def get_input():
    un = request.form['un']
    pw = request.form['pw']
    vpw = request.form['vpw']
    email = request.form['email']
    return

def validate_input():

    if un == "":
        unerror = "You must have a username."
    elif len(un) < 3 or len(un) > 20:
        unerror = "Username must be between 3 and 20 characters long."
    
    if pw == "":
        pwerror = "You must have a password."
    elif len(pw) < 3 or len(pw) > 20:
        pwerror = "Password must be between 3 and 20 characters long."
    
    if pw != vpw:
        vpwerror = "Passwords must match."

    if "." and "@" not in email:
        emailerror = "That is not a valid email. Must contain '.' and '@'." 
      
    return

@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        get_input()
        validate_input()
        return render_template('index.html', un=un, unerror=unerror, pwerror=pwerror, vpwerror=vpwerror, emerror=emailerror)

@app.route("/welcome.html", methods=['POST'])
def welcome():
    return(render_template('welcome.html', un=un))

app.run()
