# Hackathon: Women in Sports Data 2023
# Author: Isabella Couto Carlos
# Date: 7/29/23

# Importing data (AWS)

## Installing packages and importing libraries

%pip install boto3
%pip install jsonlines
%pip install jsonlines pandas

import boto3
import jsonlines
import pandas as pd
import json

## Accessing AWS 3

# Replace with your credentials
session = boto3.Session(
    aws_access_key_id='AKIA6KMLMMGZJ6CNEF5X',
    aws_secret_access_key='PnWB9kCglrwRFn2zmv0kMq7nhduN2vIYhyORnkG0'
)

s3_client = session.client('s3')

response = s3_client.list_objects(Bucket='sportradar-wisd-data')
for obj in response['Contents']:
    print(obj['Key'])

## Importing data

### Events

keyname = "games/0042100301/0042100301_events.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d1 = pd.DataFrame(data)
d1['nbaId'] = 42100301

keyname = "games/0042100302/0042100302_events.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d3 = pd.DataFrame(data)
d3['nbaId'] = 42100302

keyname = "games/0042100303/0042100303_events.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d5 = pd.DataFrame(data)
d5['nbaId'] = 42100303

keyname = "games/0042100304/0042100304_events.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d7 = pd.DataFrame(data)
d7['nbaId'] = 42100304

keyname = "games/0042100305/0042100305_events.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d9 = pd.DataFrame(data)
d9['nbaId'] = 42100305

keyname = "games/0042100306/0042100306_events.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d11 = pd.DataFrame(data)
d11['nbaId'] = 42100306

keyname = "games/0042100307/0042100307_events.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d13 = pd.DataFrame(data)
d13['nbaId'] = 42100307

keyname = "games/0042100311/0042100311_events.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d15 = pd.DataFrame(data)
d15['nbaId'] = 42100311

keyname = "games/0042100312/0042100312_events.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d17 = pd.DataFrame(data)
d17['nbaId'] = 42100312

keyname = "games/0042100313/0042100313_events.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d19 = pd.DataFrame(data)
d19['nbaId'] = 42100313

keyname = "games/0042100314/0042100314_events.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d21 = pd.DataFrame(data)
d21['nbaId'] = 42100314

keyname = "games/0042100315/0042100315_events.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d23 = pd.DataFrame(data)
d23['nbaId'] = 42100315

keyname = "games/0042100401/0042100401_events.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d25 = pd.DataFrame(data)
d25['nbaId'] = 42100401

keyname = "games/0042100402/0042100402_events.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d27 = pd.DataFrame(data)
d27['nbaId'] = 42100402

keyname = "games/0042100403/0042100403_events.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d29 = pd.DataFrame(data)
d29['nbaId'] = 42100403

keyname = "games/0042100404/0042100404_events.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d31 = pd.DataFrame(data)
d31['nbaId'] = 42100404

keyname = "games/0042100405/0042100405_events.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d33 = pd.DataFrame(data)
d33['nbaId'] = 42100405

keyname = "games/0042100406/0042100406_events.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d35 = pd.DataFrame(data)
d35['nbaId'] = 42100406

events = pd.concat([d1, d3, d5, d7, d9, d11, d13, d15, d17, d19, d21, d23, d25, d27, d29, d31, d33, d35])

events.head()

# Tranforming the players columns into 5 players columns

events[['homePlayer1', 'homePlayer2', 'homePlayer3', 'homePlayer4', 'homePlayer5']] = pd.DataFrame(events['homePlayers'].tolist())
events[['awayPlayer1', 'awayPlayer2', 'awayPlayer3', 'awayPlayer4', 'awayPlayer5']] = pd.DataFrame(events['awayPlayers'].tolist())

columns_to_drop = ['homePlayers', 'awayPlayers']
events.drop(columns_to_drop, axis=1, inplace=True)

events.columns

# Saving events table (optional)
#events.to_csv(r"events.csv", index=False)

### Tracking

keyname = "games/0042100301/0042100301_tracking.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d2 = pd.DataFrame(data)
d2['nbaId'] = 42100301

keyname = "games/0042100302/0042100302_tracking.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d4 = pd.DataFrame(data)
d4['nbaId'] = 42100302

keyname = "games/0042100303/0042100303_tracking.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d6 = pd.DataFrame(data)
d6['nbaId'] = 42100303

keyname = "games/0042100304/0042100304_tracking.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d8 = pd.DataFrame(data)
d8['nbaId'] = 42100304

keyname = "games/0042100305/0042100305_tracking.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d10 = pd.DataFrame(data)
d10['nbaId'] = 42100305

keyname = "games/0042100306/0042100306_tracking.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d12 = pd.DataFrame(data)
d12['nbaId'] = 42100306

keyname = "games/0042100307/0042100307_tracking.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d14 = pd.DataFrame(data)
d14['nbaId'] = 42100307

keyname = "games/0042100311/0042100311_tracking.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d16 = pd.DataFrame(data)
d16['nbaId'] = 42100311

keyname = "games/0042100312/0042100312_tracking.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d18 = pd.DataFrame(data)
d18['nbaId'] = 42100312

keyname = "games/0042100313/0042100313_tracking.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d20 = pd.DataFrame(data)
d20['nbaId'] = 42100313

keyname = "games/0042100314/0042100314_tracking.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d22 = pd.DataFrame(data)
d22['nbaId'] = 42100314

keyname = "games/0042100315/0042100315_tracking.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d24 = pd.DataFrame(data)
d24['nbaId'] = 42100315

keyname = "games/0042100401/0042100401_tracking.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d26 = pd.DataFrame(data)
d26['nbaId'] = 42100401

keyname = "games/0042100402/0042100402_tracking.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d28 = pd.DataFrame(data)
d28['nbaId'] = 42100402

keyname = "games/0042100403/0042100403_tracking.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d30 = pd.DataFrame(data)
d30['nbaId'] = 42100403

keyname = "games/0042100404/0042100404_tracking.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d32 = pd.DataFrame(data)
d32['nbaId'] = 42100404

keyname = "games/0042100405/0042100405_tracking.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d34 = pd.DataFrame(data)
d34['nbaId'] = 42100405

keyname = "games/0042100406/0042100406_tracking.jsonl"

data = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

d36 = pd.DataFrame(data)
d36['nbaId'] = 42100406

tracking = pd.concat([d2, d4, d6, d8, d10, d12, d14, d16, d18, d20, d22, d24, d26, d28, d30, d32, d34, d36])

tracking[['homePlayer1', 'homePlayer2', 'homePlayer3', 'homePlayer4', 'homePlayer5']] = pd.DataFrame(tracking['homePlayers'].tolist())
tracking[['awayPlayer1', 'awayPlayer2', 'awayPlayer3', 'awayPlayer4', 'awayPlayer5']] = pd.DataFrame(tracking['awayPlayers'].tolist())

columns_to_drop = ['homePlayers','awayPlayers']
tracking.drop(columns_to_drop, axis=1, inplace=True)

