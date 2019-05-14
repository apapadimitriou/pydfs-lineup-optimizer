import csv
from pydfs_lineup_optimizer.exceptions import LineupOptimizerIncorrectCSV
from pydfs_lineup_optimizer.lineup_importer import CSVImporter
from pydfs_lineup_optimizer.player import Player
from pydfs_lineup_optimizer.sites.sites_registry import SitesRegistry
from pydfs_lineup_optimizer.constants import Site


@SitesRegistry.register_csv_importer
class DraftstarsCSVImporter(CSVImporter):  # pragma: nocover
    site = Site.DRAFTSTARS

    def import_players(self):
        players = []
        with open(self.filename, 'r') as csvfile:
            csv_data = csv.DictReader(csvfile, skipinitialspace=True)
            for row in csv_data:
                try:
                    player = Player(
                        row['id'],
                        row['first name'],
                        row['last name'],
                        row['position'].split(','),
                        row['team'],
                        float(row['salary']),
                        float(row['0'])
                    )
                except KeyError:
                    raise LineupOptimizerIncorrectCSV
                players.append(player)
        return players
