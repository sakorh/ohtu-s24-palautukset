import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_returns_correct_player(self):
        player = self.stats.search("Semenko")
        self.assertEqual(player.name, "Semenko")

    def test_search_returns_none_if_player_not_found(self):
        
        self.assertEqual(self.stats.search("McDavid"), None)
        
    def test_team_returns_correct_players(self):
        players_of_team = self.stats.team("EDM")

        self.assertEqual([player.name for player in players_of_team], ["Semenko", "Kurri", "Gretzky"])

    def test_top_returns_correct_order(self):
        top_3 = [player.name for player in self.stats.top(3)]

        self.assertEqual(top_3, ["Gretzky", "Lemieux", "Yzerman", "Kurri"])

    def test_top_goal_scorers_returns_correct_players(self):
        top_3_scorers = [player.name for player in self.stats.top(3, SortBy.GOALS)]

        self.assertEqual(top_3_scorers, ["Lemieux", "Yzerman", "Kurri", "Gretzky"])

    def test_top_by_assists_returns_correct_players(self):
        top_3_assists = [player.name for player in self.stats.top(3, SortBy.ASSISTS)]

        self.assertEqual(top_3_assists, ["Gretzky", "Yzerman", "Lemieux", "Kurri"])