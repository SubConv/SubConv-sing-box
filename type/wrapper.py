import typing
import json

from dataclasses import fields

_T = typing.TypeVar('_T')

class EnhancedJSONEncoder(json.JSONEncoder):
        def default(self, o):
            if hasattr(o, 'to_dict'):
                return o.to_dict()
            return json.JSONEncoder.default(self, o)
