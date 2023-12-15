import numpy as np
import pandas as pd

customers = pd.read_csv("Customers.csv", delimiter=";")

print(customers[(customers["Age"]>30) & (customers["Income"]<30000)])

print()

print(customers[(customers["Profession"]=="Lawyer") & (customers["Work Experience"]>5)])