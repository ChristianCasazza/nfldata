
  
    
    

    create  table
      "nfl_database"."main"."distinct_teams__dbt_tmp"
  
    as (
      SELECT DISTINCT posteam 
FROM "nfl_database"."main"."nfl_pbp_2024"
    );
  
  