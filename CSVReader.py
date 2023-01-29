import pandas as pd
from tabulate import tabulate

count = 0
def csvread(values):
    global count
    df = pd.read_csv("ServiceSheet.csv")
    df.fillna("None", inplace=True)
    adv = df[df.apply(lambda row: row.astype(str).str.contains(values[0], case=False, na=False).any(), axis=1)]
    count = adv.shape[0]
    return tabulate(adv, showindex=False, headers=adv.columns, tablefmt="rounded_grid", stralign="center")

def numofresult():
    global count
    return count

