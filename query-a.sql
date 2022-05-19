-- Return the date/time, station name and the highest recorded value of nitrogen oxide (NOx) 
-- found in the dataset for the year 2019.

-- select database
use `pollution-db2`;
-- select the columns and create Alias 
SELECT 
    `datetime` AS Date_Time,
    `Location` AS Station_name,
    `nox` AS HighestRecordedValueOfNox
-- specifiy the tables to select from
FROM
    readings
    join
    stations on readings.`stationsid-fk` = stations.`stations_id`
-- use a subquery in where condition to allow use of 'max' aggregate function
-- and recieve multiple rows where the year conditions are also met
WHERE
    `nox` = (SELECT 
            MAX(`nox`)
        FROM
            `readings`
        WHERE
            YEAR(`datetime`) = '2019')
group by station_name;
