select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select total_penalties
from "nfl_database"."main"."penalty_totals"
where total_penalties is null



      
    ) dbt_internal_test