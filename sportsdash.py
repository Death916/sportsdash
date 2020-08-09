import sports
import requests
import statsapi
import nba_api

class curgames:
    
    def show_games():
        matches = sports.all_matches()
        match_info = (matches['baseball'] + matches['basketball'])
        print(str(match_info))

curgames.show_games()

class myTeams:

    def Kings():
        from nba_api.stats.static import teams
        kings = teams.find_team_by_abbreviation('sac')
        kingsid = kings['id']


