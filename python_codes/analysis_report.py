# Hackathon: Women in Sports Data 2023
# Authors: Isabella Couto Carlos and Eunice Brandares
# Date: 7/29/23

# Installing package

%pip install dash
%pip install matplotlib tk

# Importing libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

# Opening files

screenplus5_1 = pd.read_csv(r"screenplus5_1_42100301.csv")
screenplus5_2 = pd.read_csv(r"screenplus5_2_42100301.csv")

# Overall analysis

# Group the data by 'Name' and count the distinct 'ID's for each name
name_counts = screenplus5_1.groupby('name')['screenId'].nunique()

# Sort the name_counts Series in descending order
name_counts = name_counts.sort_values(ascending=False)

# Set the figure size (width, height) in inches
plt.figure(figsize=(6, 4))

# Create a bar chart
plt.bar(name_counts.index, name_counts.values, color=['#98002E','#007A33'])

# Add labels and title
plt.ylabel('# of screens')
plt.ylim(0, 65)
plt.title('# of screens per Team')

# Add labels for the count on top of each bar
for i, count in enumerate(name_counts.values):
    plt.text(i, count, str(count), ha='center', va='bottom')

# Display the plot
plt.tight_layout()
plt.show()

# Calculating delta for next print
team1 = 'Miami Heat'
team2 = 'Boston Celtics'
perc = (screenplus5_1[screenplus5_1['name']==team1].groupby('name')['screenId'].nunique().reset_index()['screenId'][0]/screenplus5_1[screenplus5_1['name']==team2].groupby('name')['screenId'].nunique().reset_index()['screenId'][0]-1)*100

if perc > 0:
    sign = "more"
else:
    sign = ""

print(f'During the game, {team1} made {perc:.1f}% {sign} screens than the {team2}.')

# Group the data by 'Name' and count the distinct 'ID's for each name
name_counts1 = screenplus5_1[screenplus5_1['name']=='Miami Heat'].groupby('player_screen_name')['screenId'].nunique()
name_counts2 = screenplus5_1[screenplus5_1['name']=='Boston Celtics'].groupby('player_screen_name')['screenId'].nunique()

# Sort the name_counts Series in descending order
name_counts1 = name_counts1.sort_values(ascending=False)
name_counts2 = name_counts2.sort_values(ascending=False)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))  # Create two subplots side by side

# Create a bar chart
axes[0].bar(name_counts1.index, name_counts1.values, color='#98002E')
axes[1].bar(name_counts2.index, name_counts2.values, color='#007A33')

# Add some text for labels, title, and custom x-axis tick labels, etc.
axes[0].set_ylabel('# of screens')
axes[0].set_title('# of screens per screener - Miami Heat')
axes[0].set_xticks(range(len(name_counts1)))
axes[0].set_xticklabels(name_counts1.index, rotation=90)
axes[0].set_ylim(0, 25)

# Add labels for the count on top of each bar
for i, count in enumerate(name_counts1.values):
    axes[0].text(i, count, str(count), ha='center', va='bottom')

axes[1].set_ylabel('# of screens')
axes[1].set_title('# of screens per screener - Boston Celtics')
axes[1].set_xticks(range(len(name_counts1)))
axes[1].set_xticklabels(name_counts2.index, rotation=90)
axes[1].set_ylim(0, 25)

# Add labels for the count on top of each bar
for i, count in enumerate(name_counts2.values):
    axes[1].text(i, count, str(count), ha='center', va='bottom')

plt.tight_layout()
plt.show()

# Group the data by 'Name' and count the distinct 'ID's for each name
name_counts1 = screenplus5_1[screenplus5_1['name']=='Miami Heat'].groupby('player_w_ball_name')['screenId'].nunique()
name_counts2 = screenplus5_1[screenplus5_1['name']=='Boston Celtics'].groupby('player_w_ball_name')['screenId'].nunique()

