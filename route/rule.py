from config import config_instance
from type.route import Rule

from urllib.parse import urlparse

def get_rules() -> list[Rule]:
    result = []

    for rule in config_instance.route.remote_rule_set:
        result.append(Rule(
            rule_set=urlparse(rule[1]).path.split("/")[-1].split(".")[0],
            outbound=rule[0]
        ))
    
    return result
