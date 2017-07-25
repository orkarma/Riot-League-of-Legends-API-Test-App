
import json
from RiotAPI import RiotAPI

def main():
    api = RiotAPI('RGAPI-5069ebae-c8e9-44f6-9ff9-d5b3f22a99d2')
    r = api.get_summoner_by_name('orkarma')
    print (r.format)

if __name__ == "__main__":
    main()