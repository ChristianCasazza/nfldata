from dagster_duckdb_polars import DuckDBPolarsIOManager
from nfl.constants import NFL_DUCKDB_PATH

# Custom IO Manager for NFL
class NFLDuckDBPolarsIOManager(DuckDBPolarsIOManager):
    def __init__(self, database=NFL_DUCKDB_PATH, schema="nfl_schema"):
        super().__init__(database=database, schema=schema)

