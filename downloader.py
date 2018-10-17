import urllib.request
import requests
import shutil
import json
from webexteamssdk import WebexTeamsAPI, ApiError

'''
Step 1: Replace token below with your own token from 
https://developer.webex.com/getting-started.html
'''
token = 'asdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdf'
api = WebexTeamsAPI(access_token=token)
headers = {'Authorization': 'Bearer '+token}

'''
Step 2: Use the find_teams() function to identify team(s) you wish to download from
You will add the relevant id(s) to the teams list
'''

def find_teams():
    response = requests.request("GET", "https://api.ciscospark.com/v1/teams", headers=headers)
    data = json.loads(response.text)['items']
    for team in data:
        try:
            print('Team Name: '+team['name']+'\nTeam id: '+team['id'])  
        except KeyError:
            pass

'''
Step 3: Collect your files in the current directory named after the title of the space!
'''
def save(file, title):
    req = urllib.request.Request(file, headers=headers)
    with urllib.request.urlopen(req) as response, open(title+' - '+response.info()['Content-Disposition'][21:].replace('"', ""), 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
        print('Saving: '+title+' - '+response.info()['Content-Disposition'][21:].replace('"', ""))

def download(teams):
    for team in teams:    
        spaces = api.rooms.list(teamId=team, type='group')
        for space in spaces:
            messages = api.messages.list(space.id)
            for message in messages:
                if message.files is not None:
                    try:
                        each = api.messages.get(message.id)
                        for file in each.files:
                            save(file, space.title)
                    except ApiError as e:
                        pass

teams = ['team1-id', 'team2-id']

find_teams() # Uncomment to list teams
download(teams) #Uncomment to bulk download attachments