tracking.head()

tracking[['xyz1', 'jersey1', 'playerID1']] = pd.DataFrame(tracking['homePlayer1'].tolist())
tracking[['xyz2', 'jersey2', 'playerID2']] = pd.DataFrame(tracking['homePlayer2'].tolist())
tracking[['xyz3', 'jersey3', 'playerID3']] = pd.DataFrame(tracking['homePlayer3'].tolist())
tracking[['xyz4', 'jersey4', 'playerID4']] = pd.DataFrame(tracking['homePlayer4'].tolist())
tracking[['xyz5', 'jersey5', 'playerID5']] = pd.DataFrame(tracking['homePlayer5'].tolist())

tracking[['away_xyz1', 'away_jersey1', 'away_playerID1']] = pd.DataFrame(tracking['awayPlayer1'].tolist())
tracking[['away_xyz2', 'away_jersey2', 'away_playerID2']] = pd.DataFrame(tracking['awayPlayer2'].tolist())
tracking[['away_xyz3', 'away_jersey3', 'away_playerID3']] = pd.DataFrame(tracking['awayPlayer3'].tolist())
tracking[['away_xyz4', 'away_jersey4', 'away_playerID4']] = pd.DataFrame(tracking['awayPlayer4'].tolist())
tracking[['away_xyz5', 'away_jersey5', 'away_playerID5']] = pd.DataFrame(tracking['awayPlayer5'].tolist())

tracking.columns

columns_to_drop = ['homePlayer1', 'homePlayer2',
       'homePlayer3', 'homePlayer4', 'homePlayer5', 'awayPlayer1',
       'awayPlayer2', 'awayPlayer3', 'awayPlayer4', 'awayPlayer5']
tracking.drop(columns_to_drop, axis=1, inplace=True)

tracking = tracking.rename(columns={'xyz1': 'home_xyz1', 
                                    'jersey1': 'home_jersey1',
                                    'playerID1': 'homePlayer1',
                                    'xyz2': 'home_xyz2', 
                                    'jersey2': 'home_jersey2',
                                    'playerID2': 'homePlayer2',
                                    'xyz3': 'home_xyz3', 
                                    'jersey3': 'home_jersey3',
                                    'playerID3': 'homePlayer3',
                                    'xyz4': 'home_xyz4', 
                                    'jersey4': 'home_jersey4',
                                    'playerID4': 'homePlayer4',
                                    'xyz5': 'home_xyz5', 
                                    'jersey5': 'home_jersey5',
                                    'playerID5': 'homePlayer5',
                                    'away_playerID1': 'awayPlayer1',
                                    'away_playerID2': 'awayPlayer2',
                                    'away_playerID3': 'awayPlayer3',
                                    'away_playerID4': 'awayPlayer4',
                                    'away_playerID5': 'awayPlayer5',
                                    })

# Saving tacking table (optional)
#tracking.to_csv(r"tracking.csv", index=False)

### Games

keyname = "metadata/games.json"
games = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

games = pd.DataFrame(games[0]['games'])

games.head()

# Filtering the games we are evaluating in the analysis

games2 = games[(games['nbaId'] == '0042100301') |
               (games['nbaId'] == '0042100302') |
               (games['nbaId'] == '0042100303') |
               (games['nbaId'] == '0042100304') |
               (games['nbaId'] == '0042100305') |
               (games['nbaId'] == '0042100306') |
               (games['nbaId'] == '0042100307') |
               (games['nbaId'] == '0042100311') |
               (games['nbaId'] == '0042100312') |
               (games['nbaId'] == '0042100313') |
               (games['nbaId'] == '0042100314') |
               (games['nbaId'] == '0042100315') |
               (games['nbaId'] == '0042100401') |
               (games['nbaId'] == '0042100402') |
               (games['nbaId'] == '0042100403') |
               (games['nbaId'] == '0042100404') |
               (games['nbaId'] == '0042100405') |
               (games['nbaId'] == '0042100406')]

# Saving games table (optional)
games2.to_csv(r"games2.csv", index=False)

### Players

keyname = "metadata/players.json"
players = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

players[0]['players']

players = pd.DataFrame(players[0]['players'])

players.head()

# Saving players table (optional)
players.to_csv(r"players.csv", index=False)

### Teams

keyname = "metadata/teams.json"
teams = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

teams[0]['teams']

teams = pd.DataFrame(teams[0]['teams'])

teams.head()

# Saving teams table (optional)
teams.to_csv(r"teams.csv", index=False)

## Cleaning tables

### Tracking

# Opening saved table
tracking = pd.read_csv(r"tracking.csv")

tracking.info()

tracking[['home_x1', 'home_y1','home_z1']] = tracking['home_xyz1'].str.split(', ', expand=True)
tracking[['home_x2', 'home_y2','home_z2']] = tracking['home_xyz2'].str.split(', ', expand=True)
tracking[['home_x3', 'home_y3','home_z3']] = tracking['home_xyz3'].str.split(', ', expand=True)
tracking[['home_x4', 'home_y4','home_z4']] = tracking['home_xyz4'].str.split(', ', expand=True)
tracking[['home_x5', 'home_y5','home_z5']] = tracking['home_xyz5'].str.split(', ', expand=True)

tracking[['away_x1', 'away_y1','away_z1']] = tracking['away_xyz1'].str.split(', ', expand=True)
tracking[['away_x2', 'away_y2','away_z2']] = tracking['away_xyz2'].str.split(', ', expand=True)
tracking[['away_x3', 'away_y3','away_z3']] = tracking['away_xyz3'].str.split(', ', expand=True)
tracking[['away_x4', 'away_y4','away_z4']] = tracking['away_xyz4'].str.split(', ', expand=True)
tracking[['away_x5', 'away_y5','away_z5']] = tracking['away_xyz5'].str.split(', ', expand=True)

tracking.head()

tracking['home_x1'] = tracking['home_x1'].str.split('[').str[-1]
tracking['home_z1'] = tracking['home_z1'].str.split(']').str[0]
tracking['home_x2'] = tracking['home_x2'].str.split('[').str[-1]
tracking['home_z2'] = tracking['home_z2'].str.split(']').str[0]
tracking['home_x3'] = tracking['home_x3'].str.split('[').str[-1]
tracking['home_z3'] = tracking['home_z3'].str.split(']').str[0]
tracking['home_x4'] = tracking['home_x4'].str.split('[').str[-1]
tracking['home_z4'] = tracking['home_z4'].str.split(']').str[0]
tracking['home_x5'] = tracking['home_x5'].str.split('[').str[-1]
tracking['home_z5'] = tracking['home_z5'].str.split(']').str[0]

