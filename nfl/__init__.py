import os
from dagster import Definitions
from nfl.resources.io.DuckDBPolarsIO import NFLDuckDBPolarsIOManager
from nfl.resources.io.DuckDBBIExport import duckdb_bi_export_io_manager
from dagster_dbt import DbtCliResource
from .assets.ingestion.nflverse.nfl import nfl_pbp_2024
from .assets.ingestion.nflverse.ops import ingest_nfl_players, ingest_nfl_pbp_2024, update_pbp_with_players_op
from .assets.dbt import dbt_project_assets  # Import the dbt assets
from .assets.bi.export import analytics_cube  # Import the analytics_cube asset
from .resources.dbt_project import dbt_project
from nfl.constants import NFL_DUCKDB_PATH, BI_DUCKDB_PATH, SQL_FOLDER

# Define the assets (Parquet data and Bloombet API data)
nfl_assets = [nfl_pbp_2024]  # Using graph-backed asset


# Resource definitions, including the I/O manager for DuckDB
resources = {
    "dbt": DbtCliResource(project_dir=dbt_project),
    "nfl_io_manager": NFLDuckDBPolarsIOManager(),  # Correctly instantiate the NFL IO Manager
    "duckdb_bi_export_io_manager": duckdb_bi_export_io_manager.configured({
        "input_duckdb_path": NFL_DUCKDB_PATH,
        "sql_folder": SQL_FOLDER,
        "export_duckdb_path": BI_DUCKDB_PATH,
    }),  # Configured DuckDB BI Export IO Manager
}

# Dagster Definitions for assets, resources, and jobs
defs = Definitions(
    assets=nfl_assets + [dbt_project_assets, analytics_cube],  # Include DBT assets and analytics_cube
    resources=resources
)
