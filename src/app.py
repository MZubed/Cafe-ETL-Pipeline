import csv


def parsing(): #Defines the function which will parse the csv file into a list of dictionaries containing each row of the customer information
    for rows in reader: #The rest of the rows in the file apart from the first line, so the customer information
        ordersDict=dict(zip(header,rows)) #zip() assigns both the header and customer information together and dict puts it in a dictionary format in all_dict. Only will do one line as it doesn't save each row in a dictionary.
        ordersList.append(ordersDict) #The .append() will now save each row in the dictionary and append the dictionary to the previously defined ordersList()
    return ordersList #Returns the ordersList as a value


ordersList=[] #Predefined orders list which will contain customer information

filename = "C:/Users/mzube/Downloads/etl-pipeline-cafe-project/data/raw-data.csv" #Location of my csv file and defines my file as filename

with open(filename, 'r') as file: #Opens file in read mode
    reader=csv.reader(file) #csv.reader reads all of my csv file one by one
    header=next(reader) #next() reads the first line in my csv file
    ordersList=parsing() #Stores the value as ordersList
    for rows in ordersList: #Goes through all of the orders in the list
        del rows['Customer Name'] #Deletes the Customer Names and Card Numbers to ensure privacy
        del rows['Card Number']
        print (rows)


#MYSQL DATABASES

'''
version: "3.8"
services:
  db:
    image: mysql
    container_name: mysql_container_etl
    restart: always
    environment:
      MYSQL_PASSWORD: 'password'
      MYSQL_ROOT_PASSWORD: "${mysql_pass}"
      MYSQL_DATABASE: "${mysql_db}"
    ports:
      - "3306:3306"
    security_opt:
      - seccomp:unconfined
    volumes:
      - type: volume
        source: my_db
        target: /var/lib/mysql
  adminer:
    image: adminer
    container_name: adminer_container_etl
    restart: always
    ports:
      - 8080:8080
volumes:
  my_db:
'''