tracking['away_x1'] = tracking['away_x1'].str.split('[').str[-1]
tracking['away_z1'] = tracking['away_z1'].str.split(']').str[0]
tracking['away_x2'] = tracking['away_x2'].str.split('[').str[-1]
tracking['away_z2'] = tracking['away_z2'].str.split(']').str[0]
tracking['away_x3'] = tracking['away_x3'].str.split('[').str[-1]
tracking['away_z3'] = tracking['away_z3'].str.split(']').str[0]
tracking['away_x4'] = tracking['away_x4'].str.split('[').str[-1]
tracking['away_z4'] = tracking['away_z4'].str.split(']').str[0]
tracking['away_x5'] = tracking['away_x5'].str.split('[').str[-1]
tracking['away_z5'] = tracking['away_z5'].str.split(']').str[0]

tracking.head()

tracking['home_x1'] = tracking['home_x1'].astype(float)
tracking['home_z1'] = tracking['home_z1'].astype(float)
tracking['home_x2'] = tracking['home_x2'].astype(float)
tracking['home_z2'] = tracking['home_z2'].astype(float)
tracking['home_x3'] = tracking['home_x3'].astype(float)
tracking['home_z3'] = tracking['home_z3'].astype(float)
tracking['home_x4'] = tracking['home_x4'].astype(float)
tracking['home_z4'] = tracking['home_z4'].astype(float)
tracking['home_x5'] = tracking['home_x5'].astype(float)
tracking['home_z5'] = tracking['home_z5'].astype(float)

tracking['away_x1'] = tracking['away_x1'].astype(float)
tracking['away_z1'] = tracking['away_z1'].astype(float)
tracking['away_x2'] = tracking['away_x2'].astype(float)
tracking['away_z2'] = tracking['away_z2'].astype(float)
tracking['away_x3'] = tracking['away_x3'].astype(float)
tracking['away_z3'] = tracking['away_z3'].astype(float)
tracking['away_x4'] = tracking['away_x4'].astype(float)
tracking['away_z4'] = tracking['away_z4'].astype(float)
tracking['away_x5'] = tracking['away_x5'].astype(float)
tracking['away_z5'] = tracking['away_z5'].astype(float)

tracking['away_y1'] = tracking['away_y1'].astype(float)
tracking['away_y2'] = tracking['away_y2'].astype(float)
tracking['away_y3'] = tracking['away_y3'].astype(float)
tracking['away_y4'] = tracking['away_y4'].astype(float)
tracking['away_y5'] = tracking['away_y5'].astype(float)
tracking['home_y1'] = tracking['home_y1'].astype(float)
tracking['home_y2'] = tracking['home_y2'].astype(float)
tracking['home_y3'] = tracking['home_y3'].astype(float)
tracking['home_y4'] = tracking['home_y4'].astype(float)
tracking['home_y5'] = tracking['home_y5'].astype(float)

tracking[['ball_x', 'ball_y','ball_z']] = tracking['ball'].str.split(', ', expand=True)

tracking['ball_z'] = tracking['ball_z'].str.split(']').str[0]
tracking['ball_x'] = tracking['ball_x'].str.split('[').str[-1]

tracking['ball_x'] = tracking['ball_x'].astype(float)
tracking['ball_z'] = tracking['ball_z'].astype(float)

tracking.columns

columns_to_drop = ['ball', 'home_xyz1', 'home_xyz2', 'home_xyz3', 'home_xyz4', 'home_xyz5',
                  'away_xyz1', 'away_xyz2', 'away_xyz3', 'away_xyz4', 'away_xyz5',]
tracking.drop(columns_to_drop, axis=1, inplace=True)

# Saving tacking table (optional)
#tracking.to_csv(r"trackings.csv", index=False)

# Importing PlayByPlay NBA API

Reference: https://github.com/swar/nba_api/tree/master/src/nba_api/stats/endpoints

## Installing packages and importing libraries

%pip install nba_api

import pandas as pd
import requests
import jsonlines
import json
import numpy as np

from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import EndPeriod, StartPeriod 
import pandas as pd

## Importing data

class PlayByPlay(Endpoint):
    endpoint = 'playbyplay'
    expected_data = {'AvailableVideo': ['VIDEO_AVAILABLE_FLAG'], 'PlayByPlay': ['GAME_ID', 'EVENTNUM', 'EVENTMSGTYPE', 'EVENTMSGACTIONTYPE', 'PERIOD', 'WCTIMESTRING', 'PCTIMESTRING', 'HOMEDESCRIPTION', 'NEUTRALDESCRIPTION', 'VISITORDESCRIPTION', 'SCORE', 'SCOREMARGIN']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None
    

    def __init__(self,
                 game_id,
                 end_period=EndPeriod.default,
                 start_period=StartPeriod.default,
                 proxy=None,
                 headers=None,
                 timeout=30,
                 get_request=True):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
                'GameID': game_id,
                'EndPeriod': end_period,
                'StartPeriod': start_period
        }
        if get_request:
            self.get_request()
    
    def get_request(self):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters=self.parameters,
            proxy=self.proxy,
            headers=self.headers,
            timeout=self.timeout,
        )
        self.load_response()
        
    def load_response(self):
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.available_video = Endpoint.DataSet(data=data_sets['AvailableVideo'])
        self.play_by_play = Endpoint.DataSet(data=data_sets['PlayByPlay'])
        
        
        self.list_tot = []
        
        self.list = list(data_sets['PlayByPlay']['headers'])
        self.list_tot.append(self.list)
        
        #self.list_body = []
        i = 0
        while i <= len(data_sets['PlayByPlay']['data'])-1:
            self.new = data_sets['PlayByPlay']['data'][i]
            self.list_tot.append(self.new)
            i = i+1
        
        self.df2 = pd.DataFrame(columns=self.list_tot)
        self.df2.to_csv(r"playbyplay1.csv", index=False)

# Insert here the id of the game you need to import info about

data = PlayByPlay("0042100301")

# Importing screen data (file in Github)

## Importing libraries

import pandas as pd
import numpy as np

## Merging tracking and events playbyplay

### Cleaning tracking

tracking = pd.read_csv(r"trackings.csv")

tracking.columns

tracking = tracking[['frameIdx', 'period', 'gameClock', 'gameClockStopped', 
                     'shotClock', 'wallClock', 'nbaId', 'ball_x', 'ball_y', 'ball_z', 
                     'homePlayer1', 'homePlayer2', 'homePlayer3', 'homePlayer4', 'homePlayer5', 
                     'awayPlayer1', 'awayPlayer2', 'awayPlayer3', 'awayPlayer4', 'awayPlayer5', 
                     'home_x1', 'home_y1', 'home_x2', 'home_y2', 'home_x3', 'home_y3', 
                     'home_x4', 'home_y4', 'home_x5', 'home_y5', 
                     'away_x1', 'away_y1', 'away_x2', 'away_y2', 'away_x3', 'away_y3', 
                     'away_x4', 'away_y4', 'away_x5', 'away_y5']].copy()

tracking.head()

# Filtering the game we analyzing
tracking1 = tracking[tracking['nbaId']==42100301].copy()

### Cleaning events playbyplay

