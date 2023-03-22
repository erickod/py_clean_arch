import contextlib
import json
from os import environ
from typing import Any, Dict, List

import django
from django.contrib import admin
from django.core.management import call_command
from django.http import HttpRequest as DjangoRequest
from django.http import JsonResponse
from django.urls import path
from django.views.decorators.http import require_http_methods

from py_clean_arch.application.protocols.controller_protocol import Controller
from py_clean_arch.infra.http.helpers.http_request import HttpRequest


class Borg(object):
    _state: Dict[Any, Any] = {}

    def __new__(
        cls,
        *args,
        shared_state: bool = True,
        **kwargs,
    ):
        instance = super(Borg, cls).__new__(cls)
        if shared_state:
            instance.__dict__ = Borg._state
        return instance


def get_query_params_as_dict(request: DjangoRequest) -> Dict[Any, Any]:
    query_params: Dict[Any, Any] = {}
    for key, value in request.GET.items():
        values_as_list = request.GET.getlist(key)
        if len(values_as_list) > 1:
            query_params[key] = values_as_list
            continue
        query_params[key] = value
    return query_params


class DjangoHttpServer(Borg):
    def __init__(self) -> None:
        environ.setdefault(
            "DJANGO_SETTINGS_MODULE",
            "py_clean_arch.infra.http.django_http_server.django_http_server.settings",
        )
        django.setup()
        self.urlpatterns: List[Any] = getattr(
            self,
            "urlpatterns",
            [
                path("admin/", admin.site.urls),
            ],
        )

    def serve(self, port: int = 8000) -> None:
        call_command("runserver", f"127.0.0.1:{port}")

    def on(self, method: str, url: str, controller: Controller) -> None:
        url = url[1:] + "/"

        @require_http_methods([method.upper()])
        def view(request: DjangoRequest, *args, **kwargs) -> Any:
            applicaton_request = HttpRequest(
                body=self.__get_body_as_dict(request),
                params=get_query_params_as_dict(request),
                headers=request.headers,
            )
            output = controller.handle(request=applicaton_request)
            return JsonResponse(
                output.body, status=output.status_code, headers=output.headers
            )

        self.urlpatterns.append(path(url, view, name=f"{method.upper()}-{url}"))

    def __get_body_as_dict(self, request: DjangoRequest) -> Dict[Any, Any]:
        with contextlib.suppress(json.decoder.JSONDecodeError):
            return json.loads(request.body)
        return {}

    def __iter__(self) -> Any:
        return iter(self.urlpatterns)
