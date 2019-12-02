import pandas as pd

class UsersByRegion:

    def __init__(self, region):
        self.url = 'https://data.stackexchange.com/stackoverflow/csv/9320?Location=' + region
        self.region = region
    
    def get_users(self):
        return pd.read_csv(self.url)