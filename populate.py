# imports modules
import mysql.connector
import sys
import csv
import re

try:
    # set the user and passoword and host
    conn = mysql.connector.connect(
        user="newuser",
        password="Newpassword01",
        host="localhost"    
            
    )
    # make/get the cursor
    cur = conn.cursor()

    #drop pre-existing and create new database
    cur.execute("DROP DATABASE IF EXISTS `pollution-db2`")
    cur.execute("CREATE DATABASE `pollution-db2`") 
    
    # empty list to hold records
    air_quality_records = [];

    # read the csv file and create list of lists
    with open('cleaned.csv','r') as csvfile: 
        reader = csv.reader(csvfile, delimiter=';') 
        for row in reader:
            air_quality_records.append(row)
        
      
    # remove header row
    air_quality_records.pop(0)
    
    # get a database handle
    cur.execute("USE `pollution-db2`")
    
     # define the SQL for each table
    stat_sql = """CREATE TABLE `stations`
                (`stations_id` INT(11) NOT NULL,
                `location` VARCHAR(50) NOT NULL,
                `geo_point_2d` VARCHAR(48) NOT NULL,
                PRIMARY KEY(`stations_id`));"""
    
    read_sql = """CREATE TABLE `readings`
            (`reading_id` INT(11) NOT NULL AUTO_INCREMENT,
            `datetime` DATETIME NOT NULL,
            `nox` FLOAT,
            `no2` FLOAT,
            `no` FLOAT,
            `pm10` FLOAT,
            `nvpm10` FLOAT,
            `vpm10` FLOAT,
            `nvpm2.5` FLOAT,
            `pm2.5` FLOAT,
            `vpm2.5` FLOAT,
            `co` FLOAT,
            `o3` FLOAT,
            `so2` FLOAT,
            `temprature` FLOAT,
            `rh` INT,
            `airpressure` INT,
            `datestart` DATETIME,
            `dateend` DATETIME,
            `current` TEXT(5),
            `instrumenttype` VARCHAR(32),
            `stationsid-fk` INT(11),
            PRIMARY KEY (`reading_id`));"""
                 
    schema_table_sql = """CREATE TABLE `schema_table`
                (`measure` VARCHAR(32) NOT NULL,
                 `description` VARCHAR(80) NOT NULL,
                 `unit` VARCHAR(24) NOT NULL,
                  PRIMARY KEY(`measure`));"""
            
    cur.execute(stat_sql)
    cur.execute(read_sql)
    cur.execute(schema_table_sql)
        
    # add the foreign-key relationships
    cur.execute("ALTER TABLE `readings` ADD FOREIGN KEY (`stationsid-fk`) REFERENCES stations(stations_id);")
       
  #create for loop to insert values    
    for row in air_quality_records:
                
        # set the autocommit flag to false
        conn.autocommit = False 
        
        #insert into stations table
        stat_sql = """INSERT IGNORE INTO `stations` values(%s, %s, %s)"""
        st_values = (row[4], row[17], row[18])        
        cur.execute(stat_sql, st_values) 
                 
        cur.execute("SELECT * FROM `stations` WHERE stations_id = %s", (row[4],))

        stations_id = cur.fetchone()[0]
        
                      
        #insert into readings table
        read_sql = """INSERT IGNORE INTO readings values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        rd_values = ("", row[0], row[1], row[2], row[3], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[19], row[20], row[21], row[22], stations_id)

        cur.execute(read_sql, rd_values) 
        read_sql = read_sql.replace("0", "NULL")
       
        #insert schema table
        schema_table_sql = """INSERT IGNORE INTO `schema_table` VALUES (%s, %s, %s)"""
        sq_values = [("Date Time", "Date and time of measurement", "datetime"), ("NOx","Concentration of oxides of nitrogen", "μg/m3"), 
        ("NO2", "Concentration of nitrogen dioxide", "μg/m3"), ("NO", "Concentration of nitric oxide", "μg/m3"), ("SiteID",  "Site ID for the station","integer"), 
        ("PM10", "Concentration of particulate matter <10 micron diameter", "μg/m3"), ("NVPM10", "Concentration of non - volatile particulate matter <10 micron diameter", "μg/m3"), 
        ("VPM10", "Concentration of volatile particulate matter <10 micron diameter", "μg/m3"), ("NVPM2.5", "Concentration of non volatile particulate matter <2.5 micron diameter", "μg/m3"), 
        ("PM2.5", "Concentration of particulate matter <2.5 micron diameter", "μg/m3"), ("VPM2.5", "Concentration of volatile particulate matter <2.5 micron diameter", "μg/m3"), 
        ("CO", "Concentration of carbon monoxide", "mg/m3"), ("O3", "Concentration of ozone", "μg/m3"), ("SO2", "Concentration of sulphur dioxide", "μg/m3"), 
        ("Temperature", "Air temperature", "°C"), ("RH", "Relative Humidity", "%"), ("Air Pressure", "Air Pressure", "mbar"), ("Location", "Text description of location", "text"), 
        ("geo_point_2d", "Latitude and longitude", "geo point"), ("DateStart", "The date monitoring started", "datetime"), ("DateEnd", "The date monitoring ended", "datetime"), 
        ("Current", "Is the monitor currently operating", "text"), ("Instrument Type", "Classification of the instrument", "text")]
 
        cur.executemany(schema_table_sql, sq_values)       
               
               
    conn.commit()
    conn.close()

# report on any error and exit with 1
# non-error scripts automatically exit with 0
except BaseException as err:
    print(f"This error occurred: {err}")
    sys.exit(1)