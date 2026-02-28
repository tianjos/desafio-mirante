import json
from dataclasses import asdict, is_dataclass
from decimal import Decimal
from datetime import datetime


class DomainEncoder(json.JSONEncoder):
    def default(self, obj):
        if is_dataclass(obj):
            return asdict(obj)

        if isinstance(obj, Decimal):
            return str(obj)

        if isinstance(obj, datetime):
            return obj.isoformat()

        return super().default(obj)
