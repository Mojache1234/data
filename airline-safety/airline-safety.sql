-- Can't really do a hypothesis test because they're not experiments
-- Rather, I can do a correlation test to see if the two variables are correlated

-- Average # of incidents and variance (n = 56)
SELECT AVG(incidents_85_99/(avail_seat_km_per_week/1000000000)) AS old, VARIANCE(incidents_85_99/(avail_seat_km_per_week/1000000000)) AS old_var, AVG(incidents_00_14/(avail_seat_km_per_week/1000000000)) AS new, VARIANCE(incidents_00_14/(avail_seat_km_per_week/1000000000)) AS new_var
FROM airline_safety
;

-- Average # of fatal accidents
SELECT AVG(fatal_accidents_85_99/(avail_seat_km_per_week/1000000000)) AS old, VARIANCE(fatal_accidents_85_99/(avail_seat_km_per_week/1000000000)) AS old_var, AVG(fatal_accidents_00_14/(avail_seat_km_per_week/1000000000)) AS new, VARIANCE(fatal_accidents_00_14/(avail_seat_km_per_week/1000000000)) AS new_var
FROM airline_safety
;

-- Average # of fatalities
SELECT AVG(fatalities_85_99/(avail_seat_km_per_week/1000000000)) AS old, VARIANCE(fatalities_85_99/(avail_seat_km_per_week/1000000000)) AS old_var, AVG(fatalities_00_14/(avail_seat_km_per_week/1000000000)) AS new, VARIANCE(fatalities_00_14/(avail_seat_km_per_week/1000000000)) AS new_var
FROM airline_safety
;

-- Correlation between incidents from 85-99 and 00-14
SELECT airline, incidents_85_99/(avail_seat_km_per_week/1000000000), incidents_00_14/(avail_seat_km_per_week/1000000000)
FROM airline_safety
INTO OUTFILE 'C:\\ProgramData\\MySQL\\MySQL Server 5.7\\Uploads\\airline_incidents.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
;

-- Correlation between incidents from 85-99 and 00-14
SELECT airline, fatalities_85_99/(avail_seat_km_per_week/1000000000), fatalities_00_14/(avail_seat_km_per_week/1000000000)
FROM airline_safety
INTO OUTFILE 'C:\\ProgramData\\MySQL\\MySQL Server 5.7\\Uploads\\airline_fatalities.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
;
