from typing import Any, Callable, Dict, Protocol


class HttpServer(Protocol):
    def serve(self) -> None:
        ...

    def on(self, method: str, url: str, controller: Callable) -> None:
        ...


class Controller(Protocol):
    http_server: HttpServer

    def __init__(self, http_server: HttpServer) -> None:
        ...

    def handle(self, body: Dict[Any, Any] = {}, params: Dict[Any, Any] = {}) -> Any:
        ...
