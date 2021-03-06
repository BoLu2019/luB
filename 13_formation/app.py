#Bo Hui Lu
#SoftDev1 pd6
#K #13: Echo Echo Echo 
#2018-9-27

from flask import Flask, render_template, request
app = Flask(__name__)    #create Flask object


@app.route("/")
def disp_loginpage():
    #workflow: uncomment one line at a time, re-run...
    print("\n\n\n")
    print( "***DIAG: this Flask obj ***" )
    print( app )
    print( "***DIAG: request obj ***" )
    print( request ) 
    print( "***DIAG: request.args ***" )
    print( request.args )
    print( "***DIAG: request.args['username']  ***" )
    #print( request.args['username'] )
    #print( "***DIAG: request.headers ***" )
    #print( request.headers )
    return render_template( 'login.html' )


@app.route("/auth")
def authenticate():
    print("\n\n\n")
    print( "***DIAG: this Flask obj ***" )
    print( app )
    print( "***DIAG: request obj ***" )
    print( request )
    print( "***DIAG: request.args ***" )
    print( request.args )
    print( "***DIAG: request.args['username']  ***" )
    print( request.args['username'] )
    print( "***DIAG: request.headers ***" )
    print( request.headers )
    return render_template( 'model_tmplt.html',
                            app = app,
                            req = request,
                            reqArg = request.args,
                            reqUser = request.args['username'],
                            reqHeader = request.headers,
                            reqMethod = request.method
                            )



if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()
