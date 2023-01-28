import pandas as pd
from tabulate import tabulate

import numpy as np

df = pd.read_csv("SheetHackathon.csv")
df.fillna("None", inplace=True)
# print(df.to_string())
user = input("Search: ").lower()
adv = df[df['Name'].str.contains(user, na=False, case=False)]
# print(adv.to_string())

print(tabulate(adv, showindex=False, headers=adv.columns))

print("Count: %d"% adv.shape[0])