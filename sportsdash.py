import sports
import requests
import statsapi
import nba_api

class curGames:
    
    def show_games(self):
        matches = sports.all_matches()
        match_info = (matches['baseball'] + matches['basketball'])
        print(str(match_info))
        return



class myTeams:

    def Kings(self):
        from nba_api.stats.static import teams
        kings = teams.find_team_by_abbreviation('sac')
        kingsid = kings['id']

    def Athletics(self):

        self.athletics = statsapi.lookup_team('oak')['id']
        self.athleticsid = athletics[0]['id']

games = curGames()
games.show_games()