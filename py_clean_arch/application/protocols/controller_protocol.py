from typing import Any, Dict, Protocol


class HttpServer(Protocol):
    def serve(self, port: int = 8000) -> None:
        ...

    def on(self, method: str, url: str, controller: "Controller") -> None:
        ...


class Controller(Protocol):
    http_server: HttpServer

    def __init__(self, http_server: HttpServer) -> None:
        ...

    def handle(self, body: Dict[Any, Any] = {}, params: Dict[Any, Any] = {}) -> Any:
        ...