eventspbp = pd.read_csv(r"eventspbp1.csv")

eventspbp.columns

eventspbp1 = eventspbp[['gameId', 'nbaId', 'pbpId', 'period', 'shotClock', 'gameClock',
       'wallClock', 'eventType', 'playerId', 'HOMEDESCRIPTION',
       'NEUTRALDESCRIPTION', 'VISITORDESCRIPTION', 'SHOTRESULT', 'SHOTRESULT2', 'shotType', 'VISITORSCOREACUM', 'HOMESCOREACUM']].copy()

eventspbp1.head()

### Merging tracking and events playbyplay

trackeventspbp = pd.merge(tracking1, eventspbp1, on=['wallClock','nbaId','period','gameClock'], how='outer')

trackeventspbp.columns

trackeventspbp = trackeventspbp[['frameIdx', 'nbaId', 'gameId', 'pbpId', 'wallClock', 
                'gameClockStopped', 'period', 'gameClock', 'shotClock_x', 
                'eventType', 'playerId', 'SHOTRESULT', 'SHOTRESULT2', 'shotType','VISITORSCOREACUM', 'HOMESCOREACUM',
                'ball_x', 'ball_y', 'ball_z', 
                'home_x1', 'home_y1', 'home_x2', 'home_y2', 'home_x3', 'home_y3', 'home_x4', 'home_y4', 'home_x5', 'home_y5', 
                'away_x1', 'away_y1', 'away_x2', 'away_y2', 'away_x3', 'away_y3', 'away_x4', 'away_y4', 'away_x5', 'away_y5',
                'homePlayer1', 'homePlayer2', 'homePlayer3', 'homePlayer4', 'homePlayer5',
                'awayPlayer1', 'awayPlayer2', 'awayPlayer3', 'awayPlayer4', 'awayPlayer5'
               ]].copy()

trackeventspbp.columns

i = 0
while trackeventspbp['gameClockStopped'][i] != False:
    trackeventspbp = trackeventspbp.drop(i)
    i = i+1

# Saving (optional)
trackeventspbp.to_csv(r"trackeventspbp.csv", index=False)

## Naming the Teams

games = pd.read_csv(r"games2.csv")
teams = pd.read_csv(r"teams.csv")

teams.head()

gamehometeam = pd.merge(games[games['nbaId'] == 42100301], teams, left_on=['homeTeamId'], right_on=['id'], how='left')

gameawayteam = pd.merge(games[games['nbaId'] == 42100301], teams, left_on=['awayTeamId'], right_on=['id'], how='left')

gamehometeam['teamStatus'] = 'home'

gamehometeam

gamehometeam = gamehometeam.rename(columns={'nbaId_x': 'gameId',
                                           'id_y': 'teamId'})

gameawayteam['teamStatus'] = 'away'

gameawayteam

gameawayteam = gameawayteam.rename(columns={'nbaId_x': 'gameId',
                                           'id_y': 'teamId'})

gamehometeam = gamehometeam[['gameId', 'teamId', 'name', 'abbrev', 'teamStatus']].copy()

gameawayteam = gameawayteam[['gameId', 'teamId', 'name', 'abbrev', 'teamStatus']].copy()

gameteams = pd.concat([gamehometeam, gameawayteam])

gameteams

## Players

players = pd.read_csv(r"players.csv")

players.head()

players['fullName'] = players['firstName'] + " " + players['lastName']

players.head()

players = players[['id', 'position', 'lastName', 'fullName']].copy()

## Opening screen data

# Calling the file in Github
url = 'https://github.com/isabellaccarloss/wisd_boston23/raw/main/screens_mapping.xlsx'
screens = pd.read_excel(url)

screens.columns

screens1 = screens[['nbaId', 'homeTeamId', 'awayTeamId', 'period',
                    'gameClock', 'shotClock',
                    'player_screen_id', 'player_w_ball_id']].copy()

screens1.head()

# Creating Screen Id

i = 0
listindex = []

while i < len(screens1):
    index = str(screens1['nbaId'][i]) + "00" + str(i) if len(str(i)) > 1 else str(screens1['nbaId'][i]) + "00" + "0" + str(i)
    listindex.append(index)
    i = i + 1

screens1['screenId'] = listindex

screens1.head()

## Merging screen data and trackeventspbp

# Importing if necessary
#trackeventspbp = pd.read_csv(r"trackeventspbp.csv")

trackeventspbp.columns

periodlist = screens1['period'].tolist()
gameclocklist = screens1['gameClock'].tolist()

k = 0
i = 0
j = 0

result_df = pd.DataFrame()

while k < len(screens1):
    
    periodfilt = periodlist[i]
    timefilter = gameclocklist[k]
    
    df = trackeventspbp[(trackeventspbp['period']==periodfilt) & 
                (trackeventspbp['gameClock'] <= timefilter+1) &
                (trackeventspbp['gameClock'] >= timefilter-1)]
    df.loc[:, 'screenId'] = screens1['screenId'][j]

    result_df = pd.concat([result_df, df])
    
    i = i + 1
    k = k + 1
    j = j + 1
    
trackeventspbpfilt = result_df

trackeventspbpfilt.head()

trackeventspbpfilt.columns

screentable1 = pd.merge(trackeventspbpfilt, screens1, on='screenId')

columns_to_drop = ['nbaId_y', 'period_y', 'shotClock']
screentable1.drop(columns_to_drop, axis=1, inplace=True)

screentable1 = screentable1.rename(columns={'nbaId_x': 'nbaId',
                                            'period_x': 'period',
                                            'gameClock_x': 'gameClock',
                                            'shotClock_x': 'shotClock',
                                            'gameClock_y': 'gameClockfrozenScreen'})

screentable1.columns

# Save if necessary
#screentable1.to_csv(r"screentable1_42100301.csv", index=False)

## Rebuilding screen table to get the exact screen moment

### Creating position table

#Importing if necessary
#screentable1 = pd.read_csv(r"screentable1_42100301.csv")

positiontable = screentable1[['nbaId', 'period', 'gameClock', 'screenId',
                              'home_x1', 'home_x2', 'home_x3', 'home_x4', 'home_x5',
                              'away_x1', 'away_x2', 'away_x3', 'away_x4', 'away_x5',
                              'home_y1', 'home_y2', 'home_y3', 'home_y4', 'home_y5',
                              'away_y1', 'away_y2', 'away_y3', 'away_y4', 'away_y5']].copy()

