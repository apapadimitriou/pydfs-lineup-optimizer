import csv
from pydfs_lineup_optimizer.exceptions import LineupOptimizerIncorrectCSV
from pydfs_lineup_optimizer.lineup_importer import CSVImporter
from pydfs_lineup_optimizer.player import Player, GameInfo
from pydfs_lineup_optimizer.sites.sites_registry import SitesRegistry
from pydfs_lineup_optimizer.constants import Site


@SitesRegistry.register_csv_importer
class DraftstarsCSVImporter(CSVImporter):  # pragma: nocover
    site = Site.DRAFTSTARSNFLMULTI

    def import_players(self):
        players = []
        i = 0
        with open(self.filename, 'r') as csvfile:
            csv_data = csv.DictReader(csvfile, skipinitialspace=True)
            for row in csv_data:
                game_info = None
                try:
                    home_team = row["HomeTeam"]
                    away_team = row["AwayTeam"]
                    game_info = GameInfo(home_team, away_team, None, False)
                except ValueError:
                    pass
                try:
                    player = Player(
                        row['Player ID'],
                        row['Name'].split(" ")[0],
                        row['Name'].split(" ")[1],
                        [row['Position']] if not row['Position2'] else [row['Position'], row['Position2']],
                        row['Team'],
                        float(row['Price']),
                        float(row['Projection']),
                        max_exposure=float(row['Max Exposure']),
                        game_info=game_info
                    )
                except KeyError:
                    raise LineupOptimizerIncorrectCSV
                i = i + 1
                players.append(player)
        return players
