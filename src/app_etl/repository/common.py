from src.app_etl.repository.postgres.connection import PostgresConnection
from src.app_etl.repository.postgres.postgres_configuration import PostgresConfiguration
from src.app_etl.repository.etl_repository import ETLRepository
import os


postgres_config = PostgresConfiguration(
    os.environ.get("POSTGRES_HOST"),
    os.environ.get("POSTGRES_PORT"),
    os.environ.get("POSTGRES_DB"),
    os.environ.get("POSTGRES_USER"),
    os.environ.get("POSTGRES_PASSWORD")
)

postgres_connection = PostgresConnection(postgres_config)

etl_repository = ETLRepository(postgres_connection)
