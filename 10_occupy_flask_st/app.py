#Team Jinja Bread Men - Joshua Weiner and Bo Hui Lu
#SoftDev pd6
#K #10: Jinja Tuning ...
#2018-09-23
<<<<<<< HEAD
=======

>>>>>>> a7672fd4b7c2b49df9c8dfcca7d30326a51296e7
from flask import Flask, render_template
from utils import reader
import random
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return('''
<h3>Find your job below</h3>
<a href="/occupations">Click Me!</a>
''')

@app.route("/occupations")
def occupado():
    #return dictionary, random occupation, html template
    return render_template("template.html", occ=reader.readcsv(), randocc=random.choice(reader.percentages()))

if __name__ == "__main__":
    app.debug=True
    app.run()
