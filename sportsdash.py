import sports
import requests
import statsapi
import nba_api

class curGames:
    
    def show_games(self):
        matches = sports.all_matches()
        match_info = (matches['baseball'] + matches['basketball'])
        return str(match_info)



class myTeams:

    def Kings(self):
        from nba_api.stats.static import teams
        kings = teams.find_team_by_abbreviation('sac')
        kingsid = kings['id']

    def Athletics(self):

        self.athletics = statsapi.lookup_team('oak')['id']
        self.athleticsid = athletics[0]['id']

games = curGames()
x = games.show_games()
for i in x.split(','):
    print(i)