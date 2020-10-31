import requests
import json
import prettytable
api_key = '1165a9ddaa564864b708f4412bfad4c3'
headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": ['LASST290000000000003','LASST300000000000003'
,'LASST310000000000003','LASST320000000000003','LASST330000000000003','LASST340000000000003'
,'LASST350000000000003','LASST360000000000003','LASST370000000000003','LASST380000000000003'
,'LASST390000000000003','LASST400000000000003','LASST410000000000003','LASST420000000000003'
,'LASST440000000000003','LASST450000000000003','LASST460000000000003','LASST470000000000003'
,'LASST480000000000003','LASST490000000000003','LASST500000000000003','LASST510000000000003'
,'LASST530000000000003','LASST540000000000003','LASST550000000000003','LASST560000000000003'],
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