import json
from pathlib import Path
from typing import List

from model import Server
from pydantic import BaseSettings

SETTINGS_PATH = 'settings.json'


class Settings(BaseSettings):
    TIMEZONE: str
    NODE_NAME: str
    INFLUX_HOST: str
    INFLUX_PORT: int
    INFLUX_DB: str
    SERVERS: List[Server]

    class Config:
        env_file_encoding = 'utf-8'

        @classmethod
        def customise_sources(cls, init_settings, env_settings, file_secret_settings,):
            return (lambda _: json.loads(Path(SETTINGS_PATH).read_bytes()),)

    def save(self):
        Path(SETTINGS_PATH).write_text(self.json(ensure_ascii=False, indent=2), encoding='utf-8')


settings = Settings()
