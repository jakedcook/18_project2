import os
from sqlalchemy import create_engine
import cgi, cgitb

def getPovertyRate(searchterm, db):
    result = []
    result_set = db.execute("SELECT array_agg(Percent ORDER BY year ASC) From poverty_from_census WHERE State=(%s);", (searchterm))
    for r in result_set:
        result.append(r[0])
        print(result)
    return(result)

def getPovertyRateYear(searchterm, db):
    result = []
    result_set = db.execute("SELECT array_agg(Year ORDER BY year ASC) From poverty_from_census WHERE State=(%s);", (searchterm))
    for r in result_set:
        result.append(r[0])
    return(result)
        
    
def getUnemploymentRate(searchterm, db):
    result = []
    result_set = db.execute("SELECT array_agg(value ORDER BY year ASC) FROM unemployment_rate WHERE series_id=(%s);", (searchterm))
    for r in (result_set):
        result.append(r[0])
    return(result)

def getUnemploymentRateYear(searchterm, db):
    result = []
    result_set = db.execute("SELECT array_agg(year ORDER BY year ASC) FROM unemployment_rate WHERE series_id=(%s);", (searchterm))
    for r in result_set:
        result.append(r[0])
    return(result)
     

def getStateLegislature(searchterm, db):
    result= []
    result_set = db.execute("SELECT array_agg(Legis_Control ORDER BY year ASC) FROM state_legislature WHERE State=(%s);", (searchterm))
    for r in result_set:
        result.append(r[0])
    return(result)

def getStateLegislatureYear(searchterm, db):
    result= []
    result_set = db.execute("SELECT array_agg(year ORDER BY year ASC) FROM state_legislature WHERE State=(%s);", (searchterm))
    for r in result_set:
        result.append(r[0])
    return(result)
       

def getPopulation(searchterm, db):
    result = []
    result_set = db.execute("SELECT POPESTIMATE2010,POPESTIMATE2011,POPESTIMATE2012,POPESTIMATE2013,POPESTIMATE2014,POPESTIMATE2015,POPESTIMATE2016,POPESTIMATE2017,POPESTIMATE2018,POPESTIMATE2019 FROM population WHERE State=(%s)", (searchterm))
    for r in result_set:
        result.append(r)
    return(result)

def getPopulationState(searchterm, db):
    result = []
    result_set = db.execute("SELECT STATE FROM population WHERE State=(%s)", (searchterm))
    for r in result_set:
        result.append(r[0])
    return(result)
    

def sql_data_from_input(state_name):

    db_string = 'postgresql+psycopg2://postgres:postgres@localhost/project2_data'
    db = create_engine(db_string)

    poverty_rate = getPovertyRate(state_name, db)
    unemployment_rate = getUnemploymentRate(state_name, db)
    state_legislature = getStateLegislature(state_name, db)
    population = getPopulation(state_name, db)

    poverty_rate_year = getPovertyRateYear(state_name, db)
    unemployment_rate_year = getUnemploymentRateYear(state_name, db)
    state_legislature_year = getStateLegislatureYear(state_name, db)
    population_state = getPopulationState(state_name, db)

    

    result = dict()
    result['poverty_rate']= poverty_rate
    result['unemployment_rate'] = unemployment_rate
    result['state_legislature'] = state_legislature
    result['population'] = population
    result['poverty_rate_year'] = poverty_rate_year
    result['unemployment_rate_year'] = unemployment_rate_year
    result['state_legislature_year'] = state_legislature_year
    result['population_state'] = population_state

   
    return(result)