# Sort the name_counts Series in descending order
name_counts1 = name_counts1.sort_values(ascending=False)
name_counts2 = name_counts2.sort_values(ascending=False)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))  # Create two subplots side by side

# Create a bar chart
axes[0].bar(name_counts1.index, name_counts1.values, color='#98002E')
axes[1].bar(name_counts2.index, name_counts2.values, color='#007A33')

# Add some text for labels, title, and custom x-axis tick labels, etc.
axes[0].set_ylabel('# of screens')
axes[0].set_title('# of screens per baller - Miami Heat')
axes[0].set_xticks(range(len(name_counts1)))
axes[0].set_xticklabels(name_counts1.index, rotation=0)
axes[0].set_ylim(0, 25)

# Add labels for the count on top of each bar
for i, count in enumerate(name_counts1.values):
    axes[0].text(i, count, str(count), ha='center', va='bottom')

axes[1].set_ylabel('# of screens')
axes[1].set_title('# of screens per baller - Boston Celtics')
axes[1].set_xticks(range(len(name_counts2)))  
axes[1].set_xticklabels(name_counts2.index, rotation=0)
axes[1].set_ylim(0, 25)

# Add labels for the count on top of each bar
for i, count in enumerate(name_counts2.values):
    axes[1].text(i, count, str(count), ha='center', va='bottom')

plt.tight_layout()
plt.show()

# Group the data by 'Name' and count the distinct 'ID's for each name
name_counts = screenplus5_1[screenplus5_1['name']=='Miami Heat'].groupby('Screen_duo')['screenId'].nunique()

# Sort the name_counts Series in descending order
name_counts = name_counts.sort_values(ascending=False)

# Set the figure size (width, height) in inches
plt.figure(figsize=(10, 4))
plt.ylim(0, 14)

# Create a bar chart
plt.bar(name_counts.index, name_counts.values, color='#98002E')

# Add labels and title
plt.ylabel('# of screens')
plt.title('# of screens per duo - Miami Heat')

# Rotate the x-axis labels if needed
plt.xticks(rotation=90)
plt.xticks(fontsize=8)

# Add labels for the count on top of each bar
for i, count in enumerate(name_counts.values):
    plt.text(i, count, str(count), ha='center', va='bottom')

# Display the plot
plt.tight_layout()
plt.show()

# Group the data by 'Name' and count the distinct 'ID's for each name
name_counts = screenplus5_1[screenplus5_1['name']=='Boston Celtics'].groupby('Screen_duo')['screenId'].nunique()

# Sort the name_counts Series in descending order
name_counts = name_counts.sort_values(ascending=False)

# Set the figure size (width, height) in inches
plt.figure(figsize=(10, 4))
plt.ylim(0, 14)

# Create a bar chart
plt.bar(name_counts.index, name_counts.values, color='#007A33')

# Add labels and title
plt.ylabel('# of screens')
plt.title('# of screens per duo - Boston Celtics')

# Rotate the x-axis labels if needed
plt.xticks(rotation=90)
plt.xticks(fontsize=8)

# Add labels for the count on top of each bar
for i, count in enumerate(name_counts.values):
    plt.text(i, count, str(count), ha='center', va='bottom')

# Display the plot
plt.tight_layout()
plt.show()

# Group the data by 'Name' and count the distinct 'ID's for each name
name_counts = screenplus5_1.groupby('eventType_LastEvent')['screenId'].nunique()

# Sort the name_counts Series in descending order
name_counts = name_counts.sort_values(ascending=False)

# Set the figure size (width, height) in inches
plt.figure(figsize=(6, 4))

# Create a bar chart
plt.bar(name_counts.index, name_counts.values, color='#A9A9A9')

# Add labels and title
plt.ylabel('# of events')
plt.title('Events after screen', fontsize=10)
plt.ylim(0, 35)

# Add labels for the count on top of each bar
for i, count in enumerate(name_counts.values):
    plt.text(i, count, str(count), ha='center', va='bottom')

