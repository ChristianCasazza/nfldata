---
title: Passing Stats
---

- View stats for QBs


## Passer Stats

```sql passer_data
select 
* 
from pbp.passer_stats
```

<DataTable data={passer_data} />


```unique_players
SELECT DISTINCT player_name
FROM pbp.passer_stats
```


<Dropdown
    name=unique_players
    data={unique_players}
    value=player_name
    title="Select a Player" 
    defaultValue="Patrick Mahomes"
/>

```indy_player_stats
select * from pbp.passer_stats
where player_name = '${inputs.unique_players.value}'
```

<BigValue 
  data={indy_player_stats} 
  value=pass_touchdowns
  title="Passing Touchdowns"
/>

<BigValue 
  data={indy_player_stats} 
  value=total_epa
  title="Total EPA"
/>


<BigValue 
  data={indy_player_stats} 
  value=pass_attempts
  title="Pass Attempts"
/>

<BigValue 
  data={indy_player_stats} 
  value=completions
  title="Completions"
/>

<BigValue 
  data={indy_player_stats} 
  value=completion_percentage
  fmt=pct1
  title="Completion Percentage"
/>

<BigValue 
  data={indy_player_stats} 
  value=total_passing_yards
  title="Total Passing Yards"
/>

<BigValue 
  data={indy_player_stats} 
  value=total_air_yards
  title="Total Air Yards"
/>

<BigValue 
  data={indy_player_stats} 
  value=yac_yards
  title="YAC Yards"
/>

<BigValue 
  data={indy_player_stats} 
  value=interceptions
  title="Interceptions"
/>

<BigValue 
  data={indy_player_stats} 
  value=sacks
  title="Sacks"
/>


<BigValue 
  data={indy_player_stats} 
  value=total_hits
  title="Total QB Hits"
/>

<BigValue 
  data={indy_player_stats} 
  value=percentage_from_yac
  fmt=pct1
  title="Percentage of Yards from YAC"
/>

<BigValue 
  data={indy_player_stats} 
  value=interception_rate
  fmt=pct1
  title="Interception Rate"
/>

<BigValue 
  data={indy_player_stats} 
  value=sack_rate
  fmt=pct1
  title="Sack Rate"
/>

<BigValue 
  data={indy_player_stats} 
  value=qb_hit_rate
  fmt=pct1
  title="QB Hit Rate"
/>

