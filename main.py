### here are some pieces that may help
from flask import Flask, request, redirect, render_template, session, flash
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too


@app.route('/login', methods=['POST'])
def donut ():
    
    if request.method == 'POST':   
        person = request.form['username']
        password = request.form['password']       
        verify = request.form['verify']
        email = request.form ['email']

        person_error = ''
        password_error = ''
        verify_error = ''
        email_error = ''

        if (len(person)<3 or len(person)>20) or ((not person)or (" " in person)):
            person_error = "This is not a valid username"

        if (len(password)>20 or len(password)<3) or ((" " in password) or (not password)):
            password_error = "This is not a valid password"

        if verify !=password:
            verify_error = "These passwords do not match"

        if len(email)>0 and ("@"and ".") not in email:
            email_error = "This is not a valid email"

        if person_error or password_error or verify_error or email_error:

            return render_template("bagel.html",
                username_error = person_error,
                email_error = email_error,
                password_error=password_error,
                verify_error=verify_error,
                person = person)   

        else:
            return render_template("welcome.html", person = person)


@app.route("/")
def base():
    return render_template("bagel.html")


if __name__ == "__main__":
    app.run()

