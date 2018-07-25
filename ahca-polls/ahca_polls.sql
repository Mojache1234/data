-- rolling average for approval rating

-- this would work only on postgres
SELECT a.Date,
    AVG(favor_rate) OVER (ORDER BY a.Date
        rows BETWEEN 6 preceding AND current row) AS avg_favor
FROM
(
    SELECT `End` AS `Date`,
        Favor / (Favor + Oppose) AS favor_rate,
        Favor - Oppose AS difference
    FROM ahca_polls
) a
ORDER BY `Date`
;

-- mysql version
CREATE VIEW favor AS
SELECT CAST(End_dt AS DATETIME) AS `date`,
    Favor / (Favor + Oppose) AS favor_rate,
    Favor - Oppose AS difference
FROM ahca_polls
ORDER BY `date`
;

SELECT a.date, avg(b.favor_rate), avg(b.difference)
FROM favor a
JOIN favor b
ON b.date BETWEEN ADDDATE(a.date, -6) AND a.date
GROUP BY a.date
ORDER BY a.date
;

SELECT CAST(Start_dt AS DATETIME) AS `date`, (Favor - Oppose) AS difference
FROM ahca_polls
ORDER BY `date`
INTO OUTFILE 'C:\\ProgramData\\MySQL\\MySQL Server 5.7\\Uploads\\ahca_polls_all.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
;
