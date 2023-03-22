from py_clean_arch.application.health_check import HealthCheckInput, HealthCheckUseCase
from py_clean_arch.application.protocols.controller_protocol import HttpServer
from py_clean_arch.infra.http.helpers import HttpRequest, HttpResponse


class HealthCheckController:
    http_server: HttpServer

    def __init__(
        self, http_server: HttpServer, health_check: HealthCheckUseCase
    ) -> None:
        self.http_server = http_server
        self.uc = health_check
        self.http_server.on(method="GET", url="/health_check", controller=self)

    def handle(self, request: HttpRequest) -> HttpResponse:
        input = HealthCheckInput(http_server=self.http_server.__class__.__name__)
        output = self.uc.execute(input=input)
        response = HttpResponse(body=output.asdict())
        return response
