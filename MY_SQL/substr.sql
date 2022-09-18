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

-- Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than . Round your answer to  decimal places.

select round(long_w, 4) from station where lat_n = (select max(lat_n) from station where lat_n < 137.2345)

-- Query the Western Longitude (LONG_W)where the smallest Northern Latitude (LAT_N) in STATION is greater than . Round your answer to  decimal places.
select round(long_w,4)
from station 
where lat_n = (select min(lat_n) from station where lat_n > 38.7780)

-- Eucliidan distance between two points
select round(power(power(max(lat_n) - min(lat_n),2) +  power(max(long_w) - min(long_w),2),0.5),4) from station



--- How to use CASE statements for SQL--
-- tabel of - A |  B  | C
            -------------
--          -20 |  20 | 23
--          -21 |  21 | 21
--          -12 |  45 | 2
SELECT CASE
        WHEN A + B <= C OR B + C <= A OR A + C <= B THEN 'Not A Triangle'
        WHEN A = B AND B = C AND A = C THEN 'Equilateral'
        WHEN A = B OR A = C OR B = C THEN 'Isosceles'
        WHEN A != B AND B != C THEN 'Scalene'
        END triangle
FROM TRIANGLES;
