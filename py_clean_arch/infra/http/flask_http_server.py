import json
from typing import Any, Dict

from flask import Flask, Request, Response, request

from py_clean_arch.application.protocols.controller_protocol import Controller
from py_clean_arch.infra.http.helpers import HttpRequest


def get_query_params_as_dict(request: Request) -> Dict[Any, Any]:
    query_params: Dict[Any, Any] = {}
    for key, value in request.args.items():
        values_as_list = request.args.getlist(key)
        if len(values_as_list) > 1:
            query_params[key] = values_as_list
            continue
        query_params[key] = value
    return query_params


class FlaskHttpServer:
    def __init__(self, debug: bool = False) -> None:
        self._debug_mode = debug
        self._app = Flask(__name__)

    def serve(self, port: int = 8000) -> None:
        self._app.run(host="0.0.0.0", port=port, debug=self._debug_mode)

    def on(self, method: str, url: str, controller: Controller) -> None:
        async def view() -> Any:
            body: Dict[str, Any] = {}
            request_data: Request = request
            if request_data.is_json and request_data.data:
                body = request_data.json.items()  # type: ignore
            application_request = HttpRequest(
                headers={**request.headers},
                body=body,
                params=get_query_params_as_dict(request),
            )
            response = controller.handle(request=application_request)
            return Response(
                json.dumps(response.body),
                status=response.status_code,
                headers=response.headers,
                content_type="application/json",
            )

        self._app.add_url_rule(url, None, view, methods=[method.upper()])
        self._app.add_url_rule(url + "/", None, view, methods=[method.upper()])
