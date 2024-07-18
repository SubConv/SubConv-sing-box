from .rule import get_rules
from .rule_set import get_rule_sets
from type.route import Route
from config import config_instance

def get_route() -> Route:
    return Route(
        rules=get_rules(),
        rule_set=get_rule_sets(),
        final=config_instance.route.final
    )
