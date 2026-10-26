"""Application configuration for the Industrial Process Intelligence Copilot."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables or a .env file."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str = "petrochem"
    postgres_user: str = "petrochem"
    postgres_password: str = "petrochem"
    mlflow_tracking_uri: str = "http://localhost:5000"

    @property
    def database_url(self) -> str:
        """Build the PostgreSQL connection URL."""
        return (
            f"postgresql+psycopg2://{self.postgres_user}:"
            f"{self.postgres_password}@{self.postgres_host}:"
            f"{self.postgres_port}/{self.postgres_db}"
        )
