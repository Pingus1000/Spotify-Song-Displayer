import requests
import time
import sys
import os.path
from os import path

TOKEN = "A NICE TOKEN\'"

RefTOKEN = "Put here Refresh-Token"



params = (
    ('market', 'DE'),
)

refreshheaders = {
    'Authorization': 'Basic NGMyYTEwNDY3ZGNhNGI5OGJmMGJkMDYwNTlkMTQ0MjI6N2Y2ZjllNTllYmI2NDhmMmJjNGI0ZjJlNGUxMTBmMWY=',
}

refreshdata = {
  'grant_type': 'refresh_token',
  'refresh_token': RefTOKEN
}


print("Programm by Pingus1000")
while True:

    headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': "\'Bearer " + TOKEN,
    }
    print('---NEW REQUEST---')

    r = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=headers, params=params)
    print('RECIEVED DATA')
    print('STATUSCODE:')
    print(r.status_code)
    
    if(r.status_code == 204): #empty
        print("EMPTY RESPONSE")
        f = open("song_name.txt", "w")
        f.write("")
        f.close()
    
        #Write File for Artist
        f = open("artist_name.txt", "w")
        f.write("")
        f.close() 
        print('---END OF REQUEST---') 
        time.sleep(5)
    elif(r.status_code == 429): #Rate Limit
        
        print('To many Request!')
        f = open("song_name.txt", "w")
        f.write("I AM FLASH")
        f.close()
    
        #Write File for Artist
        f = open("artist_name.txt", "w")
        f.write("I AM TO FAST FOR SPOTIFY")
        f.close() 
        print('---END OF REQUEST---') 
        time.sleep(10)
    elif(r.status_code == 401): #Token expired
        print('Token expired')

        refresponse = requests.post('https://accounts.spotify.com/api/token', headers=refreshheaders, data=refreshdata)
        
        refdata = refresponse.json()
        
        
        TOKEN = refdata['access_token']
        

        

        
        print('---END OF REQUEST---') 
        
        time.sleep(1)
    elif(r.status_code == 200):
    
        data = r.json()
        print(data)
    
        songname = data['item']['name']
        SONGNAME = songname.upper()
        print('SONG: ' + SONGNAME)
        artist = data['item']['album']['artists'][0]['name']
        ARTIST = artist.upper()
        print('ARTIST: ' + ARTIST)
        print('---END OF REQUEST---')
    
        #Write File for Songname
        f = open("song_name.txt", "w")
        f.write(SONGNAME)
        f.close()
    
        #Write File for Artist
        f = open("artist_name.txt", "w")
        f.write(ARTIST)
        f.close()  
        time.sleep(1)
    else:
        sys.exit()