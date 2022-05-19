-- Extend the previous query to show these values for all stations in the years 2010 to 2019

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
    YEAR(`datetime`) between '2010' and '2019'
        AND TIME(`datetime`) = '08:00:00'
GROUP BY stations_id;