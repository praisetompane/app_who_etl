class PostgresConfiguration:

    def __init__(self, host, port, database_name, username, password) -> None:
        self.host = host
        self.port = port
        self.database_name = database_name
        self.username = username
        self.password = password

    def uri(self) -> str:
        return f"postgresql+psycopg2://{self.username}:{self.password}@{self.host}:{self.port}/{self.database_name}"
