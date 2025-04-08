FROM python:3.10.0

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

#RUN alembic upgrade head