# Display the plot
plt.tight_layout()
plt.show()
print("*Considering events that happened until five seconds after or until a player\n"
"that was not part of the screen duo gets the ball.")

# Group the data by 'Name' and count the distinct 'ID's for each name
name_counts = screenplus5_1[screenplus5_1['eventType_LastEvent']=='SHOT'].groupby('playerWithBall_LastEvent')['screenId'].nunique()

# Sort the name_counts Series in descending order
name_counts = name_counts.sort_values(ascending=False)

# Set the figure size (width, height) in inches
plt.figure(figsize=(6, 4))

# Create a bar chart
plt.bar(name_counts.index, name_counts.values, color='#A9A9A9')

# Add labels and title
plt.ylabel('# of shots')
plt.title('# of shots in screen duo', fontsize=10)
plt.ylim(0, 30)

# Add labels for the count on top of each bar
for i, count in enumerate(name_counts.values):
    plt.text(i, count, str(count), ha='center', va='bottom')

# Display the plot
plt.tight_layout()
plt.show()

# Group the data by 'Name' and count the distinct 'ID's for each name
name_counts1 = screenplus5_1[(screenplus5_1['name']=='Miami Heat') & (screenplus5_1['eventType_LastEvent']=='SHOT')].groupby('playerWithBall_LastEvent')['screenId'].nunique()
name_counts2 = screenplus5_1[(screenplus5_1['name']=='Boston Celtics') & (screenplus5_1['eventType_LastEvent']=='SHOT')].groupby('playerWithBall_LastEvent')['screenId'].nunique()

# Sort the name_counts Series in descending order
name_counts1 = name_counts1.sort_values(ascending=False)
name_counts2 = name_counts2.sort_values(ascending=False)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))  # Create two subplots side by side

# Create a bar chart
axes[0].bar(name_counts1.index, name_counts1.values, color='#98002E')
axes[1].bar(name_counts2.index, name_counts2.values, color='#007A33')

# Add some text for labels, title, and custom x-axis tick labels, etc.
axes[0].set_ylabel('# of shots')
axes[0].set_title('# of shots in screen duo - Miami Heat')
axes[0].set_xticks(range(len(name_counts1)))
axes[0].set_xticklabels(name_counts1.index, rotation=0)
axes[0].set_ylim(0, 20)

# Add labels for the count on top of each bar
for i, count in enumerate(name_counts1.values):
    axes[0].text(i, count, str(count), ha='center', va='bottom')

axes[1].set_ylabel('# of shots')
axes[1].set_title('# of shots in screen duo - Boston Celtics')
axes[1].set_xticks(range(len(name_counts2)))  
axes[1].set_xticklabels(name_counts2.index, rotation=0)
axes[1].set_ylim(0, 20)

# Add labels for the count on top of each bar
for i, count in enumerate(name_counts2.values):
    axes[1].text(i, count, str(count), ha='center', va='bottom')

plt.tight_layout()
plt.show()

# Group the data by 'screenId' and count the distinct 'ID's for each name and shot result
name_counts = screenplus5_1[screenplus5_1['eventType_LastEvent'] == 'SHOT'] \
    .groupby(['shotResult_LastEvent', 'shotResult2_LastEvent'])['screenId'].nunique() \
    .unstack(fill_value=0)

# Sort the name_counts DataFrame based on the total number of shots for each name
name_counts['Total'] = name_counts.sum(axis=1)
name_counts = name_counts.sort_values(by='Total', ascending=False)

# Drop the 'Total' column for plotting
name_counts.drop('Total', axis=1, inplace=True)

# Set the figure size (width, height) in inches
plt.figure(figsize=(8, 6))

colors = {
    'BLOCKED': '#FE1111',
    'MADE': '#02A13E',
    'MISSED': '#7F0606',
    'FOUL': '#FFB514'
}

# Create a stacked bar chart
ax = name_counts.plot(kind='bar', stacked=True, color=[colors[col] for col in name_counts.columns])

