
import pandas as pd
import plotly.express as px
import csv
import numpy as np

# df = pd.read_csv('iceCreamvsTemp.csv')

# fig= px.scatter(df,x= "Temperature", y="Ice-cream Sales( ₹ )")

# fig.show()


def getDataSource(dataPath):
    iceCreamSales=[]
    tempertaure=[]
    
    with open(dataPath) as csvFile:
        csvReader=csv.DictReader(csvFile)
        for row in csvReader:
            iceCreamSales.append(float(row['IceCreamSales']))
            tempertaure.append(float(row['Temperature']))
            
    return {"x": tempertaure,'y':iceCreamSales}

def findCorrelation(datasource):
    coRrelation= np.corrcoef(datasource['x'], datasource['y'])
    print("Correlation between the temp and iceCream SAles:  ",coRrelation[0,1])
    
def main():
    dataPath= './iceCreamvsTemp.csv'
    dataSource= getDataSource(dataPath)
    
    findCorrelation(dataSource)
    
main()