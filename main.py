from fastapi_clean_arch.infra.controllers.health_check_controller import (
    HealthCheckController,
    HealthCheckUseCase,
)
from fastapi_clean_arch.infra.http.django_http_server import DjangoHttpServer
from fastapi_clean_arch.infra.http.fastapi_http_server import FastApiHttpServer
from fastapi_clean_arch.infra.http.flask_http_server import FlaskHttpServer

# server = DjangoHttpServer()
# server = FlaskHttpServer()
server = FastApiHttpServer()
health_check = HealthCheckUseCase()
controller = HealthCheckController(http_server=server, health_check=health_check)
server.serve()