# Add labels to the bars
for col in name_counts.columns:
    for index, value in enumerate(name_counts[col]):
        if value > 0:  # Only show labels for bars with count greater than 0
            bottom = 0
            for c in name_counts.columns:
                if c == col:
                    ax.text(index, bottom + value / 2, str(value), ha='center', va='center', color='white')
                    break
                bottom += name_counts[c][index]

# Add labels and title
plt.ylabel('# of shots')
plt.xlabel('')
plt.xticks(rotation=0)
plt.title('Shots results', fontsize=12)
plt.legend(title='')

# Display the plot
plt.tight_layout()
plt.show()

# Group the data by 'Name' and count the distinct 'ID's for each name
name_counts1 = screenplus5_1[(screenplus5_1['name']=='Miami Heat') & (screenplus5_1['eventType_LastEvent'] == 'SHOT')].groupby(['shotResult_LastEvent', 'shotResult2_LastEvent'])['screenId'].nunique().unstack(fill_value=0)
name_counts2 = screenplus5_1[(screenplus5_1['name']=='Boston Celtics') & (screenplus5_1['eventType_LastEvent'] == 'SHOT')].groupby(['shotResult_LastEvent', 'shotResult2_LastEvent'])['screenId'].nunique().unstack(fill_value=0)


# Sort the name_counts DataFrame based on the total number of shots for each name
name_counts1['Total'] = name_counts1.sum(axis=1)
name_counts1 = name_counts1.sort_values(by='Total', ascending=False)
name_counts1.drop('Total', axis=1, inplace=True)

name_counts2['Total'] = name_counts2.sum(axis=1)
name_counts2 = name_counts2.sort_values(by='Total', ascending=False)
name_counts2.drop('Total', axis=1, inplace=True)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))  # Create two subplots side by side

colors = {
    'BLOCKED': '#FE1111',
    'MADE': '#02A13E',
    'MISSED': '#7F0606',
    'FOUL': '#FFB514'
}

# Create a stacked bar chart for name_counts1
name_counts1.plot(kind='bar', stacked=True, color=[colors[col] for col in name_counts1.columns], ax=axes[0])

# Add labels to the bars
# Add labels to the bars
for col in name_counts1.columns:
    for index, value in enumerate(name_counts1[col]):
        if value > 0:  # Only show labels for bars with count greater than 0
            bottom = 0
            for c in name_counts1.columns:
                if c == col:
                    axes[0].text(index, bottom + value / 2, str(value), ha='center', va='center', color='white')
                    break
                bottom += name_counts1[c][index]

# Create a stacked bar chart for name_counts2
name_counts2.plot(kind='bar', stacked=True, color=[colors[col] for col in name_counts2.columns], ax=axes[1])

# Add labels to the bars
for col in name_counts2.columns:
    for index, value in enumerate(name_counts2[col]):
        if value > 0:  # Only show labels for bars with count greater than 0
            bottom = 0
            for c in name_counts2.columns:
                if c == col:
                    axes[1].text(index, bottom + value / 2, str(value), ha='center', va='center', color='white')
                    break
                bottom += name_counts2[c][index]

# Add labels and title to the first subplot
axes[0].set_ylabel('# of shots')
axes[0].set_xlabel('')
axes[0].set_xticks(range(len(name_counts1)))
axes[0].set_xticklabels(name_counts1.index, rotation=0)
axes[0].set_title('Shots results - Miami Heat', fontsize=12)
axes[0].legend(title='')
axes[0].set_ylim(0, 12)

# Add labels and title to the second subplot
axes[1].set_ylabel('# of shots')
axes[1].set_xlabel('')
axes[1].set_xticks(range(len(name_counts2)))
axes[1].set_xticklabels(name_counts2.index, rotation=0)
axes[1].set_title('Shots results - Boston Celtics', fontsize=12)
axes[1].legend(title='')
axes[1].set_ylim(0, 12)

# Display the plot
plt.tight_layout()
plt.show()

