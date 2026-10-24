from pathlib import Path

import pytest

from config import Settings


@pytest.mark.unit
def test_default_settings(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.chdir(tmp_path)

    for name in (
        "POSTGRES_HOST",
        "POSTGRES_PORT",
        "POSTGRES_DB",
        "POSTGRES_USER",
        "POSTGRES_PASSWORD",
        "MLFLOW_TRACKING_URI",
    ):
        monkeypatch.delenv(name, raising=False)

    settings = Settings()

    assert settings.postgres_host == "localhost"
    assert settings.postgres_port == 5432
    assert settings.postgres_db == "petrochem"
    assert settings.mlflow_tracking_uri == "http://localhost:5000"


@pytest.mark.unit
def test_database_url(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.chdir(tmp_path)

    settings = Settings(
        postgres_host="db.example.com",
        postgres_port=5433,
        postgres_db="testdb",
        postgres_user="testuser",
        postgres_password="testpass",
    )

    assert settings.database_url == (
        "postgresql+psycopg2://testuser:testpass@db.example.com:5433/testdb"
    )


@pytest.mark.unit
def test_environment_variable_override(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("POSTGRES_HOST", "test-database")

    settings = Settings()

    assert settings.postgres_host == "test-database"
