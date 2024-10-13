from r2x.models.core import BaseComponent


class PlexosGenerator(BaseComponent):
    name: str
    units: float
    max_capacity: float | None
    rating: float | None
    min_stable_level: float | None
    heat_rate: float | dict | None


class PlexosOperationalCost(BaseComponent):
    pass