# Group the data by 'Name' and count the distinct 'ID's for each name
name_counts = screenplus5_1.groupby('Location_Screen_Def')['screenId'].nunique()

# Sort the name_counts Series in descending order
name_counts = name_counts.sort_values(ascending=False)

# Set the figure size (width, height) in inches
plt.figure(figsize=(6, 4))

# Create a bar chart
plt.bar(name_counts.index, name_counts.values, color='#A9A9A9')

# Add labels and title
plt.ylabel('# of screens')
plt.title('# of screens per Position of Screener defender', fontsize=10)
plt.ylim(0, 65)

# Add labels for the count on top of each bar
for i, count in enumerate(name_counts.values):
    plt.text(i, count, str(count), ha='center', va='bottom')

# Display the plot
plt.tight_layout()
plt.show()


# Static plot screen

screenplus5_1['screenId'].unique()

# Input here a screenId that you want to see in the plot

screenid = 421003010001

screenfilter = screenplus5_1.loc[screenplus5_1.groupby(['screenId'])['gameClock'].idxmax()]

screenfilterid = screenfilter[screenfilter['screenId']==screenid]

# Select the relevant columns for x and y values
x_columns = ['homePlayer1_x', 'homePlayer2_x',  'homePlayer3_x', 'homePlayer4_x', 'homePlayer5_x', 'awayPlayer1_x', 'awayPlayer2_x', 'awayPlayer3_x', 'awayPlayer4_x', 'awayPlayer5_x']
y_columns = ['homePlayer1_y','homePlayer2_y', 'homePlayer3_y',  'homePlayer4_y', 'homePlayer5_y', 'awayPlayer1_y', 'awayPlayer2_y', 'awayPlayer3_y', 'awayPlayer4_y', 'awayPlayer5_y']

# Define the colors for each set of data
line_colors = ['#98002E', '#98002E', '#98002E', '#98002E', '#98002E', '#007A33', '#007A33', '#007A33', '#007A33', '#007A33']

# Create the line plot
plt.figure(figsize=(10, 6))
plt.xlim(-50,50)
plt.ylim(-25,25)

# Sample image (Replace 'image_path.png' with the path to your actual image)
image_path = 'https://github.com/isabellaccarloss/wisd_boston23/raw/main/basketball_court.png'

# Load the image using Pillow
with urllib.request.urlopen(image_path) as url:
    img = Image.open(url)
    img_array = np.array(img)

plt.imshow(img_array, extent=[-50,50,-25,25], aspect='auto')

# Remove the values on both axes
plt.xticks([])
plt.yticks([])

for x_col, y_col, color in zip(x_columns, y_columns, line_colors):
    plt.plot(screenfilterid[x_col], screenfilterid[y_col], marker='o', linestyle='-', color=color)

plt.title('Screen plot')
plt.tight_layout()
plt.show()


# Animated plot screens

screenplus5_1['screenId'].unique()

# Input here a screenId that you want to see in the plot

screenid = 421003010001

%matplotlib tk

# Select the relevant columns for x and y values
x_columns = ['homePlayer1_x', 'homePlayer2_x',  'homePlayer3_x', 'homePlayer4_x', 'homePlayer5_x', 'awayPlayer1_x', 'awayPlayer2_x', 'awayPlayer3_x', 'awayPlayer4_x', 'awayPlayer5_x']
y_columns = ['homePlayer1_y','homePlayer2_y', 'homePlayer3_y',  'homePlayer4_y', 'homePlayer5_y', 'awayPlayer1_y', 'awayPlayer2_y', 'awayPlayer3_y', 'awayPlayer4_y', 'awayPlayer5_y']

# Define the colors for each set of data
line_colors = ['#98002E', '#98002E', '#98002E', '#98002E', '#98002E', '#007A33', '#007A33', '#007A33', '#007A33', '#007A33']

# Filter the DataFrame based on the desired time period
filtered_df = screenplus5_1[screenplus5_1['screenId'] == screenid]

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Set the x-axis and y-axis limits
ax.set_xlim(-50,50)
ax.set_ylim(-25,25)

