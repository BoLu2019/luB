# Bo Hui Lu - This homework was made possible by Aaron's generous donation of his laptop and his guidance
#SoftDev1 pd6
# K25 -- Getting More REST
# 2018-11-14


from flask import Flask, render_template
import urllib.request, json
import random

# instantiates that flask
app = Flask(__name__)


@app.route("/")
def home():

    #NASA STUFF
    key = "JOjMA46tgsLCyqo5Djy8qF5cuwVMkft8rjIoolwI"
    date = "&date=2018-08-02"
    linkerino = "https://api.nasa.gov/planetary/apod?api_key="

    finale = linkerino + key + date

    url = urllib.request.urlopen(finale)

    #this is my dict
    data = json.loads(url.read().decode())
 #---------------------------------------------------------

   #MEMES STUFF
    num = random.randint(1,5000)
    key2 = str(num) + ".jpg"
    linkerino2 = "https://memegenerator.net/img/images/"
    finale2= linkerino2+ key2 
   
    #---------------------------------------------------------
 
    return render_template("index.html", imgNASA = data.get("url"), imgMEME = finale2 )



#run the flask
if __name__ == "__main__":
    app.run(debug=True)
