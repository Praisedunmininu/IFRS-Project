UK Pound to Euro Exchange Rate Analysis

   What This Project Does
This project looks at how the UK Pound (GBP) changes compared to the Euro (EUR) over time. It cleans the data, summarizes it, and shows a trend using a line chart.

Dataset
File used: GBP_EUR.csv

Columns:
Date – when the exchange rate was recorded
Time_period – the time period of the observation
Exchange_rate – value of 1 GBP in Euros

Steps in the Project

Load and check the data using Python : data = pd.read_csv("GBP_EUR.csv)
Fill missing values so the data is complete
Get basic statistics about the exchange rate
Plot a line chart to show trends over time

How to Run
Install required libraries:
pip install pandas matplotlib
Put GBP_EUR.csv in the same folder as your Python script

Run the script:
python IFRS_Impact_Analysis.py
View the line chart of GBP to EUR changes

Output
A simple line chart
X-axis: Date
Y-axis: Exchange rate
shows how the Uk pound changes against the Euro over time. 

Shows how the UK Pound changes against the Euro over time
