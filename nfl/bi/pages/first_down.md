
---
title: 1st Down Stats
---

# 1st down stats

## 1st Down Tendencies per Team


```sql unique_teams
select 
posteam 
from pbp.distinct_teams
group by 1
```

<Dropdown
    name=unique_teams
    data={unique_teams}
    value=posteam
    title="Select a Team" 
    defaultValue="MIA"
/>

```team_breakdown
select * from pbp.team_breakdown
where posteam = '${inputs.unique_teams.value}'
```

<DataTable data={team_breakdown} />

