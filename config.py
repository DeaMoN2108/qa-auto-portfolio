from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).parent
ENV_FILE_PATH = ROOT_DIR / ".env"

class Settings(BaseSettings):
    base_url: str
    standard_user: str
    problem_user: str
    password: str
    checkout_one_page_url: str
    checkout_two_page_url: str
    checkout_complete_page_url: str
    first_name: str
    last_name: str
    postal_code: str
    api_base_url: str
    model_config = SettingsConfigDict(env_file=ENV_FILE_PATH, extra="ignore")

config = Settings()