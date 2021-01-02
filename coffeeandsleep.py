import plotly.express as px
import csv
import numpy as np
def DataSource(datapath):
    coffee = []
    sleep = []
    with open(datapath) as file:
        reader  = csv.DictReader(file)
        for row in reader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return{"x":coffee,"y":sleep}
def findcorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])
def setup():
    datapath = "C:/Users/Manorama/Desktop/coffeeandsleep.csv"
    datasource = DataSource(datapath)
    findcorrelation(datasource)
setup()
