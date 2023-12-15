import pandas as pd

customers = pd.read_csv("Customers.csv", delimiter=";")

if customers.isna:
    customers.dropna(inplace=True)

print(customers.groupby("Profession")["Income"].mean())