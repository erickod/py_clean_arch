from dataclasses import dataclass
from typing import Dict


@dataclass
class HealthCheckInput:
    http_server: str


@dataclass
class HealthCheckOutput:
    http_server: str
    status: str


class HealthCheckUseCase:
    def execute(self, input: HealthCheckInput) -> HealthCheckOutput:
        return HealthCheckOutput(input.http_server, "running")
