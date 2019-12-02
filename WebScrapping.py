import urllib.request
from bs4 import BeautifulSoup

class WebScrapping:
    PAGE_NOT_FOUND = 'Page not found'
    ERROR_INVALID_USER_URL = 'Invalid StackOverflow User URL passed'
    MESSAGE_VALID_USER_URL = 'Valid StackOverflow User URL passed'

    def __init__(self, url):
        with urllib.request.urlopen(url) as url:
            html = url.read()
            self.soup = BeautifulSoup(html, 'lxml')
    
    def extract_user_card(self):
        self.user_card = self.soup.find(id='user-card')

    def validate_page(self, user):
        title = self.soup.title.string
        so_user_title = title.split('User ')[1].split(' - Stack Overflow')[0]
        if '-' in user:
            so_user_title = '-'.join(so_user_title.split(' '))
        if self.PAGE_NOT_FOUND in title or user.upper() != so_user_title.upper():
            raise Exception(self.ERROR_INVALID_USER_URL)
        else:
            print(self.MESSAGE_VALID_USER_URL + ' for ' + user)
            self.extract_user_card()

    def get_badges(self):
        gold = silver = bronze = 0
        # Extracting Gold Badges
        gold_sib = self.user_card.findAll('span', {'class': 'badge1'})
        if len(gold_sib) > 0:
            gold = int(gold_sib[0].findNext('span').text)
        # Extracting Silver Badges
        silver_sib = self.user_card.findAll('span', {'class': 'badge2'})
        if len(silver_sib) > 0:
            silver = int(silver_sib[0].findNext('span').text)
        # Extracting Bronze Badges
        bronze_sib = self.user_card.findAll('span', {'class': 'badge3'})
        if len(bronze_sib) > 0:
            bronze = int(bronze_sib[0].findNext('span').text)
        return {
            'gold': gold,
            'silver': silver,
            'bronze': bronze
        }
    
    def get_reputation(self):
        reputation = int(self.user_card.findAll('div', {'title' : 'reputation'})[0].findAll('div')[1].text.replace(',',''))
        return reputation