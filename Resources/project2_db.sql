create table poverty_from_census (
YEAR INT,
STATE varchar(30),
Percent float);

select * from poverty_from_census;

create table state_legislature (
YEAR INT,
STATE varchar(30),
Legis_Control varchar(30),
Gov_Part varchar(30),
State_Control varchar(30));

select * from state_legislature;

create table unemployment_rate(
series_id varchar(30),
year INT,
value float);

select * from unemployment_rate;

create table population(
STATE VARCHAR(30),
ESTIMATEBASE2010 INT,
POPESTIMATE2010 INT,
POPESTIMATE2011 INT,
POPESTIMATE2012 INT,
POPESTIMATE2013 INT,
POPESTIMATE2014 INT,
POPESTIMATE2015 INT,
POPESTIMATE2016 INT,
POPESTIMATE2017 INT,
POPESTIMATE2018 INT,
POPESTIMATE2019 INT);

select * from population;