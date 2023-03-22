from typing import Any, Dict, Protocol

from py_clean_arch.infra.http.helpers.http_request import HttpRequest
from py_clean_arch.infra.http.helpers.http_response import HttpResponse


class HttpServer(Protocol):
    def serve(self, port: int = 8000) -> None:
        ...

    def on(self, method: str, url: str, controller: "Controller") -> None:
        ...


class Controller(Protocol):
    http_server: HttpServer

    def __init__(self, http_server: HttpServer) -> None:
        ...

    def handle(self, request: HttpRequest) -> HttpResponse:
        ...
