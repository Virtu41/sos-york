import pandas as pd
from tabulate import tabulate

import numpy as np
count = 0
def csvread(values):
    global count
    df = pd.read_csv("SheetHackathon.csv")
    df.fillna("None", inplace=True)
    # print(df.to_string())
    
    # adv = df[df['Name'].str.contains(values[3], na=False, case=False)]
    # Rows that matches the user's input
    adv = df[df.apply(lambda row: row.astype(str).str.contains(values[3], case=False, na=False).any(), axis=1)]
    
    # print(adv.to_string())

    print(tabulate(adv, showindex=False, headers=adv.columns, tablefmt="rounded_grid", stralign="center"))
    count = adv.shape[0]
    return tabulate(adv, showindex=False, headers=adv.columns, tablefmt="rounded_grid", stralign="center")

def numofresult():
    global count
    return count

