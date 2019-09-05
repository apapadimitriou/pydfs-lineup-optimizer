import csv
from pydfs_lineup_optimizer.exceptions import LineupOptimizerIncorrectCSV
from pydfs_lineup_optimizer.lineup_importer import CSVImporter
from pydfs_lineup_optimizer.player import Player
from pydfs_lineup_optimizer.sites.sites_registry import SitesRegistry
from pydfs_lineup_optimizer.constants import Site


@SitesRegistry.register_csv_importer
class MoneyballCSVImporter(CSVImporter):  # pragma: nocover
    site = Site.MONEYBALL

    def import_players(self):
        players = []
        i = 0
        with open(self.filename, 'r') as csvfile:
            csv_data = csv.DictReader(csvfile, skipinitialspace=True)
            for row in csv_data:
                try:
                    player = Player(
                        row['Player ID'],
                        row['Name'].split(" ")[0],
                        row['Name'].split(" ")[1],
                        [row['Position']] if not row['Position2'] else [row['Position'], row['Position2']],
                        row['Team'],
                        float(row['Price']),
                        float(row['Projection']),
                        max_exposure=float(row['Max Exposure'])
                    )
                except KeyError:
                    raise LineupOptimizerIncorrectCSV
                i = i + 1
                players.append(player)
        return players
