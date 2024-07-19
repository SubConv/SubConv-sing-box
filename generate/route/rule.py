from config.config import config_instance
from type.route import Rule

from urllib.parse import urlparse
import re
from starlette.datastructures import URL

def get_rules(base_url: URL) -> list[Rule]:
    result = []

    result.extend([
        # add this server's domain to direct
        Rule(
            domain=[re.search(r"([^:]+)(:\d{1,5})?", base_url.hostname).group(1)],
            outbound="direct"
        ),
        # add dns route
        Rule(
            protocol=["dns"],
            outbound="dns-out"
        )
    ])

    for rule in config_instance.route.remote_rule_set:
        result.append(Rule(
            rule_set=[urlparse(rule[1]).path.split("/")[-1].split(".")[0]],
            outbound=rule[0]
        ))
    
    return result
