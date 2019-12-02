import pandas as pd
data = pd.read_csv('https://data.stackexchange.com/stackoverflow/csv/9320?Location=Melbourne')
data.to_csv("Test.csv", sep='\t', encoding='utf-8')