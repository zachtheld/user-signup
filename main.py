from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/signup")
def display_signup_form():
    return render_template('signup_form.html') 

@app.route("/signup", methods=['POST'])
def valid_inputs():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    user_name_error = ''
    #password_error = ''
    #validate_pass_error = ''
    #email_error = ''
    
    if len(username) < 3:
        user_name_error = 'Please enter a valid username'
        username = ''
        return render_template('signup_form.html', user_name_error=user_name_error,
        username=username, password=password, verify=verify, email=email)



@app.route('/welcome', methods=['POST'])
def welcome_page():
    username =request.form["username"]
    return render_template('welcome.html', name=username)


app.run()