positiontable = positiontable.rename(columns={'home_x1': 'homePlayer1_x',
                                                'home_x2': 'homePlayer2_x',
                                                'home_x3': 'homePlayer3_x',
                                                'home_x4': 'homePlayer4_x',
                                                'home_x5': 'homePlayer5_x',
                                                'away_x1': 'awayPlayer1_x',
                                                'away_x2': 'awayPlayer2_x',
                                                'away_x3': 'awayPlayer3_x',
                                                'away_x4': 'awayPlayer4_x',
                                                'away_x5': 'awayPlayer5_x',
                                                'home_y1': 'homePlayer1_y',
                                                'home_y2': 'homePlayer2_y',
                                                'home_y3': 'homePlayer3_y',
                                                'home_y4': 'homePlayer4_y',
                                                'home_y5': 'homePlayer5_y',
                                                'away_y1': 'awayPlayer1_y',
                                                'away_y2': 'awayPlayer2_y',
                                                'away_y3': 'awayPlayer3_y',
                                                'away_y4': 'awayPlayer4_y',
                                                'away_y5': 'awayPlayer5_y'})

positiontable.head()

playerclassiftable = pd.melt(screentable1, id_vars=['screenId'], 
                        value_vars=['homePlayer1', 'homePlayer2', 'homePlayer3', 'homePlayer4', 'homePlayer5', 
                                    'awayPlayer1', 'awayPlayer2', 'awayPlayer3', 'awayPlayer4', 'awayPlayer5'], 
                        var_name='playerClassification')

playerclassiftable.drop_duplicates(inplace=True)

playerclassiftable.head()

# Getting what's the classification of the screener and baller

screenerballer = pd.melt(screentable1, id_vars=['screenId'], 
                        value_vars=['player_screen_id', 'player_w_ball_id'], 
                        var_name='playerClassification')

screenerballer.drop_duplicates(inplace=True)

screenerballer

screenerballer1 = pd.merge(screenerballer, playerclassiftable, on=['screenId','value'], how='left')

# Getting x value
screenerballer2 = screenerballer1[screenerballer1['playerClassification_x']=='player_screen_id'].copy()
# Getting y value
screenerballer3 = screenerballer1[screenerballer1['playerClassification_x']=='player_w_ball_id'].copy()

positiontable.head()

positiontable1 = pd.merge(positiontable, screenerballer2, on=['screenId'], how='left')

positiontable1 = positiontable1.rename(columns={'playerClassification_y': 'player_screen'})

columns_to_drop = ['playerClassification_x', 'value']
positiontable1.drop(columns_to_drop, axis=1, inplace=True)

positiontable1.head()

positiontable1 = pd.merge(positiontable1, screenerballer3, on=['screenId'], how='left')

positiontable1 = positiontable1.rename(columns={'playerClassification_y': 'player_w_ball'})

columns_to_drop = ['playerClassification_x', 'value']
positiontable1.drop(columns_to_drop, axis=1, inplace=True)

positiontable1

i = 0
distancescreenballer = []

while i < len(positiontable1):
    
    columnscreenerx = positiontable1['player_screen'][i] + "_x"
    columnscreenery = positiontable1['player_screen'][i] + "_y"
    columnballerx = positiontable1['player_w_ball'][i] + "_x"
    columnballery = positiontable1['player_w_ball'][i] + "_y"
    distancescreenballer.append(np.sqrt((positiontable1[columnscreenerx][i] - positiontable1[columnballerx][i])**2 + (positiontable1[columnscreenery][i] - positiontable1[columnballery][i])**2))

    i = i + 1
    
positiontable1['distancescreenballer'] = distancescreenballer

positiontable1.head()

# Getting the min distance between screener and baller

positiontablemin = positiontable1.groupby(['screenId','player_screen','player_w_ball'])['distancescreenballer'].min().reset_index()

positiontablemin.head()

# Merge the result back

screentabletrack = pd.merge(positiontablemin, positiontable1, on=['screenId', 'distancescreenballer', 'player_screen', 'player_w_ball'], how='left')

columns_to_drop = ['distancescreenballer']
screentabletrack.drop(columns_to_drop, axis=1, inplace=True)

screentabletrack.head()

### Getting the row with the closest the Baller and Screener

i = 0
distancescreen1 = []
distancescreen2 = []
distancescreen3 = []
distancescreen4 = []
distancescreen5 = []

while i < len(screentabletrack):
    
    if screentabletrack['player_screen'][i][:4] == 'home':
        
        columnnamex = screentabletrack['player_screen'][i] + "_x"
        columnnamey = screentabletrack['player_screen'][i] + "_y"
        distancescreen1.append(np.sqrt((screentabletrack[columnnamex][i] - screentabletrack['awayPlayer1_x'][i])**2 + (screentabletrack[columnnamey][i] - screentabletrack['awayPlayer1_y'][i])**2))
        distancescreen2.append(np.sqrt((screentabletrack[columnnamex][i] - screentabletrack['awayPlayer2_x'][i])**2 + (screentabletrack[columnnamey][i] - screentabletrack['awayPlayer2_y'][i])**2))
        distancescreen3.append(np.sqrt((screentabletrack[columnnamex][i] - screentabletrack['awayPlayer3_x'][i])**2 + (screentabletrack[columnnamey][i] - screentabletrack['awayPlayer3_y'][i])**2))
        distancescreen4.append(np.sqrt((screentabletrack[columnnamex][i] - screentabletrack['awayPlayer4_x'][i])**2 + (screentabletrack[columnnamey][i] - screentabletrack['awayPlayer4_y'][i])**2))
        distancescreen5.append(np.sqrt((screentabletrack[columnnamex][i] - screentabletrack['awayPlayer5_x'][i])**2 + (screentabletrack[columnnamey][i] - screentabletrack['awayPlayer5_y'][i])**2))
        
    else:

        columnnamex = screentabletrack['player_screen'][i] + "_x"
        columnnamey = screentabletrack['player_screen'][i] + "_y"
        distancescreen1.append(np.sqrt((screentabletrack[columnnamex][i] - screentabletrack['homePlayer1_x'][i])**2 + (screentabletrack[columnnamey][i] - screentabletrack['homePlayer1_y'][i])**2))
        distancescreen2.append(np.sqrt((screentabletrack[columnnamex][i] - screentabletrack['homePlayer2_x'][i])**2 + (screentabletrack[columnnamey][i] - screentabletrack['homePlayer2_y'][i])**2))
        distancescreen3.append(np.sqrt((screentabletrack[columnnamex][i] - screentabletrack['homePlayer3_x'][i])**2 + (screentabletrack[columnnamey][i] - screentabletrack['homePlayer3_y'][i])**2))
        distancescreen4.append(np.sqrt((screentabletrack[columnnamex][i] - screentabletrack['homePlayer4_x'][i])**2 + (screentabletrack[columnnamey][i] - screentabletrack['homePlayer4_y'][i])**2))
        distancescreen5.append(np.sqrt((screentabletrack[columnnamex][i] - screentabletrack['homePlayer5_x'][i])**2 + (screentabletrack[columnnamey][i] - screentabletrack['homePlayer5_y'][i])**2))

    i = i + 1

screentabletrack['Player1'] = distancescreen1
screentabletrack['Player2'] = distancescreen2
screentabletrack['Player3'] = distancescreen3
screentabletrack['Player4'] = distancescreen4
screentabletrack['Player5'] = distancescreen5

screentabletrack.head()

