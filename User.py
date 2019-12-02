import pandas as pd
import sys
sys.path.append('./UsersByRegion')
from UsersByRegion import UsersByRegion
sys.path.append('./WebScrapping')
from WebScrapping import WebScrapping

class User:
    reputation = 0
    badges = {
        'gold': 0,
        'silver': 0,
        'bronze': 0
    }
    relative_ranking = {}

    def __init__(self, url):
        self.so_url = url
        self.user_name = url.split('/')[-1]
    
    def calculate_relative_ranking(self, reputations, user_reputation):
        total_reputations = len(reputations)
        higher_reputations = (reputations > user_reputation).sum()
        return round((higher_reputations / total_reputations) * 100, 4)

    def build_profile_info(self, regions):
        scrape = WebScrapping(self.so_url)
        users_by_region = {}
        try:
            scrape.validate_page(self.user_name)
            self.badges = scrape.get_badges()
            self.reputation = scrape.get_reputation()
            for region in regions:
                users_by_region = UsersByRegion(region)
                reputations = users_by_region.get_users()['Reputation']
                self.relative_ranking[region] = self.calculate_relative_ranking(reputations, self.reputation)
        except Exception as e:
            print(str(e))
            raise Exception(str(e))
        
        