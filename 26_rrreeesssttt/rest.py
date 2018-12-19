# Bo Hui Lu 
#SoftDev1 pd6
# K26 -- Getting More REST
# 2018-11-16

#Many thanks for Thomas Zhao for lendig me his home, internet, and laptop to do this homework
from flask import Flask, render_template
import urllib.request, json
import random

# instantiates that flask
app = Flask(__name__)


@app.route("/")
def home():

    #CAT FACT STUFF
    length = random.randint(10,500)
    fact = "fact?"
    linkerino = "https://catfact.ninja/"

    finale = linkerino + fact + str(length)

    url = urllib.request.urlopen(finale)

    #this is my dict
    data = json.loads(url.read().decode())
 #---------------------------------------------------------

   #doggo info
    linkerino2 = "https://dog.ceo/api/breeds/image/random"
    url2 = urllib.request.urlopen(linkerino2)
    data2 = json.loads(url2.read().decode())
   
    #---------------------------------------------------------
    #ddoggo info
    linkerino3 = "https://random.dog/woof.json"
    url3 = urllib.request.urlopen(linkerino3)
    data3 = json.loads(url3.read().decode())
    #print(data3)
    
    return render_template("index.html", img1 = data.get("fact"), img2 = data2.get("message"), img3 = data3.get("url"))



#run the flask
if __name__ == "__main__":
    app.run(debug=True)
