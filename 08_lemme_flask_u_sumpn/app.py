#Bo Hui Lu
#SoftDev1 pd6
#K #08: Fill Yer Flask
#2018-9-19
from flask import Flask

app = Flask(__name__)

@app.route('/')
def func1():
    return '<a href = "http://127.0.0.1:5000/Ho"> Hello, World!</a>'

@app.route('/Ho')
def func2():
    return '<a href = "http://127.0.0.1:5000/Ho/Bo"> peekaboo </a>'

@app.route('/Ho/Bo')
def func3():
    return '<a href = "http://127.0.0.1:5000/"> you done good my friend </a>'
    
