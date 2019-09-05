from pydfs_lineup_optimizer.settings import BaseSettings, LineupPosition
from pydfs_lineup_optimizer.constants import Sport, Site
from pydfs_lineup_optimizer.sites.sites_registry import SitesRegistry


class DraftstarsNFLSettings(BaseSettings):
    site = Site.DRAFTSTARSNFL
    budget = 80000
    max_from_one_team = 5


@SitesRegistry.register_settings
class DraftstarsNFLSettings(DraftstarsNFLSettings):
    sport = Sport.FOOTBALL
    positions = [
        LineupPosition('FLEX', ('FLEX', )),
        LineupPosition('FLEX', ('FLEX', )),
        LineupPosition('FLEX', ('FLEX', )),
        LineupPosition('FLEX', ('FLEX', )),
        LineupPosition('FLEX', ('FLEX', )),
        LineupPosition('FLEX', ('FLEX', ))
    ]
