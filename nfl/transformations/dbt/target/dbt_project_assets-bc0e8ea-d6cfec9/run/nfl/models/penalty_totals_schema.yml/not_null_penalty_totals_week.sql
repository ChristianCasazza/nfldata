select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select week
from "nfl_database"."main"."penalty_totals"
where week is null



      
    ) dbt_internal_test