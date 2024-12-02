class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def get_score(self):
        scores_dict = {0:"Love", 1:"Fifteen", 2:"Thirty", 3:"Forty"}
        return scores_dict[self.score]

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1.score = self.player1.score + 1
        else:
            self.player2.score = self.player2.score + 1

    def check_for_deuce(self):
        if self.player1.score < 3:
            return self.player1.get_score() + "-All"
        return "Deuce"

    def get_game_state(self):
        difference = self.player1.score - self.player2.score
        if difference == 1:
            score = "Advantage player1"
        elif difference == -1:
            score = "Advantage player2"
        elif difference >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score

    def get_score(self):
        if self.player1.score == self.player2.score:
            return self.check_for_deuce()

        elif self.player1.score >= 4 or self.player2.score >= 4:
            return self.get_game_state()
        
        return self.player1.get_score() + "-" + self.player2.get_score()

