import uvicorn
from fastapi import FastAPI

from fastapi_clean_arch.application.protocols.controller_protocol import Controller


class FastApiHttpServer:
    def __init__(self) -> None:
        self._app = FastAPI()

    def serve(self, port: int = 8000) -> None:
        uvicorn.run(self._app, port=port)

    def on(self, method: str, url: str, controller: Controller) -> None:
        self._app.add_api_route(
            path=url, endpoint=controller.handle, methods=[method.upper()]
        )
