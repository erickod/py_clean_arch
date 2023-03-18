from typing import Any, Dict

from fastapi_clean_arch.application.protocols.controller_protocol import HttpServer


class HealthCheckUseCase:
    def execute(self) -> str:
        return "running"


class HealthCheckController:
    http_server: HttpServer

    def __init__(
        self, http_server: HttpServer, health_check: HealthCheckUseCase
    ) -> None:
        self.http_server = http_server
        self.health_check = health_check
        self.http_server.on(method="get", url="/health_check", controller=self.handle)

    def handle(self, body: Dict[Any, Any] = {}, params: Dict[Any, Any] = {}) -> Any:
        return self.health_check.execute()
