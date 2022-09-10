-- https://www.hackerrank.com/challenges/weather-observation-station-7/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
SELECT DISTINCT CITY FROM STATION WHERE SUBSTR(CITY,1,1) IN ('A','E','I','O','U');
-- Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters.
-- Your result cannot contain duplicates.
SELECT DISTINCT CITY FROM STATION WHERE (SUBSTR(CITY,1,1) IN ('A','E','I','O','U') and SUBSTR(CITY,-1,1) IN ('A','E','I','O','U') ) 
--learned order by
select name from employee order by name

-- Query the following two values from the STATION table:
    --The sum of all values in LAT_N rounded to a scale of  decimal places.
    --The sum of all values in LONG_W rounded to a scale of  decimal places.

select round(sum(lat_n),2) , round(sum(long_w),2) from station

-- Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than 137.2345. Truncate your answer to  decimal places.
select round(max(lat_n), 4) from station where lat_n < 137.2345 ;
