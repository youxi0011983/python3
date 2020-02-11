#!/usr/bin/python3
import pandas as pd 

url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'

match = "Metcalf Bank"
dfs = pd.read_html(url,match=match)

print (dfs)