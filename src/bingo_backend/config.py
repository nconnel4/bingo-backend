from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    database_url: str
    database_username: str
    database_password: SecretStr
    database_port: int = 5432
    database_name: str

    @property
    def connection_string(self):
        return f"postgresql://{self.database_username}:{self.database_password.get_secret_value()}@{self.database_url}:{self.database_port}/{self.database_name}"

    redis_url: str

    model_config = SettingsConfigDict(env_file=".env")