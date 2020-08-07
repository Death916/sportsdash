import sports
import requests

class curgames:
    
    def show_games():
        matches = sports.all_matches()
        match_info = (matches['baseball'] + matches['basketball'])
        print(str(match_info))

curgames.show_games()





