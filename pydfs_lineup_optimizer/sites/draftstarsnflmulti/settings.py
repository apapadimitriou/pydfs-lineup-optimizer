from pydfs_lineup_optimizer.settings import BaseSettings, LineupPosition
from pydfs_lineup_optimizer.constants import Sport, Site
from pydfs_lineup_optimizer.sites.sites_registry import SitesRegistry


class DraftstarsNFLMultiSettings(BaseSettings):
    site = Site.DRAFTSTARSNFL
    budget = 100000
    max_from_one_team = 4


@SitesRegistry.register_settings
class DraftstarsNFLMultiSettings(DraftstarsNFLMultiSettings):
    sport = Sport.FOOTBALL
    positions = [
        LineupPosition('QB', ('QB', )),
        LineupPosition('RB', ('RB', )),
        LineupPosition('RB', ('RB', )),
        LineupPosition('WR', ('WR', )),
        LineupPosition('TE', ('TE', )),
        LineupPosition('FLEX', ('FLEX', )),
        LineupPosition('FLEX', ('FLEX',)),
        LineupPosition('DST', ('DST',))
    ]
