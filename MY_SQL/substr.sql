-- https://www.hackerrank.com/challenges/weather-observation-station-7/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
SELECT DISTINCT CITY FROM STATION WHERE SUBSTR(CITY,1,1) IN ('A','E','I','O','U');
-- Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters.
-- Your result cannot contain duplicates.
SELECT DISTINCT CITY FROM STATION WHERE (SUBSTR(CITY,1,1) IN ('A','E','I','O','U') and SUBSTR(CITY,-1,1) IN ('A','E','I','O','U') ) 
--learned order by
select name from employee order by name