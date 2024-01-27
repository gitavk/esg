from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=True)
    PROJECT_NAME: str
    SQLALCHEMY_DATABASE_URI: str


settings = Settings()
