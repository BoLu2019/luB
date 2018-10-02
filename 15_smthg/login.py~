#Team Denn is this Bo'kay - Dennis Chen & Bo Hui Lu
#SoftDev pd6
#K #14: Do I Know You?
#10/1/18
from flask import Flask, render_template, request, url_for, redirect, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)


@app.route("/", methods = ['GET','POST'])
def disp_login():
    #print(request.method)
    if request.method == 'POST':
        #diagnostic
        session['username'] = request.form['username'] #assigns username var to the inputted username
        session['password'] = request.form['password'] #assigns password var to the inputted password


        #proceeds to authenticate the given login credentials.
        return redirect(url_for("authenticate"))

    return render_template('login.html')


@app.route('/auth')
def authenticate():
    #initially checks to see if the username is correctly inputted to match 'bo'
    #if it passes the username check, it checks the password 
    if 'username' in session and session['username'].lower() == 'bo':
        if 'password' in session and session['password'].lower() == 'dennis':
            username = session['username']
            #diagnostic
            print(session['username'])
            print(session['password'])
            
            return render_template('auth.html',
                                   method = request.method,
                                   name = "Bo",
                                   wa = "WAAAAAAAA.... Hello there")
        else:
            return redirect(url_for("error")) #if password doesn't match, goes to error page
    else:
        return redirect(url_for("error")) #if username doesn't match, goes to error page

    
@app.route('/error', methods = ['GET','POST'])
def error():
    if request.method == 'POST':
        #assigns session variables to inputted values
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        return redirect(url_for("authenticate"))
    
    return render_template('error.html', error = 'Wrong username or password')


@app.route('/logout')
def logout():
    
    #these pop() methods removes the variable we inputted in beginning
    session.pop('username', None)
    session.pop('password', None)
    
    #goes back to the login page
    return redirect(url_for('disp_login'))


#the good ole' debugger
if __name__ == '__main__':
    app.run(debug=True)
