-- DROP TABLE population;
-- DROP TABLE State_Legislature;
-- DROP TABLE poverty_from_census;

CREATE TABLE population (
	STATE VARCHAR (20),
	ESTIMATESBASE2010 INT,
	POPESTIMATE2010 INT,
	POPESTIMATE2011 INT,
	POPESTIMATE2012 INT,
	POPESTIMATE2013 INT,
	POPESTIMATE2014 INT,
	POPESTIMATE2015 INT,
	POPESTIMATE2016 INT,
	POPESTIMATE2017 INT,	
	POPESTIMATE2018 INT,
	POPESTIMATE2019 INT
);

CREATE TABLE poverty_from_census (
    YEAR INT,
    STATE VARCHAR (20),
    Total INT,
    Below_poverty INT,
    Standard_error INT,
    Percent DECIMAL,
    Standard_error_v2 DECIMAL
);

CREATE TABLE State_Legislature (
    YEAR INT,
    STATE VARCHAR (20),
    Legis_Control VARCHAR (20) ,
    Gov_Party VARCHAR (20),
    State_Control VARCHAR (20)
);

-- DROP TABLE unemployment_rate

CREATE TABLE unemployment_rate (
    series_id VARCHAR (25),
	year INT, 
	period VARCHAR (20), 
	value DECIMAL	
);

