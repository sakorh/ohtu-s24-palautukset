from player_reader import PlayerReader
from player_stats import PlayerStats
from rich import print
from rich.table import Table
from rich.console import Console

def main():

    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    console = Console()

    print("[italic white]NHL statistics by nationality[/italic white]\n")

    season = console.input("Select season [magenta][2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/][/magenta]: ")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
     
    players = reader.get_players()

    nationalities = set([player.nationality for player in players])

    while True:
        nationality = console.input(f"\nSelect nationality [bold cyan][{'/'.join(n for n in sorted(nationalities))}][/bold cyan]: ")

        if not nationality:
            break

        players = stats.top_scorers_by_nationality(nationality)

        table = Table(title=f"Top scorers of {nationality} season {season}")

        table.add_column("name", style="red1")
        table.add_column("team", style="magenta")
        table.add_column("goals", style="cyan", justify="right")
        table.add_column("assists", style="green", justify="right")
        table.add_column("points", style="gold1", justify="right")

        for player in players:
            table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.points))

        console.print(table)


if __name__ == "__main__":
    main()
