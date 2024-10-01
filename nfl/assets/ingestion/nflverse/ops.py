import duckdb
import polars as pl
from dagster import op, get_dagster_logger
from nfl.constants import NFL_DUCKDB_PATH

@op
def ingest_nfl_pbp_2024() -> pl.DataFrame:
    """
    Ingest NFL PBP data as a Polars DataFrame.
    """
    url = "https://github.com/nflverse/nflverse-data/releases/download/pbp/play_by_play_2024.parquet"
    return pl.read_parquet(url)

@op
def ingest_nfl_players() -> pl.DataFrame:
    """
    Ingest NFL player data as a Polars DataFrame.
    """
    url = "https://github.com/nflverse/nflverse-data/releases/download/players/players.parquet"
    return pl.read_parquet(url)

@op
def update_pbp_with_players_op(context, nfl_pbp_2024: pl.DataFrame, nfl_players: pl.DataFrame) -> None:
    """
    Update the NFL PBP table with player names and positions after storing them in DuckDB.
    """
    logger = get_dagster_logger()
    con = duckdb.connect(NFL_DUCKDB_PATH)

    # Step 1: Persist the ingested Polars DataFrames to DuckDB as base tables
    logger.info("Persisting NFL PBP and Player data to DuckDB...")
    con.execute("DROP TABLE IF EXISTS nfl_pbp_2024;")  # Ensure old table is dropped
    con.execute("DROP TABLE IF EXISTS nfl_players;")
    
    # Write the data into DuckDB
    con.register("nfl_pbp_2024_df", nfl_pbp_2024)  # Register the Polars DataFrame
    con.execute("CREATE TABLE nfl_pbp_2024 AS SELECT * FROM nfl_pbp_2024_df;")  # Create DuckDB table

    con.register("nfl_players_df", nfl_players)  # Register the Polars DataFrame
    con.execute("CREATE TABLE nfl_players AS SELECT * FROM nfl_players_df;")  # Create DuckDB table

    # Step 2: Add necessary columns to the base table
    logger.info("Adding necessary columns...")
    columns_to_add = [
        "passer_display_name STRING",
        "passer_position STRING",
        "rusher_display_name STRING",
        "rusher_position STRING",
        "receiver_display_name STRING",
        "receiver_position STRING"
    ]
    
    for column in columns_to_add:
        try:
            con.execute(f"ALTER TABLE nfl_pbp_2024 ADD COLUMN {column}")
            logger.info(f"Column {column} added.")
        except Exception as e:
            logger.warning(f"Column {column} already exists or error: {e}")

    # Step 3: Update the table based on player IDs
    logger.info("Updating the PBP table with player data...")
    con.execute("""
        UPDATE nfl_pbp_2024
        SET passer_display_name = p.display_name, 
            passer_position = p.position
        FROM nfl_players p
        WHERE nfl_pbp_2024.passer_player_id = p.gsis_id
    """)

    # Similar updates for rushers and receivers...
    con.execute("""
        UPDATE nfl_pbp_2024
        SET rusher_display_name = p.display_name, 
            rusher_position = p.position
        FROM nfl_players p
        WHERE nfl_pbp_2024.rusher_player_id = p.gsis_id
    """)
    
    con.execute("""
        UPDATE nfl_pbp_2024
        SET receiver_display_name = p.display_name, 
            receiver_position = p.position
        FROM nfl_players p
        WHERE nfl_pbp_2024.receiver_player_id = p.gsis_id
    """)

    # Step 4: Verify results
    result = con.execute("SELECT * FROM nfl_pbp_2024 LIMIT 10").fetchdf()
    logger.info(f"Updated PBP data: {result}")
    con.close()
