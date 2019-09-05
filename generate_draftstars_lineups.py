import pandas as pd
from itertools import chain
from pydfs_lineup_optimizer import get_optimizer, Site, Sport, CSVLineupExporter
from pydfs_lineup_optimizer.player import Player


class GenerateDraftstarsLineups:

    def __init__(self):
        self.optimizer = get_optimizer(Site.DRAFTSTARS, Sport.AFL)

    def process(self):
        data = self._import_data("AFLDFSUniverses.csv")
        lineup_list = list()
        for i in [100, 800, 1500, 2200, 2900, 3600, 4300, 5000, 5700, 6400, 7100, 7800, 8500, 9200, 9900]:
            print("Processing lineup " + str(i))
            optimizer = get_optimizer(Site.DRAFTSTARS, Sport.AFL)
            players = self._create_player_list(data, i)
            optimizer.load_players(players)
            lineup = optimizer.optimize(n=1)
            lineup_list.append(lineup)
        return lineup_list

    @staticmethod
    def _create_player_list(data, universe):
        data = data[["draftstarsID",
                     "playerName",
                     "draftstarsPosition",
                     "draftstarsPosition2",
                     "team",
                     "dsSalary",
                     str(universe)]]
        players = list()
        for index, row in data.iterrows():
            player = Player(
                row["draftstarsID"],
                row['playerName'].split(" ")[0],
                row['playerName'].split(" ")[1],
                [row['draftstarsPosition']] if str(row['draftstarsPosition2']) == "nan" else [row['draftstarsPosition'],
                                                                                              row['draftstarsPosition2']],
                row["team"],
                row["dsSalary"],
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
    exporter.export("universeLineups.csv")
    print("CSV exported")
