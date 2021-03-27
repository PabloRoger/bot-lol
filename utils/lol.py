import requests
import random
import os
from dotenv import load_dotenv

load_dotenv()
LOL_API_KEY = os.getenv('LOL_API_KEY')

class LolSettings:
    def __init__(self, summoner, region):
        self.summoner = summoner
        self.region = region
        self.headers = {'X-Riot-Token': '{LOL_API_KEY}'}

    def start(self):
        url = f'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{self.summoner}'
        response = requests.get(url, headers=self.headers)
        return response.json()

class Lol(LolSettings):
    def __init__(self, summoner, region):
        super().__init__(summoner, region)

    def greetings(self):
        summoner = self.start()
        if 'name' in summoner:
            name = summoner['name']
            lvl = summoner['summonerLevel']
            icon_id = summoner['profileIconId']

            greetings = f'Tu polla {name}, eres lvl {lvl}.'
            icon_url  = f'https://ddragon.leagueoflegends.com/cdn/11.6.1/img/profileicon/{icon_id}.png'
            return {'greetings': greetings, 'icon_url': icon_url}
        else:
            return {'greetings': 'No se pudo encontrar el nombre del invocador.', 'icon_url': ''}


    def rank(self):
        summoner = self.start()
        summoner_id = summoner['id']
        url = f'https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}'
        response = requests.get(url, headers=self.headers)
        print(response.json())
        return response.json()[0]

class LolInfo():
    def exotico(self):
        url = 'https://ddragon.leagueoflegends.com/cdn/13.22.1/data/en_US/champion.json'
        response = requests.get(url)
        champion_data = response.json()['data']
        random_champion = random.choice(list(champion_data.values()))
        return random_champion