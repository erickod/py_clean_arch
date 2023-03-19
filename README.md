## About this project

This project is an use example of the Uncle Bob's Clean Architecture, and here we are using some dependencies:
- FastApi
- Django
- Flask

There's an abstraction called `HttpServer` implemented to each framework above, and this abstraction works with a `controller` implementing it's own `route`;

Also you'll see the `HealthCheckUseCase` and the `HealthCheckController` as an example/way of how implement your own routes; 

## How run this project
- Install poetry: https://python-poetry.org/docs/#installation
- Inside the `py_clean_arch` dir call `poetry shell` and `poetry install`
- Go to the `main.py` file and choose one of the servers (FastApiHttpServer, FlaskHttpServer, DjangoHttpServer)
and let the others commented:
- If your chooice was the `DjangoHttpServer`, run the default Django migrations inside the `py_clean_arch` dir using the `python infra/http/django_http_server/manage.py migrate` command;
- Inside the `py_clean_arch` dir run the project by calling `python main.py`
- To check the server running make a `GET` request to the `/health_check/` endpoint and you'll get it:
```json
{"http_server": "DjangoHttpServer", "status": "running"}
```

I hope it helps. Feel free to propose any changes.