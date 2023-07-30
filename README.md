# wisd_boston23
Hackathon Project Women in Sports Data 2023 - Team Boston23

- This project aims to analyze screens and their impact on the games evaluated.

- The analysis of screens and their outcomes can provide coaches and staff with information about other teams’ and their own screens behavior/results. This can be used to improve approaches and tactics.

Dataset used:
- Data provided by the Hackathon organization: AWS S3 bucket: sportradar-wisd-data.
- Imported data through NBA API.
- Data collected manually by watching the games (available here for download).

The project is divided in four parts:
1. Importing/cleaning AWS S3 dataset
  - You credentials to access this data
2. Importing NBA API dataset
  - Install nba_api
3. Downloading mapped screens 
  - Download .xlsx file from this repository (screens_mapping.xlsx)
4. Data manipulation/evaluation

You need to run the files in the same order (data_import_py folder):
1. aws_data_import.py
2. nba_api_import.py
3. data_screen_analysis

Next steps:
- Map other games' screens
- Track the coverage behaviour
