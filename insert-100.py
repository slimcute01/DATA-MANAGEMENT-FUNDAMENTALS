#import modules
import csv
import itertools
import sys

#create empty list to hold records
count = 1
reading_table = []

new_sql = 'INSERT INTO `reading_table` VALUES\n'

#read csv file
#create for loop
with open ('cleaned.csv', 'r') as csvfile:
    for row in itertools.islice(csv.DictReader(csvfile, delimiter = ";"), 100):

        del row['Location']
        del row['geo_point_2d']
      
        reading_table = ["'" + str(i) + "'" for i in row.values()] 

        # specify delimeter used
        reading_table = ";".join(reading_table)

        reading_table = reading_table.replace("''", "NULL")
      
        new_sql += '(' + str(count) + ' , ' + reading_table + '),' +'\n'
        count += 1
    
#exit()
insert_sql = new_sql[:-2] + ';'
file = open('insert-100.sql', 'w')        
file.write(insert_sql + "\n")
print(insert_sql)