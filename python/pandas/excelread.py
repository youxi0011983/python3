#!/usr/bin/python3
import pandas as pd 

data = pd.read_excel('Sell Thru Copies 06212019.xlsx',sheet_name='Copy fr Sell Thru NoD16')

print(data)