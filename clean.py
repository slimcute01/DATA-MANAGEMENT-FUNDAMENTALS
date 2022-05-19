#import module
import csv 

#creat a python dictionary 
monitors = {'188':'AURN Bristol Centre',
'203':'Brislington Depot',
'206':'Rupert Street',
'209':'IKEA M32',
'213': 'Old Market',
'215':'Parson Street School',
'228':'Temple Meads Station',
'270':'Wells Road',
'271':'Trailer Portway P&R',
'375':'Newfoundland Road Police Station',
'395':"Shiner's Garage",
'452':'AURN St Pauls',
'447':'Bath Road',
'459':'Cheltenham Road \ Station Road',
'463':'Fishponds Road',
'481':'CREATE Centre Roof',
'500':'Temple Way',
'501':'Colston Avenue'}

#open readable file
with open ('cropped.csv', newline= '') as csvfile:
    cleandata = csv.reader(csvfile, delimiter = ';')

#open writable file
    with open ('cleaned.csv', 'w', newline='') as new_csv:
        new_clean = csv.writer(new_csv, delimiter =';')
        
        row_number = 1
        #skip the header
        header= next(cleandata)

        new_clean.writerow(header)
        
        #create 'for loop'
        for line in cleandata:
            site_id = line[4]
            location_id = line[17]

            #use if..else statements to evaluate
            if len(site_id) > 0 and (site_id in monitors) and monitors[site_id] == location_id: 
                new_clean.writerow(line) 
            else:
                if len(site_id) == 0:
                    print('line', row_number, 'siteid is not given')
                elif site_id not in monitors:
                    print('line', row_number, 'site_id does not exist in monitors', line[17])
                elif monitors[site_id] != line[17]:
                    print('line', row_number, 'site_id location should be', monitors[site_id], 'not', line[17])
            row_number += 1