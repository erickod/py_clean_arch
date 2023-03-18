from typing import Any, Callable

from flask import Flask


class FlaskHttpServer:
    def __init__(self) -> None:
        self._app = Flask(__name__)

    def serve(self) -> None:
        self._app.run(port=8000)

    def on(self, method: str, url: str, controller: Callable) -> None:
        self._app.add_url_rule(url, None, controller, {"methods": [method.upper()]})
