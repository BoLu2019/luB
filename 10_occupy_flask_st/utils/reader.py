import csv
from csv import reader

occDict = {}
occList = []

#returns a dictionary of jobs/percentage pairs (occDict)
def readcsv():
    #opens csv file, reads it as dictionary
    #separates by commas not contained in double quotes
    with open('data/occupations.csv', 'r') as infile:
        reader = csv.DictReader(infile)
        #for each row in the csv file
        for row in reader:
            #add occupation and percentage to dictionary
             occDict[ row['Job Class'] ] = row['Percentage']
        #remove the dictionary key/value pair of 'Total'
        occDict.pop('Total')
    #Turns percentage string into a floating point
    #Loop through each key/value pair in dictionary
    for i in occDict.keys():
        occDict[i] = eval(occDict[i])
    return occDict

#returns a list of jobs, with the amount of each job proportional to the percentage of the workforce employed in that area (occList)
def percentages():
    #Adds jobs to list where it can be selected randomly based on its percentage
    for job in occDict.keys():
        for numTimes in range(int(occDict[job] * 10)):
            #Need to convert percentages to integers accurately to use the range() function,
            occList.append(job)
            #populate an list of ~1000 values, because of the use of range
            #list populated by percentages
    return occList
