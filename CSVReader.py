import pandas as pd
from tabulate import tabulate
import numpy as np

df = pd.read_csv("SheetHackathon.csv")
df.fillna("None", inplace=True)
while True:
    user = input("Search: ").lower()
    adv = df[df['Name'].str.contains(user, na=False, case=False)]

    # tabulate -> str table
    print(tabulate(adv, showindex=False, headers=adv.columns, tablefmt="rounded_grid", stralign="center"))

    # Number of search results
    print("Count: %d" % adv.shape[0])
