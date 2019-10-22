from pydfs_lineup_optimizer.settings import BaseSettings, LineupPosition
from pydfs_lineup_optimizer.constants import Sport, Site
from pydfs_lineup_optimizer.sites.sites_registry import SitesRegistry


class MoneyballSettings(BaseSettings):
    site = Site.MONEYBALL
    budget = 60000
    max_from_one_team = 9


@SitesRegistry.register_settings
class MoneyballAFLSettings(MoneyballSettings):
    sport = Sport.AFL
    positions = [
        LineupPosition('FWD', ('FWD', )),
        LineupPosition('FWD', ('FWD', )),
        LineupPosition('DEF', ('DEF', )),
        LineupPosition('DEF', ('DEF', )),
        LineupPosition('MID', ('MID', )),
        LineupPosition('MID', ('MID', )),
        LineupPosition('MID', ('MID', )),
        LineupPosition('RU', ('RU', )),
        LineupPosition('FLEX', ('FWD', 'DEF', 'MID', 'RU'))
    ]

@SitesRegistry.register_settings
class MoneyballNBASettings(MoneyballSettings):
    sport = Sport.BASKETBALL
    positions = [
        LineupPosition('PG', ('PG',)),
        LineupPosition('PG', ('PG',)),
        LineupPosition('SG', ('SG',)),
        LineupPosition('SG', ('SG',)),
        LineupPosition('SF', ('SF',)),
        LineupPosition('SF', ('SF',)),
        LineupPosition('PF', ('PF',)),
        LineupPosition('PF', ('PF',)),
        LineupPosition('C', ('C',)),
    ]
