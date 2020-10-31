import requests
import json
import prettytable
api_key = '1165a9ddaa564864b708f4412bfad4c3'
headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": ['LASST010000000000003','LASST020000000000003','LASST040000000000003'
,'LASST050000000000003','LASST060000000000003','LASST080000000000003','LASST090000000000003'
,'LASST100000000000003','LASST110000000000003','LASST120000000000003','LASST130000000000003'
,'LASST150000000000003','LASST160000000000003','LASST170000000000003','LASST180000000000003'
,'LASST190000000000003','LASST200000000000003','LASST210000000000003','LASST220000000000003'
,'LASST230000000000003','LASST240000000000003','LASST250000000000003','LASST260000000000003'
,'LASST270000000000003','LASST280000000000003'],
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
            if 'M01' == period <= 'M01':
        output = open(seriesId + '.csv','w')
        output.write (x.get_string())
        output.close()