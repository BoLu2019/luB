#Team Jinja Bread Men - Joshua Weiner and Bo Hui Lu
#SoftDev pd6
#K #10: Jinja Tuning ...
#2018-09-23

from flask import Flask, render_template
import csv,random
app = Flask(__name__)

occDict = {}
occList = []

coll = [0,1,1,2,3,5,8]

@app.route("/my_foist_template")
def home():
    return render_template("template.html",
                        coll=coll)

@app.route("/occupations")
def occupado():
    with open('occupations.csv') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
             occDict[ row['Job Class'] ] = row['Percentage']
        occDict.pop('Total')
    for i in occDict.keys():
        occDict[i] = eval(occDict[i])
    for job in occDict.keys():
        for numTimes in range(int(occDict[job] * 10)):
            #Need to convert percentages to integers accurately to use the range() function,
            occList.append(job)
            #populate an array of ~1000 values, because of the use of range
            #array populated by percentages
    return render_template("template.html", occ=occDict, randocc=random.choice(occList))

if __name__ == "__main__":
    app.debug=True
    app.run()
