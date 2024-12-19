import pandas as pd

print("Script is running...")  # Add this at the beginning to confirm execution
file_path = 'Desktop/Lastsemester/data/final/Dataanalysis/retail1.csv'
data = pd.read_csv(file_path)
print(data.head())
print(data.info())
