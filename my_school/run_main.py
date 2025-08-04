__all__ = (
    "app_main",
    "main",
)

from core.config import setting
from core.gunicorn_app import Application, get_app_options
from main import app_main


def main():
    Application(
        app=app_main,
        options=get_app_options(
            host=setting.gunicorn.host,
            port=setting.gunicorn.port,
            workers=setting.gunicorn.workers,
            timeout=setting.gunicorn.timeout,
            loglevel=setting.logging.log_level,
        ),
    ).run()


if __name__ == "__main__":
    main()
