from pydfs_lineup_optimizer.settings import BaseSettings, LineupPosition
from pydfs_lineup_optimizer.constants import Sport, Site
from pydfs_lineup_optimizer.sites.sites_registry import SitesRegistry


class DraftstarsSettings(BaseSettings):
    site = Site.DRAFTSTARS
    budget = 100000
    max_from_one_team = 8


@SitesRegistry.register_settings
class DraftstarsAFLSettings(DraftstarsSettings):
    sport = Sport.AFL
    positions = [
        LineupPosition('FWD', ('FWD', )),
        LineupPosition('FWD', ('FWD', )),
        LineupPosition('DEF', ('DEF', )),
        LineupPosition('DEF', ('DEF', )),
        LineupPosition('MID', ('MID', )),
        LineupPosition('MID', ('MID', )),
        LineupPosition('MID', ('MID', )),
        LineupPosition('MID', ('MID', )),
        LineupPosition('RK', ('RK', )),
    ]


@SitesRegistry.register_settings
class DraftstarsGolfSettings(DraftstarsSettings):
    sport = Sport.GOLF
    positions = [
        LineupPosition('G', ('G', )),
        LineupPosition('G', ('G', )),
        LineupPosition('G', ('G', )),
        LineupPosition('G', ('G', )),
        LineupPosition('G', ('G', )),
        LineupPosition('G', ('G', ))
    ]

