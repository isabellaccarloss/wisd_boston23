# Hackathon: Women in Sports Data 2023
# Author: Isabella Couto Carlos
# Date: 7/29/23

# Importing libraries

%pip install boto3
%pip install jsonlines
%pip install jsonlines pandas

import boto3
import jsonlines
import pandas as pd
import json

# Accessing AWS 3

# Replace with your credentials
session = boto3.Session(
    aws_access_key_id='AKIA6KMLMMGZJ6CNEF5X',
    aws_secret_access_key='PnWB9kCglrwRFn2zmv0kMq7nhduN2vIYhyORnkG0'
)

s3_client = session.client('s3')

response = s3_client.list_objects(Bucket='sportradar-wisd-data')
for obj in response['Contents']:
    print(obj['Key'])

# Importing data

## Events

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

## Tracking

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
tracking.to_csv(r"tracking.csv", index=False)

## Games

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
#games2.to_csv(r"games2.csv", index=False)

## Players

keyname = "metadata/players.json"
players = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

players[0]['players']

players = pd.DataFrame(players[0]['players'])

players.head()

# Saving players table (optional)
#players.to_csv(r"players.csv", index=False)

## Teams

keyname = "metadata/teams.json"
teams = [json.loads(line) for line in s3_client.get_object(Bucket='sportradar-wisd-data', Key=keyname)['Body'].read().decode('utf-8').strip().split('\n')]

teams[0]['teams']

teams = pd.DataFrame(teams[0]['teams'])

teams.head()

# Saving teams table (optional)
#teams.to_csv(r"teams.csv", index=False)

# Cleaning tables

## Tracking

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
