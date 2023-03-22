from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class HttpResponse:
    headers: Dict[str, Any] = field(default_factory=dict)
    body: Dict[str, Any] = field(default_factory=dict)
    status_code: int = 200