# Initialize empty line objects for each line with assigned colors
lines = [ax.plot([], [], color=color, marker='.', markersize=8)[0] for color in line_colors]

# Load the image using Pillow
with urllib.request.urlopen(image_path) as url:
    img = Image.open(url)
    img_array = np.array(img)

plt.imshow(img_array, extent=[-50,50,-25,25], aspect='auto')

# Define the update function that will be called for each animation frame
def update(frame):
    # Get the current data based on the frame index
    current_data = filtered_df.iloc[frame]

    # Update the line data for each line
    for i, (x_col, y_col) in enumerate(zip(x_columns, y_columns)):
        x_values = current_data[x_col]
        y_values = current_data[y_col]
        lines[i].set_data(x_values, y_values)
        
    return lines

# Create the animation with a 100-millisecond delay between frames
animation = FuncAnimation(fig, update, frames=len(filtered_df), interval=50, blit=True)

# Add labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Line Chart Animation')

# Show the plot
plt.show()



# Dashboard

# Create a DataFrame from the data
df = pd.DataFrame(screenplus5_2)

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Basketball Stats Dashboard"),
    
    # Team filter (dropdown)
    dcc.Dropdown(
        id='team-dropdown',
        options=[{'label': team, 'value': team} for team in df['name'].unique()],
        value=df['name'].unique()[0],
        style={'width': '50%'}
    ),
    
    # player_w_ball_name filter (dropdown)
    dcc.Dropdown(
        id='player-dropdown',
        value=df['player_w_ball_name'].unique()[0],
        style={'width': '50%'}
    ),

    # Stats section
    html.H3("Shooting Percentage"),
    dcc.Graph(id='shooting-percentage-graph'),

    html.H3("Best player to block him:"),
    html.Div(id='best-blocker'),

    html.H3("Duo most effective to block him:"),
    html.Div(id='best-blocker-duo'),

    html.H3("Duo most effective to make him turn over:"),
    html.Div(id='best-turnover-duo')
])

# Callback to update the player_w_ball_name dropdown options based on the selected team
@app.callback(
    Output('player-dropdown', 'options'),
    Input('team-dropdown', 'value')
)
def update_player_dropdown(selected_team):
    # Filter the DataFrame to get the unique player names for the selected team
    filtered_players = df[df['name'] == selected_team]['player_w_ball_name'].unique()

    # Create the options list for the player dropdown
    player_dropdown_options = [{'label': player, 'value': player} for player in filtered_players]

    return player_dropdown_options


# Callbacks to update the various components based on the selected team and player_w_ball_name
@app.callback(
    Output('shooting-percentage-graph', 'figure'),
    Output('best-blocker', 'children'),
    Output('best-blocker-duo', 'children'),
    Output('best-turnover-duo', 'children'),
    Input('team-dropdown', 'value'),
    Input('player-dropdown', 'value')
)

