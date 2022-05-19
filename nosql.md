# Modeled Data From Mysql to a NoSQL using MongoDB

NoSQL databases are non-tabular databases that store data differently. The term “NoSQL” stands for “non SQL” or “not only SQL”.

NoSQL is a non-tabular database that stores data without relational structures. The term “NoSQL” is used to represents “non SQL” or "not-only-SQL.” There are four (4) main types namely the key-value, the wide-column, graphs, and documents. Usually, these databases can take high user load. It provides schemas which help with large sized data and so it is appropriate for our use to model a station from the Bristol air quality data we are working with. Here, we use a database to model all the related data for a specific monitor called __Bath Road station__.

The database I have chosen to complete this assessment is the **MongoDB** database. I feel it is a good fit because it is a general purpose, document-based and distributed database, built with new application developers in mind. Also, it has a flexible data model, it has easy scalability, and it has the option to stores data in JSON-like documents, which means the fields can vary from document to document and any data structure can easily be changed over time. Working with this type of database was relatively new to me, and so initially I was hesitant, but I knew it would open me up to a new perspective of working with data. Looking back, I’m feeling grateful that I have gained knowledge on the use of NoSQL, and personally, I found MongoDB easier to understand and work with, when compared to other available databases.

First, I wrote a MySQL query that extracts all the information pertaining to the Bath Road station, excluding the siteID and then I exported this data in Json format to a folder outside my SQL workbench. The SQL script I required to complete my task was to contain all fields from the table excluding the siteID but I was unable to write a script that would allow me to select all except the one. So instead, I wrote a script listing out all the fields I wanted to appear in my output.

_See extracted jason file in link below:_

[jason_file]: bath_station_Dmf5.json
[Extracted Jason File][jason_file]

After installing my MongoDB application, I created a new database within the application which I named “readings”, and I went ahead to import my previously saved Json file containing my result set, using the ‘add data’ menu. Importing this data took a couple of minutes and after I was done importing into the database, my result set was printed neatly, with assigned object id for each array. This was generally a great experience for me as a first time MongoDB user because uploading this file was relatively simple and it has encouraged me to learn more about non-relational data base.

*Attached below is an image of my populated MongoDB database:*

![no_sql_image](mongoDB.png.bmp)

I think that my ease with using MongoDB resulted from the research videos I had watched beforehand, and the review of my lecture notes on understanding JSON files.

In conclusion, I learnt that I don’t need to be hesitant towards any unfamiliar concept, as I am only a study away from whatever knowledge I desire to acquire, I also learnt that the possibilities available with data are endless as this course constantly introduces a new block of those possibilities.

If I had to do this project again, I would develop a better SQL script to select the portion of data required for my work. I would also start my research and studies early on so that am better prepared and able to deliver efficiently and timely.
