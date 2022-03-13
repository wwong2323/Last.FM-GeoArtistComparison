import requests
import json
import time


# Initilizing 
country_name = []
countries_info = requests.get('https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.json')
countries = countries_info.json()
for countryName in countries:
    country_name.append(countryName['name'])

    
     


#artist = input("Input an Artist's Name")

artist_name = []
listeners = []

def albuminfo():
    album_info = requests.post(f'http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={API_KEY}&artist=Terno Rei&album=Violeta&format=json')
    album = album_info.json()
    

    with open('album.json','w') as outfile:
        json.dump(album,outfile)

def topArtist():
    top_info = requests.post(f'http://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key={API_KEY}&format=json')
    top = json.loads(top_info.text)

    with open('topartist.json','w') as outfile:
        json.dump(top,outfile)
    
    for name in top['artists']['artist']:
        print(name['name'])

def geotopArtist():
    i = 0
    for c in country_name:
        geo_info = requests.post(f'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country={c}&limit=1&api_key={API_KEY}&format=json')
        geo = json.loads(geo_info.text)

        with open('geotopartists.json','w') as outfile:
            json.dump(geo,outfile)
        print(f'{c}')
        try:
            for name in geo['topartists']['artist']:
                
                artist_name.append((name['name']))
                listeners.append(name['listeners'])
                print(artist_name[i])
                i += 1
        except KeyError:
            pass 
    return None

geotopArtist()

print(artist_name[3])
