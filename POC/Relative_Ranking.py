import pandas as pd
users = pd.read_csv('https://data.stackexchange.com/stackoverflow/csv/9320?Location=Melbourne')
reputation = 1973
reputations = users['Reputation']
total_reputations = len(reputations)
higher_reputations = (reputations > 1973).sum()
print(higher_reputations / total_reputations)