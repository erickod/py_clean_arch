from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class HttpRequest:
    headers: Dict[str, Any] = field(default_factory=dict)
    body: Dict[str, Any] = field(default_factory=dict)
    params: Dict[str, Any] = field(default_factory=dict)
