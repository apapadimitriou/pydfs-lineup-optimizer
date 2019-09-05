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
