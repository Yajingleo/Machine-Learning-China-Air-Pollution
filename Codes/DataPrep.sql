#Adjust text setting to utf8 for Chinese characters
show variables like '%character%';

set character_set_server=utf8;
set character_set_database=utf8;

#Create tables and databases. 
create database China_Air;

create table China_PM
(locationid int,
stationname nvarchar(100),
chinesename nvarchar(100),
latitude float,
longitude float,
pm25 int,
pm10 int,
o3 int,
no2 int,
so2 int,
co int,
temperature int,
dewpoint int,
pressure int,
humidity int,
wind int,
est_time timestamp
);
#Load data into table. 
load data local infile 
"/Volumes/Macintosh HD/Users/yajingleo/Downloads/data/ChinaPM2015.csv"
into table China_PM
fields terminated by ','
enclosed by '"'
lines terminated by'\n'
ignore 1 lines;

create table Beijing_weather
(
STN int,
WBAN int, 
YEARMODA date,   
TEMP float,  
TEMP1 int,   
DEWP float,
DEWP1  int,
SLP  float,
SLP1  int,
STP float,
STP1 int, 
VISIB float,
VISIB1 int,  
WDSP float,  
WDSP1 int, 
MXSPD float,  
GUST float,   
MAX_  float,
MIN_  float,
PRCP float,
SNDP float,
FRSHTT char(100)
);
#Load data into table. 
load data local infile "/Volumes/Macintosh HD/Users/yajingleo/Downloads/CDO1690827031565.csv"
into table Beijing_weather
fields terminated by ','
lines terminated by '\n'
ignore 1 lines;

#Create table Beijing_PM_night, by combining average PM value at 0AM and 7AM in Beijing. 
create table Beijing_PM_night as
select PM_7_AM, PM_0_AM, A.DATE_ as PUBLISHDATE from
(select avg(PM25) as PM_0_AM, date(PUBLISH_TIME) as DATE_ from China_PM 
where CITY_NAME_EN='beijing' and time(PUBLISH_TIME)='00:00:00'
group by PUBLISH_TIME) as A
inner join
(select avg(PM25) as PM_7_AM, date(PUBLISH_TIME) as DATE_ from Beijing_Air.PM 
where CITY_NAME_EN='beijing' and time(PUBLISH_TIME)='07:00:00'
group by PUBLISH_TIME) as B
on A.DATE_=B.DATE_;

#Combine weather on the previous day. 
create table Beijing_PM_combo as
select * from
Beijing_PM_night 
left join Beijing_weather
on Beijing_PM_night.PUBLISHDATE=date(Beijing_weather.YEARMODA)+1;

select * from Beijing_PM_combo 
into outfile '/Volumes/Macintosh HD/Users/yajingleo/Downloads/data/beijing_1.csv'
fields terminated by ','
lines terminated by '\n';
