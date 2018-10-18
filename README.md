# py-teams-attachment

Uses the Webex Teams SDK to fetch attachments of all spaces for specified teams. 

#### Instructions

1. Generate and copy your personal API token from https://developer.webex.com/getting-started.html to the `token` variable in downloader.py
2. Run included `find_teams()` in downloader.py, or otherwise find the ids of the teams you wish to plunder and add them manually to the `teams` list in downloader.py
3. Run `pip install webexteamssdk`
4. Run `python downloader.py`

Files can be found in current directory named after the space they came from
