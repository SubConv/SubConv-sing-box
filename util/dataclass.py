from dataclasses import is_dataclass
from dataclass_wizard import fromdict
import json

def to_dict(data) -> dict:
    result = {}
    for key, value in data.__dict__.items():
        if value is None:
            continue
        if is_dataclass(value):
            result[key] = to_dict(value)
        elif isinstance(value, list) or isinstance(value, tuple):
            result[key] = []
            for item in value:
                if is_dataclass(item):
                    result[key].append(to_dict(item))
                else:
                    result[key].append(item)
        elif isinstance(value, dict):
            result[key] = {}
            for k, v in value.items():
                if is_dataclass(v):
                    result[key][k] = to_dict(v)
                else:
                    result[key][k] = v
        else:
            result[key] = value
    return result


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        # check if dataclass
        if is_dataclass(o):
            return to_dict(o)
        return super().default(o)

def to_json(d: dict):
    return json.dumps(d, cls=EnhancedJSONEncoder, indent=4)

def from_dict(*args, **kwargs):
    return fromdict(*args, **kwargs)
