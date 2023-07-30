# Hackathon: Women in Sports Data 2023
# Author: Isabella Couto Carlos and Eunice Brandares
# Date: 7/29/23

# Importing libraries

import pandas as pd
import numpy as np

# Merging tracking and events playbyplay

## Cleaning tracking

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

## Cleaning events playbyplay

eventspbp = pd.read_csv(r"eventspbp1.csv")

eventspbp.columns

eventspbp1 = eventspbp[['gameId', 'nbaId', 'pbpId', 'period', 'shotClock', 'gameClock',
       'wallClock', 'eventType', 'playerId', 'HOMEDESCRIPTION',
       'NEUTRALDESCRIPTION', 'VISITORDESCRIPTION', 'SHOTRESULT', 'SHOTRESULT2', 'shotType', 'VISITORSCOREACUM', 'HOMESCOREACUM']].copy()

eventspbp1.head()

## Merging tracking and events playbyplay

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

# Naming the Teams

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

# Players

players = pd.read_csv(r"players.csv")

players.head()

players['fullName'] = players['firstName'] + " " + players['lastName']

players.head()

players = players[['id', 'position', 'lastName', 'fullName']].copy()

# Opening screen data

# Here you need to import the .xlsx file that is avaiable for download in Github

screens = pd.read_excel(r"screens_mapping.xlsx")

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

# Merging screen data and trackeventspbp

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

# Rebuilding screen table to get the exact screen moment

## Creating position table

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

## Getting the row with the closest the Baller and Screener

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

# Defining the LOCATION of screen's defender

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

# Getting the next 5 seconds after screen

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

# Player with ball definition

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

# Inputing players name for analysis

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

# Last event per play

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

# Merging event result with general table

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

# Save if necessary
#screenplus5_1.to_csv(r"screenplus5_42100301.csv", index=False)

# Analysis

# Open if necessary
screenplus5_1 = pd.read_csv(r"screenplus5_42100301.csv")

