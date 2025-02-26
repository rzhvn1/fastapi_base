from pydantic import BaseModel
from pydantic import PostgresDsn
from pydantic_settings import (
	BaseSettings, 
	SettingsConfigDict
)


class RunConfig(BaseModel):
	host: str = "0.0.0.0"
	port: str = 8000


class ApiPrefix(BaseModel):
	prefix: str = "/api"


class DatabaseConfig(BaseModel):
	url: PostgresDsn
	echo: bool = False
	echo_pool: bool = False
	pool_size: int = 50
	max_overflow: int = 10


class Settings(BaseSettings):
	model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_prefix="APP_CONFIG__",
    )
	run: RunConfig = RunConfig()
	api: ApiPrefix = ApiPrefix()
	db: DatabaseConfig

from pydantic import ValidationError

try:
    settings = Settings()
    print(settings.model_dump())  # Print parsed settings
except ValidationError as e:
    print("Pydantic Validation Error:", e.json(indent=2))  # Print detailed errors
