from .rule import get_rules
from .rule_set import get_rule_sets
from type.route import Route
from config.config import config_instance

from starlette.datastructures import URL

def get_route(base_url: URL) -> Route:
    return Route(
        rules=get_rules(base_url),
        rule_set=get_rule_sets(base_url),
        final=config_instance.route.final
    )
