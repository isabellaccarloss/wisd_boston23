# wisd_boston23
Hackathon Project Women in Sports Data 2023 - Team Boston23

- This project aims to analyze screens and their impact on the games evaluated.

- The analysis of screens and their outcomes can provide coaches and staff with information about other teams’ and their own's screens behavior/results. This can be used to improve approaches and tactics.

- The final product is a Python code containing analysis and a dashboard.

- To access the data that are the input for the product, you need to run the importing/cleaning code.
  - Outputs: two csv files. 

   
Dataset used:
- Data provided by the Hackathon organization: AWS S3 bucket: sportradar-wisd-data.
- Imported data through NBA API.
- Data collected manually by watching the games (available here).

The project is divided in two codes:
1. Importing/cleaning/manipulating the data (importing_data.py).
2. Analysis and dashboard (analysis_report.py).


What do you need in each file:
1. importing_data.py
  - Credentials to access AWS S3 dataset
  - Install packages:
    - boto3
    - jsonlines
    - jsonlines pandas
    - nba_api
2. analysis_report.py
  - Install packages:
    - dash
    - matplotlib tk
  - two tables generated in the previous code:
    - screenplus5_1
    - screenplus5_2


Next steps:
- Map other games' screens
- Track the coverage behavior
