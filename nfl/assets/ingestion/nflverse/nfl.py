from dagster import graph_asset
from .ops import (
    ingest_nfl_pbp_2024, 
    ingest_nfl_players, 
    update_pbp_with_players_op
)

@graph_asset
def nfl_pbp_2024():
    """
    Graph asset for ingesting NFL PBP data and updating it with player information.
    """
    pbp_data = ingest_nfl_pbp_2024()
    players_data = ingest_nfl_players()
    # Return the result from the update operation
    return update_pbp_with_players_op(pbp_data, players_data)
