#Bo Hui Lu
#SoftDev1 pd6
#K #13: Echo Echo Echo 
#2018-9-27

from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)    #create Flask object


@app.route("/")
def disp_loginpage():
    return render_template( 'login.html' )


@app.route("/auth", methods = ["POST"])
def authenticate():
    print (url_for('disp_loginpage'))
    print (url_for('authenticate'))
    user = 'Bo'
    passwd = 'Dennis'

    
    if request.form["username"] != 'Bo':
        rtr = "Wrong username buddy"
        return render_template( 'login.html', error = rtr)

    if request.form["password"] != 'Dennis':
        rtr = "Wrong password buddy"
        return render_template( 'login.html', error = rtr)

    return render_template( 'model_tmplt.html',
                            app = app,
                            req = request,
                            reqUser = "Bo",
                            reqHeader = request.headers,
                            reqMethod = request.method
                            )



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
