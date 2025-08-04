FROM python:3.12.11-bookworm

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN pip install --upgrade pip wheel "poetry==2.1.3"

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY my_school .

COPY my_school/prestart.sh .
COPY my_school/run.py .

RUN chmod +x prestart.sh
RUN chmod +x run.py

ENTRYPOINT ["./prestart.sh"]

CMD ["python", "run.py"]