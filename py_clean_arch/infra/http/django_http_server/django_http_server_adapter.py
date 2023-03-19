from dataclasses import asdict
from os import environ
from typing import Any, Dict, List

import django
from django.contrib import admin
from django.core.management import call_command
from django.http import HttpRequest, JsonResponse
from django.urls import path
from django.views.decorators.http import require_http_methods

from py_clean_arch.application.protocols.controller_protocol import Controller


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
        def view(request: HttpRequest, *args, **kwargs) -> Any:
            output = controller.handle(body=request.body, params=request.headers)
            output_asdict = asdict(output)
            return JsonResponse(output_asdict)

        self.urlpatterns.append(path(url, view, name=f"{method.upper()}-{url}"))

    def __iter__(self) -> Any:
        return iter(self.urlpatterns)
