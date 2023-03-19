from dataclasses import asdict
from typing import Any, Dict

from flask import Flask, Request, request

from fastapi_clean_arch.application.protocols.controller_protocol import Controller


class FlaskHttpServer:
    def __init__(self) -> None:
        self._app = Flask(__name__)

    def serve(self, port: int = 8000) -> None:
        self._app.run(host="0.0.0.0", port=port, debug=True)

    def on(self, method: str, url: str, controller: Controller) -> None:
        async def view() -> Any:
            body: Dict[str, Any] = {}
            request_data: Request = request
            if request_data.is_json and request_data.data:
                body = request_data.json.items()  # type: ignore
            output = controller.handle(
                body=body,
                params=dict(request.headers),
            )
            return asdict(output)

        self._app.add_url_rule(url, None, view, methods=[method.upper()])
        self._app.add_url_rule(url + "/", None, view, methods=[method.upper()])
