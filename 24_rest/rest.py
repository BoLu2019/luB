# Bo Hui Lu - This homework was made possible by Aaron's generous donation of his laptop and his guidance
#SoftDev1 pd6
# K24 -- A RESTful Journey Skyward
# 2018-11-13


from flask import Flask, render_template
import urllib.request, json

# instantiates that flask
app = Flask(__name__)


@app.route("/")
def home():

    # my api key plus the picture I want
    linkerino = "https://api.nasa.gov/planetary/apod?api_key=JOjMA46tgsLCyqo5Djy8qF5cuwVMkft8rjIoolwI&date=2018-08-02"

    url = urllib.request.urlopen(linkerino)

    #this is my dict
    data = json.loads(url.read().decode())

    return render_template("index.html", img = data.get("url"))



#run the flask
if __name__ == "__main__":
    app.run(debug=True)
