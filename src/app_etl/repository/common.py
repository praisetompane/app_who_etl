from dotenv import dotenv_values
from src.app_etl.repository.postgres.connection import PostgresConnection
from src.app_etl.repository.postgres.postgres_configuration import PostgresConfiguration
from src.app_etl.repository.etl_repository import ETLRepository

config = dotenv_values(".env")

postgres_config = PostgresConfiguration(
    config["POSTGRES_HOST"],
    config["POSTGRES_PORT"],
    config["POSTGRES_DB"],
    config["POSTGRES_USER"],
    config["POSTGRES_PASSWORD"],
)

postgres_connection = PostgresConnection(postgres_config)

etl_repository = ETLRepository(postgres_connection)
