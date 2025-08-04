from .logger import GunicornLogger


def get_app_options(
    host: str,
    port: int,
    timeout: int,
    workers: int,
    loglevel: str,
) -> dict:
    return {
        "accesslog": "-",
        "errorlog": "-",
        "bind": f"{host}:{port}",
        "loglevel": loglevel,
        "logger_class": GunicornLogger,
        "timeout": timeout,
        "workers": workers,
        "worker_class": "uvicorn.workers.UvicornWorker",
    }
