from dataclasses import asdict, dataclass
from typing import Any, Dict


@dataclass
class HealthCheckInput:
    http_server: str


@dataclass
class HealthCheckOutput:
    http_server: str
    status: str

    def asdict(self) -> Dict[str, Any]:
        return asdict(self)


class HealthCheckUseCase:
    def execute(self, input: HealthCheckInput) -> HealthCheckOutput:
        return HealthCheckOutput(input.http_server, "running")