screentabletrack['pscreencloser1'] = screentabletrack[['Player1','Player2','Player3','Player4','Player5']].idxmin(axis=1)
screentabletrack['pscreencloser2'] = screentabletrack[['Player1','Player2','Player3','Player4','Player5']].apply(lambda row: row.nsmallest(2).idxmax(), axis=1)

screentabletrack.head()

i = 0
pscreencloser1 = []
pscreencloser2 = []

while i < len(screentabletrack):
    
    if screentabletrack['player_screen'][i][:4] == 'home':
        
        pscreencloser1.append(screentabletrack['pscreencloser1'][i].replace("P", "awayP"))
        pscreencloser2.append(screentabletrack['pscreencloser2'][i].replace("P", "awayP"))
        
    else:
        
        pscreencloser1.append(screentabletrack['pscreencloser1'][i].replace("P", "homeP"))
        pscreencloser2.append(screentabletrack['pscreencloser2'][i].replace("P", "homeP"))
        
    i = i + 1
    
screentabletrack['pscreencloser1'] = pscreencloser1
screentabletrack['pscreencloser2'] = pscreencloser2

columns_to_drop = ['Player1','Player2','Player3','Player4','Player5']
screentabletrack.drop(columns_to_drop, axis=1, inplace=True)

screentabletrack.head()

i = 0
distanceballer1 = []
distanceballer2 = []
distanceballer3 = []
distanceballer4 = []
distanceballer5 = []

while i < len(screentabletrack):
    
    if screentabletrack['player_w_ball'][i][:4] == 'home':
        
        columnnamex = screentabletrack['player_w_ball'][i] + "_x"
        columnnamey = screentabletrack['player_w_ball'][i] + "_y"
        distanceballer1.append(np.sqrt((screentabletrack[columnnamex][i] - screentabletrack['awayPlayer1_x'][i])**2 + (screentabletrack[columnnamey][i] - screentabletrack['awayPlayer1_y'][i])**2))
        distanceballer2.append(np.sqrt((screentabletrack[columnnamex][i] - screentabletrack['awayPlayer2_x'][i])**2 + (screentabletrack[columnnamey][i] - screentabletrack['awayPlayer2_y'][i])**2))
        distanceballer3.append(np.sqrt((screentabletrack[columnnamex][i] - screentabletrack['awayPlayer3_x'][i])**2 + (screentabletrack[columnnamey][i] - screentabletrack['awayPlayer3_y'][i])**2))
        distanceballer4.append(np.sqrt((screentabletrack[columnnamex][i] - screentabletrack['awayPlayer4_x'][i])**2 + (screentabletrack[columnnamey][i] - screentabletrack['awayPlayer4_y'][i])**2))
        distanceballer5.append(np.sqrt((screentabletrack[columnnamex][i] - screentabletrack['awayPlayer5_x'][i])**2 + (screentabletrack[columnnamey][i] - screentabletrack['awayPlayer5_y'][i])**2))
        
    else:

        columnnamex = screentabletrack['player_w_ball'][i] + "_x"
        columnnamey = screentabletrack['player_w_ball'][i] + "_y"
        distanceballer1.append(np.sqrt((screentabletrack[columnnamex][i] - screentabletrack['homePlayer1_x'][i])**2 + (screentabletrack[columnnamey][i] - screentabletrack['homePlayer1_y'][i])**2))
        distanceballer2.append(np.sqrt((screentabletrack[columnnamex][i] - screentabletrack['homePlayer2_x'][i])**2 + (screentabletrack[columnnamey][i] - screentabletrack['homePlayer2_y'][i])**2))
        distanceballer3.append(np.sqrt((screentabletrack[columnnamex][i] - screentabletrack['homePlayer3_x'][i])**2 + (screentabletrack[columnnamey][i] - screentabletrack['homePlayer3_y'][i])**2))
        distanceballer4.append(np.sqrt((screentabletrack[columnnamex][i] - screentabletrack['homePlayer4_x'][i])**2 + (screentabletrack[columnnamey][i] - screentabletrack['homePlayer4_y'][i])**2))
        distanceballer5.append(np.sqrt((screentabletrack[columnnamex][i] - screentabletrack['homePlayer5_x'][i])**2 + (screentabletrack[columnnamey][i] - screentabletrack['homePlayer5_y'][i])**2))

    i = i + 1

screentabletrack['Player1'] = distanceballer1
screentabletrack['Player2'] = distanceballer2
screentabletrack['Player3'] = distanceballer3
screentabletrack['Player4'] = distanceballer4
screentabletrack['Player5'] = distanceballer5

screentabletrack['pballcloser1'] = screentabletrack[['Player1','Player2','Player3','Player4','Player5']].idxmin(axis=1)
screentabletrack['pballcloser2'] = screentabletrack[['Player1','Player2','Player3','Player4','Player5']].apply(lambda row: row.nsmallest(2).idxmax(), axis=1)

screentabletrack.head()

i = 0
pballcloser1 = []
pballcloser2 = []

while i < len(screentabletrack):
    
    if screentabletrack['player_screen'][i][:4] == 'home':
        
        pballcloser1.append(screentabletrack['pballcloser1'][i].replace("P", "awayP"))
        pballcloser2.append(screentabletrack['pballcloser2'][i].replace("P", "awayP"))
        
    else:
        
        pballcloser1.append(screentabletrack['pballcloser1'][i].replace("P", "homeP"))
        pballcloser2.append(screentabletrack['pballcloser2'][i].replace("P", "homeP"))
        
    i = i + 1
    
screentabletrack['pballcloser1'] = pscreencloser1
screentabletrack['pballcloser2'] = pscreencloser2

columns_to_drop = ['Player1','Player2','Player3','Player4','Player5']
screentabletrack.drop(columns_to_drop, axis=1, inplace=True)

screentabletrack.head()

## Defining the LOCATION of screen's defender

locationlist = []
i = 0

while i < len(screentabletrack):

    screenx = screentabletrack['player_screen'][i] + "_x"
    screendefx = screentabletrack['pscreencloser2'][i] + "_x"
    
    if screentabletrack[screenx][i] > 0: 
    #if x positive to define the side of the court

        if (screentabletrack[screendefx][i] - screentabletrack[screenx][i]) >= 2.5:
            locationlist.append("Below screen")

        elif (screentabletrack[screendefx][i] - screentabletrack[screenx][i]) >= 0:
            locationlist.append("At screen")

        else:
            locationlist.append("Above screen")

    else:

        if (screentabletrack[screenx][i] - screentabletrack[screendefx][i]) >= 2.5:
            locationlist.append("Below screen")

        elif (screentabletrack[screenx][i] - screentabletrack[screendefx][i]) >= 0:
            locationlist.append("At screen")

        else:
            locationlist.append("Above screen")
            
    i = i + 1
    
    
#print(locationlist)

screentabletrack['Location_Screen_Def'] = locationlist

screentabletrack.head()

