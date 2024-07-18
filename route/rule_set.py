from config import config_instance
from type.route import Rule_set, Remote

from urllib.parse import urlparse

def get_rule_sets() -> list[Rule_set]:
    result = []

    for rule_set in config_instance.route.remote_rule_set:
        result.append(Remote(
            tag=urlparse(rule_set[1]).path.split("/")[-1].split(".")[0],
            format="binary",
            url=rule_set[1]
        ))

    return result