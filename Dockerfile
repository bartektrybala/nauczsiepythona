FROM python:3.8-slim-bullseye

WORKDIR /aplikacja-do-nauki-pythona

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

COPY ./entrypoint.sh /aplikacja-do-nauki-pythona
ENTRYPOINT [ "sh", /aplikacja-do-nauki-pythona/entrypoint.sh ]
CMD ["python3", ""]