## Getting the next 5 seconds after screen

screentabletrack.head()

periodlist1 = screentabletrack['period'].tolist()
gameclocklist1 = screentabletrack['gameClock'].tolist()

k = 0
i = 0
j = 0

result_df1 = pd.DataFrame()

while k < len(screentabletrack):
    
    periodfilt1 = periodlist1[i]
    timefilter1 = gameclocklist1[k]
    
    df = trackeventspbp[(trackeventspbp['period'] == periodfilt1) & 
                (trackeventspbp['gameClock'] <= timefilter1) &
                (trackeventspbp['gameClock'] >= timefilter1-5)]
    df.loc[:, 'screenId'] = screentabletrack['screenId'][j]

    result_df1 = pd.concat([result_df1, df])
    
    i = i + 1
    k = k + 1
    j = j + 1
    
trackeventspbpfilt5 = result_df1

trackeventspbpfilt5.columns

screentabletrack.head()

screenplus5 = pd.merge(trackeventspbpfilt5, screentabletrack, on=['screenId'], how='left')

columns_to_drop = ['nbaId_y', 'period_y', 'gameClock_y', 'homePlayer1_x', 'homePlayer2_x', 'homePlayer3_x',
       'homePlayer4_x', 'homePlayer5_x', 'awayPlayer1_x', 'awayPlayer2_x',
       'awayPlayer3_x', 'awayPlayer4_x', 'awayPlayer5_x', 'homePlayer1_y',
       'homePlayer2_y', 'homePlayer3_y', 'homePlayer4_y', 'homePlayer5_y',
       'awayPlayer1_y', 'awayPlayer2_y', 'awayPlayer3_y', 'awayPlayer4_y',
       'awayPlayer5_y']
screenplus5.drop(columns_to_drop, axis=1, inplace=True)

screenplus5 = screenplus5.rename(columns={'home_x1': 'homePlayer1_x',
                                            'home_x2': 'homePlayer2_x',
                                            'home_x3': 'homePlayer3_x',
                                            'home_x4': 'homePlayer4_x',
                                            'home_x5': 'homePlayer5_x',
                                            'away_x1': 'awayPlayer1_x',
                                            'away_x2': 'awayPlayer2_x',
                                            'away_x3': 'awayPlayer3_x',
                                            'away_x4': 'awayPlayer4_x',
                                            'away_x5': 'awayPlayer5_x',
                                            'home_y1': 'homePlayer1_y',
                                            'home_y2': 'homePlayer2_y',
                                            'home_y3': 'homePlayer3_y',
                                            'home_y4': 'homePlayer4_y',
                                            'home_y5': 'homePlayer5_y',
                                            'away_y1': 'awayPlayer1_y',
                                            'away_y2': 'awayPlayer2_y',
                                            'away_y3': 'awayPlayer3_y',
                                            'away_y4': 'awayPlayer4_y',
                                            'away_y5': 'awayPlayer5_y',
                                            'period_x': 'period', 
                                            'gameClock_x': 'gameClock'
                                         })

screenplus5.head()

# Save if necessary
#screenplus5.to_csv(r"screenplus5.csv", index=False)

## Player with ball definition

# Import if necessary
#screenplus5 = pd.read_csv(r"screenplus5.csv")

# getting id for closest players

i = 0
listscreenid1 = []
listballid2 = []

while i < len(screenplus5):
    
    getscreenid1 = screenplus5['player_screen'][i]
    listscreenid1.append(screenplus5[getscreenid1][i])
    
    getballid2 = screenplus5['player_w_ball'][i]
    listballid2.append(screenplus5[getballid2][i])
    
    i = i + 1

screenplus5['player_screen_id'] = listscreenid1
screenplus5['player_w_ball_id'] = listballid2

screenplus5[['player_screen', 'player_w_ball','player_screen_id','player_w_ball_id']].head()

i = 0
listplayer = []

while i < len(screenplus5):
    
    if screenplus5['playerId'][i] == screenplus5['player_screen_id'][i]:
        listplayer.append('Screener')
    elif screenplus5['playerId'][i] == screenplus5['player_w_ball_id'][i]:
        listplayer.append('Baller')
    elif pd.isnull(screenplus5['playerId'][i]):
        listplayer.append(None)
    else:
        listplayer.append('Other player')
        
    i = i + 1
    
screenplus5['playerWithBall'] = listplayer

i = 0
teamPlay = []

while i < len(screenplus5):
    
    if screenplus5['player_screen'][i][:4] == 'home':
        teamPlay.append('home')
    else:
        teamPlay.append('away')
        
    i = i + 1
    
screenplus5['teamPlay'] = teamPlay

screenplus5.head()

## Inputing players name for analysis

gameteams.head()

screenplus5 = pd.merge(screenplus5, gameteams, left_on=['teamPlay'], right_on=['teamStatus'], how='left')

screenplus5.head()

columns_to_drop = ['teamId', 'teamStatus', 'gameId_y']
screenplus5.drop(columns_to_drop, axis=1, inplace=True)

screenplus5 = screenplus5.rename(columns={'gameId_x': 'gameId'})

screenplus5.head()

# getting id for closest players

i = 0
listid1 = []
listid2 = []

while i < len(screenplus5):
    
    getid1 = screenplus5['pscreencloser1'][i]
    listid1.append(screenplus5[getid1][i])
    
    getid2 = screenplus5['pscreencloser2'][i]
    listid2.append(screenplus5[getid2][i])
    
    i = i + 1

screenplus5['pscreencloser1id'] = listid1
screenplus5['pscreencloser2id'] = listid2

screenplus5.head()

screenplus5 = pd.merge(screenplus5, players, left_on=['pscreencloser1id'], right_on=['id'], how='left')

columns_to_drop = ['id', 'position', 'fullName']
screenplus5.drop(columns_to_drop, axis=1, inplace=True)

screenplus5 = screenplus5.rename(columns={'lastName': 'pscreencloser1name'})

screenplus5.head()

screenplus5 = pd.merge(screenplus5, players, left_on=['pscreencloser2id'], right_on=['id'], how='left')

columns_to_drop = ['id', 'position', 'fullName']
screenplus5.drop(columns_to_drop, axis=1, inplace=True)

screenplus5 = screenplus5.rename(columns={'lastName': 'pscreencloser2name'})

screenplus5 = pd.merge(screenplus5, players, left_on=['player_screen_id'], right_on=['id'], how='left')

columns_to_drop = ['id', 'position', 'fullName']
screenplus5.drop(columns_to_drop, axis=1, inplace=True)

screenplus5 = screenplus5.rename(columns={'lastName': 'player_screen_name'})

screenplus5 = pd.merge(screenplus5, players, left_on=['player_w_ball_id'], right_on=['id'], how='left')

columns_to_drop = ['id', 'position', 'fullName']
screenplus5.drop(columns_to_drop, axis=1, inplace=True)

screenplus5 = screenplus5.rename(columns={'lastName': 'player_w_ball_name'})

