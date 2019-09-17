#!/usr/bin/env pyhon

import pandas as pd

data = pd.read_csv("wages_hours.csv", sep ="\t")
data1 = data[["AGE", "RATE"]]
# print(data[["AGE", "HRS"]].head(10))