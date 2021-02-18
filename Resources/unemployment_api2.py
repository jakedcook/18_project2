import requests
import json
import prettytable
api_key = '1165a9ddaa564864b708f4412bfad4c3'
headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": ['LASST560000000000003'],
"startyear": '2010',"endyear":'2019'})
p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/?registrationkey=1165a9ddaa564864b708f4412bfad4c3/', data=data, headers=headers)
json_data = json.loads(p.text)
for series in json_data['Results']['series']:
    x=prettytable.PrettyTable(["series id","year","period","value","footnotes"])
    seriesId = series['seriesID']
    for item in series['data']:
        year = item['year']
        period = item['period']
        value = item['value']
        footnotes=""
        for footnote in item['footnotes']:
            if footnote:
                footnotes = footnotes + footnote['text'] + ','
            if 'M01' <= period <= 'M12':
                output = open(seriesId + '.csv','w')
                output.write (x.get_string())
                output.close()
