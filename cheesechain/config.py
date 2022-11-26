from pydantic import BaseSettings


class Config(BaseSettings):
    class Config:
        env_prefix = "cheesechain_"
        env_file = ".env"
        env_file_encoding = "utf-8"

    token: str
    guild_id: str = "497544520695808000"


config = Config()

__all__ = ["config"]
