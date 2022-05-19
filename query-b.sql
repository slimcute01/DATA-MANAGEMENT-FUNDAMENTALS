-- Return the mean values of PM2.5 (particulate matter <2.5 micron diameter) & 
-- VPM2.5 (volatile particulate matter <2.5 micron diameter) by each station 
-- for the year 2019 for readings taken on or near 08:00 hours (peak traffic intensity)

-- select database
use `pollution-db2`;
SELECT 
    readings.`datetime` AS Date_time,
    stations.`Location` AS Station_name,
    AVG(readings.`pm2.5`) AS 'AveragePM2.5',
    AVG(readings.`vpm2.5`) AS 'AverageVPM2.5'
FROM
    readings
        JOIN
    stations ON readings.`stationsid-fk` = stations.`stations_id`
WHERE
    YEAR(`datetime`) = '2019'
        AND TIME(`datetime`) BETWEEN '07:30:00' AND '8:30:00'
        group by stations_id;