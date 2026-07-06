from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        case_sensitive=False,
        extra='ignore'
    )

    TEST_ENV_VAR: str
    IS_DEV: bool
    FRONTEND_URL_DEV : str
    FRONTEND_URL_PROD : str
    DB_URL_DEV : str
    DB_URL_PROD : str
    AUTH_SECRET_KEY : str

settings = Settings()