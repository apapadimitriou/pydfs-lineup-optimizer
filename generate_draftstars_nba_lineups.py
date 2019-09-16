import pandas as pd
from itertools import chain
from pydfs_lineup_optimizer import get_optimizer, Site, Sport, CSVLineupExporter
from pydfs_lineup_optimizer.player import Player


class GenerateDraftstarsLineups:

    def __init__(self):
        self.optimizer = get_optimizer(Site.DRAFTSTARS, Sport.BASKETBALL)

    def process(self):
        data = self._import_data("UNIVERSES.csv")
        lineup_list = list()
        for i in range(201):
            print("Processing lineup " + str(i))
            optimizer = get_optimizer(Site.DRAFTSTARS, Sport.BASKETBALL)
            players = self._create_player_list(data, i)
            optimizer.load_players(players)
            lineup = optimizer.optimize(n=1)
            lineup_list.append(lineup)
        return lineup_list

    @staticmethod
    def _create_player_list(data, universe):
        data = data[["Player ID",
                     "Name",
                     "Position",
                     "Position2",
                     "Team",
                     "Price",
                     str(universe)]]
        players = list()
        for index, row in data.iterrows():
            player = Player(
                row["Player ID"],
                row['Name'].split(" ")[0],
                row['Name'].split(" ")[1] if len(row["Name"].split(" ")) > 1 else "",
                [row['Position']] if str(row['Position2']) == "nan" else [row['Position'], row['Position2']],
                row["Team"],
                row["Price"],
                row[str(universe)]
            )
            players.append(player)
        return players

    @staticmethod
    def _import_data(filename):
        data = pd.read_csv(filename)
        return data


if __name__ == "__main__":
    generator = GenerateDraftstarsLineups()
    lineups = generator.process()
    lineup_generator = chain.from_iterable(lineups)
    exporter = CSVLineupExporter(lineup_generator)
    exporter.export("universeNBALineups.csv")
    print("CSV Exported")
