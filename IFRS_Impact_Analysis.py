# ==============
# 1. Load the data
# ================
# import pandas library and give it the  alias "pd"
import pandas as pd
import matplotlib.pyplot as plt
# ==============
# 2. Rename the DataFrame
#=======================
# Read the csv file ("GBP_EUR.csv")and store it in a variable called "data" 
data = pd.read_csv("GBP_EUR.csv")
# Rename column and make changes 
data.rename(columns={
"DATE":"Date",
"TIME PERIOD":"Time_period",
"UK pound sterling/Euro (EXR.D.GBP.EUR.SP00.A)": "Exchange_rate"
}, inplace = True)
# Get me the new columns names
print(data.columns)
# Check missing values in each columns
# ============
# 3. Handle missing Data
# =============
print(data.isnull().sum())
# Drop columns that are empty
data.dropna(axis=1,how="all", inplace =True)
# Fill missing values in Exchange_rate column with previous value 
data["Exchange_rate"].fillna(method="ffill", inplace=True)
# Get me the information of the dataset
print(data.info())
# ============
# 4. Summary Statistics
# =============
#  Describe Exchange_rate column
data["Exchange_rate"].describe()
print(data["Exchange_rate"].describe())
# =======================
# visualization showing trends 
# ====================
# plotting a line chart with x and y to visualize the change in currency
data["Date"] = pd.to_datetime(data["Date"])
data = data.sort_values("Date")
plt.figure(figsize=(10,6))
plt.plot(data["Date"],data["Exchange_rate"])
plt.title("Uk pounds to Euro Exchange Rate Changes over time")
plt.xlabel("Date")
plt.ylabel("Exchange_rate")
plt.grid(True)
plt.show()






            

