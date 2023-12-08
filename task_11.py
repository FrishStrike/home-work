import numpy as np
import pandas as pd

arr = np.arange(30)
arr.shape = 10, 3

df = pd.DataFrame(arr)

print(df[:3], "\n", df[-3:])

df.to_csv("data_frame.csv")