def update_stats(selected_team, selected_player):
    # Filter data based on selected team and player
    filtered_df = df[(df['name'] == selected_team) & (df['player_w_ball_name'] == selected_player)]

    # Calculate 3Pt and 2Pt shooting percentage
    p3 = ['3PT Jump Shot','3PT Pullup Jump Shot']
    p2 = ['Driving Dunk','Pullup Jump Shot','Cutting Layup Shot','Driving Reverse Layup','Driving Layup','Driving Floating Jump Shot','Fadeaway Jumper','Alley Oop Layup']

    total_shots = len(filtered_df[(filtered_df['eventType_LastEvent'] == 'SHOT')])
    total_3p_shots = len(filtered_df[(filtered_df['eventType_LastEvent'] == 'SHOT') & (filtered_df['shotType_LastEvent'].isin(p3))])
    shots_3p = len(filtered_df[(filtered_df['eventType_LastEvent'] == 'SHOT') & (filtered_df['shotResult_LastEvent'].isin(['MADE', 'MISSED'])) & (filtered_df['shotType_LastEvent'].isin(p3))])
    made_3pt = len(filtered_df[(filtered_df['eventType_LastEvent'] == 'SHOT') & (filtered_df['shotResult_LastEvent'] == 'MADE') & (filtered_df['shotType_LastEvent'].isin(p3))])
    shooting_percentage_3pt = (made_3pt / total_3p_shots) * 100 if total_3p_shots > 0 else 0

    total_2p_shots = len(filtered_df[(filtered_df['eventType_LastEvent'] == 'SHOT') & (filtered_df['shotType_LastEvent'].isin(p2))])
    shots_2p = len(filtered_df[(filtered_df['eventType_LastEvent'] == 'SHOT') & (filtered_df['shotResult_LastEvent'].isin(['MADE', 'MISSED'])) & (filtered_df['shotType_LastEvent'].isin(p2))])
    made_2pt = len(filtered_df[(filtered_df['eventType_LastEvent'] == 'SHOT') & (filtered_df['shotResult_LastEvent'] == 'MADE') & (filtered_df['shotType_LastEvent'].isin(p2))])
    shooting_percentage_2pt = (made_2pt / total_2p_shots) * 100 if total_2p_shots > 0 else 0

    # Calculate the best player to block him
    block_count_by_pscreencloser1 = filtered_df[filtered_df['shotResult2_LastEvent'] == 'BLOCKED'].groupby('pscreencloser1name').size()
    if not block_count_by_pscreencloser1.empty:
        best_blocker = block_count_by_pscreencloser1.idxmax()
    else:
        best_blocker = "None" 
    
    # Calculate the duo most effective to block him
    block_count_by_pscreencloser = filtered_df[filtered_df['shotResult2_LastEvent'] == 'BLOCKED'].groupby(['pscreencloser1name', 'pscreencloser2name']).size()
    if not block_count_by_pscreencloser.empty:
        best_blockerduo1 = block_count_by_pscreencloser.idxmax()
        best_blocker_duo = '/'.join(best_blockerduo1)
    else:
        best_blocker_duo = "None"
        
    # Calculate the duo most effective to make him turn over
    turnover_pscreencloser = filtered_df[filtered_df['eventType_LastEvent'] == 'TO'].groupby(['pscreencloser1name', 'pscreencloser2name']).size()
    if not turnover_pscreencloser.empty:
        best_TOduo1 = turnover_pscreencloser.idxmax()
        best_turnover_duo = '/'.join(best_TOduo1)
    else:
        best_turnover_duo = "None" 

   # Prepare the figure for the shooting percentage plot
    fig = go.Figure()

    # Add 3P shots bar
    fig.add_trace(go.Bar(
        x=['3-Point'],
        y=[(made_3pt / total_3p_shots * 100) if total_3p_shots > 0 else 0],
        name='3-Point',
        text=[f'{shooting_percentage_3pt:.1f}% ({made_3pt}/{total_3p_shots})'],
        textposition='outside',
        marker=dict(color='#22B14C')
    ))

    # Add 2P shots bar
    fig.add_trace(go.Bar(
        x=['2-Point'],
        y=[(made_2pt / total_2p_shots * 100) if total_2p_shots > 0 else 0],
        name='2-Point',
        text=[f'{shooting_percentage_2pt:.1f}% ({made_2pt}/{total_2p_shots})'],
        textposition='outside',
        marker=dict(color='#15B0ED')
    ))

    # Update layout
    fig.update_layout(
        xaxis_title='Shot Type',
        yaxis_title='Shooting Percentage (%)',
        showlegend=False
    )
    
    # Update the title of the figure
    fig.update_layout(title=f'{selected_player} - Shooting Percentage')

    return fig, f'{best_blocker}', f'{best_blocker_duo}', f'{best_turnover_duo}'


if __name__ == '__main__':
    app.run_server(debug=True, port=805)
