import duckdb
import logging

logger = logging.getLogger("common")


class DatabaseConnection:

    CONFIG = """
        SET enable_progress_bar = true;
        SET enable_progress_bar_print = true;
    """

    def __init__(self, database: str):
        self.database = database
        try:
            with duckdb.connect(self.database) as conn:
                logger.info(f"Connected to database: {self.database}")
        except Exception:
            logger.exception(f"Failed to connect to database: {self.database}")

    def execute(self, query: str):
        logger.debug(f"Executing query: {query}\non database: {self.database}")
        try:
            with duckdb.connect(self.database) as conn:
                conn.execute(self.CONFIG)
                logger.debug(
                    f"Configuration settings applied:\n{self.CONFIG.strip()}"
                )
                logger.debug(
                    query
                )
                logger.info("Executing query...")
                result = conn.execute(query).df()
                logger.info("Query executed successfully")
                return result
        except Exception:
            logger.exception("Error executing query")
