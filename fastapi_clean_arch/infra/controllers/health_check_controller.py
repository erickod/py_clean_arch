from typing import Any, Dict

from fastapi_clean_arch.application.health_check import (
    HealthCheckInput,
    HealthCheckOutput,
    HealthCheckUseCase,
)
from fastapi_clean_arch.application.protocols.controller_protocol import HttpServer


class HealthCheckController:
    http_server: HttpServer

    def __init__(
        self, http_server: HttpServer, health_check: HealthCheckUseCase
    ) -> None:
        self.http_server = http_server
        self.health_check = health_check
        self.http_server.on(method="GET", url="/health_check", controller=self)

    def handle(
        self, body: Dict[Any, Any] = {}, params: Dict[Any, Any] = {}
    ) -> HealthCheckOutput:
        input = HealthCheckInput(http_server=self.http_server.__class__.__name__)
        return self.health_check.execute(input=input)
