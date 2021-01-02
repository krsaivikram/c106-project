import plotly.express as px
import csv
import numpy as np
def DataSource(datapath):
    marks = []
    dayspresent = []
    with open(datapath) as file:
        reader  = csv.DictReader(file)
        for row in reader:
            marks.append(float(row["Marks In Percentage"]))
            dayspresent.append(float(row["Days Present"]))
    return{"x":marks,"y":dayspresent}
def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])
def setup():
    datapath = "C:/Users/Manorama/Desktop/Marks&days.csv"
    datasource = DataSource(datapath)
    findcorrelation(datasource)
setup()
