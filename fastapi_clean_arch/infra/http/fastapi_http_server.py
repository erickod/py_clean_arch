from typing import Callable

import uvicorn
from fastapi import FastAPI


class FastApiHttpServer:
    def __init__(self) -> None:
        self._app = FastAPI()

    def serve(self, port: int = 8000) -> None:
        uvicorn.run(self._app, port=port)

    def on(self, method: str, url: str, controller: Callable) -> None:
        self._app.add_api_route(path=url, endpoint=controller, methods=[method.upper()])
