Hackathon: Women in Sports Data 2023
<br>
<br>Author: Isabella Couto Carlos
<br>Date: 7/29/23
<br>

Reference: https://github.com/swar/nba_api/tree/master/src/nba_api/stats/endpoints

# Importing libraries

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

# Importing data

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
