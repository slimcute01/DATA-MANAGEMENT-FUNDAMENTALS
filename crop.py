#import module
import csv

#open readable csv file
with open ('bristol-air-quality-data.csv', newline= '') as csvfile:
    cropdata = csv.reader(csvfile, delimiter = ';') 

    #open writable csv file
    with open ('cropped.csv', 'w', newline= '') as new_air:
        new_file = csv.writer(new_air, delimiter= '-')

        #create 'for loop' with condition
        for index in cropdata:
            if index[0] >= '2010-01-01T00:00:00+00:00': 
                new_file.writerow(index)
  