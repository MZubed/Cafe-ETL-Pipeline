import csv
ordersList=[]
filename = "C:/Users/mzube/Downloads/etl-pipeline-cafe-project/data/raw-data.csv"
with open(filename, 'r') as file:
    reader=csv.reader(file)
    header=next(reader)
    print(list(zip(header,reader)))