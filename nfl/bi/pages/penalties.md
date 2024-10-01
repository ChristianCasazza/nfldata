
---
title: NFL Penalties
description: View detailed stats on penalties committed by the Miami Dolphins
---


## Total Penalties per Week (Breakdown by Penalty Type):

```total_penalties_per_week_query
select * from pbp.penalty_totals
```

<BarChart 
    data={total_penalties_per_week_query}
    x=week
    y=total_penalties
    series=penalty_type
    title="Total Penalties per Week (Breakdown by Penalty Type)"
/>

```sql unique_penalties
select 
    penalty_type
from pbp.penalties_per_team
group by 1
```
<Dropdown
    name=penalty_type
    data={unique_penalties}
    value=penalty_type
/>

```sql penalties_per_team
select * 
from pbp.penalties_per_team
where penalty_type = '${inputs.penalty_type.value}'
```

<DataTable data={penalties_per_team} />

```sql penalties_per_team_full
select * 
from pbp.penalties_per_team
```

<DataTable data={penalties_per_team_full} />

