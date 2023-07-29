# wisd_boston23
Hackathon Project Women in Sports Data 2023 - Team Boston23

- This project aims to analyze screens and their impact on the games evaluated.

- The analysis of screens and their outcomes can provide coaches and staff with information about other teams’ and their own screens behavior/results. This can be used to improve approaches and tactics.

Dataset used:
- Data provided by the Hackathon organization: AWS S3 bucket: sportradar-wisd-data.
- Imported data through NBA API.
- Data collected manually by watching the games (available here for download).

The project is divided in four parts:
1. Importing AWS S3 dataset
  - You credentials to access this data
2. Importing NBA API dataset
  - Install nba_api
3. Importing mapped screens 
  - Import .xlsx file from this repository (screens_mapping.xlsx)
4. Data cleaning/manipulation/evaluation

You need to run the files in the same order:
1. AWS_data_import.py (data_import folder)
2. 

Next steps:
- Map other games' screens
- Track the coverage behaviour
