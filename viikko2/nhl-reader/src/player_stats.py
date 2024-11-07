

class PlayerStats:
    def __init__(self, player_reader):
        reader = player_reader
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):

        players = list(filter(lambda player: player.nationality == nationality, self._players))
        
        return sorted(players, key=lambda player: player.points, reverse=True)


    
