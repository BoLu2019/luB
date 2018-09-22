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
            occList.append(row['Job Class'])
            
    occDict.pop('Total')
            
    for i in occDict.keys():
        occDict[i] = eval(occDict[i])           
      
    return render_template("template.html",
                           occ = occList,
                           occDict = occDict,
                           )
                           
    
        
if __name__ == "__main__":
    app.debug=True
    app.run()