screenplus5['Screen_duo'] = screenplus5['player_screen_name'] + "/" + screenplus5['player_w_ball_name']

screenplus5['playerWithBall'].unique()

## Last event per play

lastevent = screenplus5[['nbaId_x', 'screenId', 'period', 'gameClock', 'eventType',
                         'playerId', 'SHOTRESULT', 'SHOTRESULT2', 'shotType', 'playerWithBall']].copy()

screenidlist = lastevent['screenId'].unique().tolist()

i = 0
lasteventlist2 = []
lasteventlist3 = []
lasteventlist4 = []

while i < len(screenidlist):
    
    screenid = screenidlist[i]
    lasteventlist = lastevent[(lastevent['eventType'].notnull()) & (lastevent['screenId']==screenid)  & (lastevent['playerWithBall']=='Baller')]['eventType'].tolist()
    lasteventballlist = lastevent[(lastevent['eventType'].notnull()) & (lastevent['screenId']==screenid)]['eventType'].tolist()
    
    if 'TO' in lasteventlist:
    
        if 'Baller'in lastevent[(lastevent['eventType'].notnull()) & 
                     (lastevent['screenId']==screenid) & 
                     (lastevent['eventType']=='TO')]['playerWithBall'].tolist():
            
            lasteventlist2.append((lastevent[(lastevent['eventType'].notnull()) & 
                                             (lastevent['screenId']==screenid) & 
                                             (lastevent['eventType']=='TO')]['gameClock']).values[0])
        
        
    elif 'Screener' in lastevent[(lastevent['eventType'].notnull()) & 
                     (lastevent['screenId']==screenid)]['playerWithBall'].tolist():
        
        if 'SHOT' in lastevent[(lastevent['eventType'].notnull()) & 
                               (lastevent['screenId']==screenid) &
                               (lastevent['playerWithBall']=='Screener')]['eventType'].tolist():
        
            lasteventlist2.append(lastevent[(lastevent['eventType'].notnull()) & 
                                                                (lastevent['screenId']==screenid) & 
                                                                (lastevent['playerWithBall']=='Screener') &
                                                                (lastevent['eventType']=='SHOT')].groupby('screenId')['gameClock'].min().reset_index()['gameClock'].values[0])
            
        else:
            
            lasteventlist2.append((lastevent[(lastevent['eventType'].notnull()) & 
                                                                 (lastevent['screenId']==screenid) & 
                                                                 (lastevent['playerWithBall']=='Screener')].groupby('screenId')['gameClock']).min().reset_index()['gameClock'].values[0])
                
    elif 'Baller' in lastevent[(lastevent['eventType'].notnull()) & 
                     (lastevent['screenId']==screenid)]['playerWithBall'].tolist():
        
        if 'SHOT' in lastevent[(lastevent['eventType'].notnull()) & 
                               (lastevent['screenId']==screenid) &
                               (lastevent['playerWithBall']=='Baller')]['eventType'].tolist():
        
            lasteventlist2.append(lastevent[(lastevent['eventType'].notnull()) & 
                                            (lastevent['screenId']==screenid) & 
                                            (lastevent['playerWithBall']=='Baller') &
                                            (lastevent['eventType']=='SHOT')].groupby('screenId')['gameClock'].min().reset_index()['gameClock'].values[0])
                
        else:
            
            lasteventlist2.append(lastevent[(lastevent['eventType'].notnull()) & 
                         (lastevent['screenId']==screenid) & 
                         (lastevent['playerWithBall']=='Baller')].groupby('screenId')['gameClock'].min().reset_index()['gameClock'].values[0])

    
    elif ('Baller' not in lastevent[(lastevent['eventType'].notnull()) & 
                     (lastevent['screenId']==screenid)]['playerWithBall'].tolist() and 
    'Screener' not in lastevent[(lastevent['eventType'].notnull()) & 
                     (lastevent['screenId']==screenid)]['playerWithBall'].tolist()):
    
        lasteventlist2.append(lastevent[(lastevent['eventType'].notnull()) & 
                     (lastevent['screenId']==screenid)].groupby('screenId')['gameClock'].min().reset_index()['gameClock'].values[0])
      
    else:
        
        lasteventlist2.append('error')
    
    i = i + 1

# filter all table using the time
k = 0
i = 0

result_df2 = pd.DataFrame()

while k < len(screentabletrack):
    
    screenfilt1 = screenidlist[i]
    timefilter1 = lasteventlist2[k]
    
    df = lastevent[(lastevent['screenId'] == screenfilt1) & 
                   (lastevent['gameClock'] == timefilter1) & 
                   (lastevent['eventType'].notnull())]
    
    result_df2 = pd.concat([result_df2, df])
    
    i = i + 1
    k = k + 1
    
lastevent = result_df2

lastevent.head()

lastevent2 = lastevent[~lastevent[['nbaId_x','screenId','period','gameClock']].duplicated(keep='first')]

lastevent2

## Merging event result with general table

screenplus5_1 = pd.merge(screenplus5, lastevent2, on=['screenId'], how='left')

screenplus5_1.columns

screenplus5_1.rename(columns={'gameClock_y': 'gameClock_LastEvent',
                              'eventType_y': 'eventType_LastEvent',
                              'SHOTRESULT_y': 'shotResult_LastEvent',
                              'SHOTRESULT2_y': 'shotResult2_LastEvent',
                              'shotType_y': 'shotType_LastEvent',
                              'playerWithBall_y': 'playerWithBall_LastEvent',
                              'nbaId_x_x': 'nbaId',
                              'period_x': 'period', 
                              'gameClock_x': 'gameClock', 
                              'shotClock_x': 'shotClock',
                              'eventType_x': 'eventType', 
                              'playerId_x': 'playerId', 
                              'SHOTRESULT_x': 'shotResult', 
                              'SHOTRESULT2_x': 'shotResult2',
                              'shotType_x': 'shotType'}, inplace=True)

columns_to_drop = ['nbaId_x_y','playerId_y']
screenplus5_1.drop(columns_to_drop, axis=1, inplace=True)

screenplus5_1.head()

screenplus5_1[screenplus5_1['eventType_LastEvent']=='SHOT'][['Screen_duo', 'period_y',
       'gameClock_LastEvent', 'eventType_LastEvent', 'shotResult_LastEvent',
       'shotResult2_LastEvent', 'shotType_LastEvent']]

# Creating a table to use in the dashboard

screenplus5_2 = screenplus5_1[(screenplus5_1['gameClock']==screenplus5_1['gameClock_LastEvent']) & 
               (screenplus5_1['period']==screenplus5_1['period_y']) &
               (screenplus5_1['eventType']==screenplus5_1['eventType_LastEvent'])].copy()

screenplus5_2.info()

# Saving final tables
screenplus5_1.to_csv(r"screenplus5_1_42100301.csv", index=False)
screenplus5_2.to_csv(r"screenplus5_2_42100301.csv", index=False)
