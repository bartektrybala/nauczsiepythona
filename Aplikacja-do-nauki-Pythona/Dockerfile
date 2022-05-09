FROM python:3.9-slim-bullseye

WORKDIR /aplikacja-do-nauki-pythona

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

COPY ./entrypoint.sh /aplikacja-do-nauki-pythona

# set priviliges for code exec security
RUN useradd -ms /bin/bash code-exec
RUN chmod -R 700 /aplikacja-do-nauki-pythona
RUN mkdir /exec_code && touch /exec_code/file.py && chmod 777 /exec_code/file.py
# for nginx
RUN chmod -R 777 /aplikacja-do-nauki-pythona/media

ENTRYPOINT [ "/bin/bash", "/aplikacja-do-nauki-pythona/entrypoint.sh"]