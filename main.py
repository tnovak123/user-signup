from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

#def get_input(u, p, v, e):
#    return u, p, v, e

#def validate_input(u, ue, p, pe, v, ve, e,):

      
#    return

#def check_errors():
 #   if unerror == "" and pwerror == "" and vpwerror == "" and emailerror == "":
  #      return redirect('/welcome')


@app.route("/", methods=['GET', 'POST'])
def index():

    un = ""
    pw = ""
    vpw = ""
    email = ""
    unerror = ""
    pwerror = ""
    vpwerror = ""
    emailerror = ""

    if request.method == 'GET':
        return render_template('index.html', title='User Signup')
    elif request.method == 'POST':
        un = request.form['un']
        pw = request.form['pw']
        vpw = request.form['vpw']
        email = request.form['email']

        if un == "":
            unerror = "You must have a username."
        elif " " in un:
            unerror = "Not a valid username. Cannot contain a space."
        elif len(un) < 3 or len(un) > 20:
            unerror = "Username must be between 3 and 20 characters long."
        
        if pw == "":
            pwerror = "You must have a password."
        elif " " in pw:
            pwerror = "Not a valid username. Cannot contain a space."
        elif len(pw) < 3 or len(pw) > 20:
            pwerror = "Password must be between 3 and 20 characters long."
        
        if pw != vpw:
            vpwerror = "Passwords must match."

        if email == "":
            pass
        else:
            if "." and "@" not in email:
                emailerror = "That is not a valid email. Must contain '.' and '@'." 
    #        check_errors()

        if unerror == "" and pwerror == "" and vpwerror == "" and emailerror == "":
            return redirect('/welcome?un=' + un)
        else:
            return render_template('index.html', title='User Signup', un=un, 
                unerror=unerror, pw=pw, pwerror=pwerror, vpw=vpw, 
                vpwerror=vpwerror, email=email, emerror=emailerror)

@app.route("/welcome")
def welcome():
    un = request.args.get("un")
    return render_template('welcome.html', un=un)

app.run()
