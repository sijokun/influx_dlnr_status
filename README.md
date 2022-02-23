# Бот, который пингует сервера в ДНР и ЛНР

Для отправки icmp запросов в linux библиотеке aioping требуются root права.

## Установка:

1. Склонировать репозиторий, установить окружение и требуемые библиотеки
    ```shell
    git clone https://github.com/Egorrko/dlnr_status.git
    cd dlnr_status
    python -m venv env
    source env/bin/activate  # linux
    env/Scripts/activate.bat  # windows
    pip install -r requirements.txt
    ```
2. Заполнить `settings.json`
    ```json
     "NODE_NAME": "Test node",
     "INFLUX_HOST": "127.0.0.1",
     "INFLUX_PORT": "8086",
     "INFLUX_DB": "dlnr"
    ```
3. Запустить.
    ```shell
    python app/main.py
    ```
    Docker
    ```
    git clone https://github.com/Egorrko/dlnr_status.git
    docker build -t dlnr_status_bot .
    # заполните settings.json
    docker run --rm -v ${PWD}/settings.json:/app/settings.json -d dlnr_status_bot
    ```
    Docker-compose
    ```
    git clone https://github.com/Egorrko/dlnr_status.git
    # заполните settings.json
    docker-compose up -d
    ```
