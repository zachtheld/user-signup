from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/signup')
def display_signup_form():
    return render_template('signup_form.html', title='User Signup') 

def input_length(x):
    if len(x)>= 3 and len(x) <=20:
        return True
    else:
        return False

def email_symbol(x):
    if x.count('@') == 1:
        return True
    else:
        return False

def email_period(x):
    if x.count('.') == 1:
        return True
    else:
        return False

def char(x):
    if x:
        return True
    else:
        return False

@app.route('/signup', methods=['POST'])
def validate_user_inputs():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    #username validation
    if not input_length(username):
        username_error = 'Username must be between 3 and 20 characters'
        username = ''
    elif ' ' in username:
        username_error = 'Username cannot contain spaces'
        username = ''

    #password validation
    if not char(password) and not char(verify):
        password_error = 'Required'
        verify_error = 'Required'
        password = ''
        verify = '' 
    elif not char(password):
        password_error = 'Required'
        password = ''
    elif not input_length(password) and not input_length(verify):
        password_error = 'Password must be between 3 and 20 characters'
        verify_error = password_error
        password = ''
        verify = ''    
    elif ' ' in password and ' ' in verify:
        password_error = 'Password cannot contain spaces'
        verify_error = password_error
        password = ''
        verify = ''
    elif ' ' in password and char(verify):
        password_error = 'Password cannot contain spaces'
        verify_error = 'Please enter a matching password'
     
    #verify password matches password
    if verify != password:
        verify_error = 'Please enter a matching password'
        verify = ''

    #email validation
    if char(email):
        if not email_symbol(email):
            email_error = 'A valid email contains one "@" symbol and one "."'
            email = ''
        elif not email_period(email):
            email_error = 'A valid email contains one "@" symbol and one "."'
            email = ''
        elif  ' ' in email:
            email_error = 'A valid email contains no spaces'
        elif not input_length(email):
            email_error = 'A valid email must be between 3 and 20 characters'

    if not username_error and not password_error and not verify_error and not email_error:
        username = username
        return redirect('welcome?username={0}'.format(username))
    else:
        return render_template('signup_form.html', username_error=username_error,
        username=username, password_error=password_error, password=password,
        verify_error=verify_error, verify=verify, email_error=email_error,
        email=email)

@app.route('/welcome')
def welcome_page():
    username = request.args.get('username')
    return render_template('welcome.html',title='Welcome', username=username)

app.run()