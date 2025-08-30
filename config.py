from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="allow"
    )

    model_name: str = Field(default="meta-llama/Llama-3.1-8B-Instruct")
    offload_to_cpu: bool = Field(default=True)
    vram_in_GiB: str = Field(default=16)
    cpu_in_GiB: str = Field(default=20)
    data_count: int = Field(default=1000)
    database_url: str = Field(default="")


config = Settings()
