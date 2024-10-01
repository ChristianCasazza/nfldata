
---
title: Flex Stats
---

Markdown can be used to write expressively in text.

- **View stats** for _RBs_, _WRs_, and _TEs_




## EPA Leaders from RBs. WRs, and TEs:

```sql flex_data
select 
* 
from pbp.flex_stats
```

<DataTable data={flex_data} />


```unique_players
SELECT DISTINCT Player_Name
FROM pbp.flex_stats
```


<Dropdown
    name=unique_players
    data={unique_players}
    value=Player_Name
    title="Select a Player" 
    defaultValue="Jaylen Waddle"
/>

```indy_player_stats
select * from pbp.flex_stats
where Player_Name = '${inputs.unique_players.value}'
```

<BigValue 
  data={indy_player_stats} 
  value=Total_EPA
  title="Total Expected Points Added (EPA)"
/>

<BigValue 
  data={indy_player_stats} 
  value=Total_Yards
  title="Total Yards"
/>

<BigValue 
  data={indy_player_stats} 
  value=Total_Pass_Targets
  title="Total Pass Targets"
/>

<BigValue 
  data={indy_player_stats} 
  value=Total_Catches
  title="Total Catches"
/>

<BigValue 
  data={indy_player_stats} 
  value=Total_Receiving_Yards
  title="Total Receiving Yards"
/>

<BigValue 
  data={indy_player_stats} 
  value=Total_Rush_Attempts
  title="Total Rush Attempts"
/>

<BigValue 
  data={indy_player_stats} 
  value=Total_Rushing_Yards
  title="Total Rushing Yards"
/>


<BigValue 
  data={indy_player_stats} 
  value=Total_First_Downs_Rush
  title="Total First Downs (Rush)"
/>

<BigValue 
  data={indy_player_stats} 
  value=Total_First_Downs_Pass
  title="Total First Downs (Pass)"
/>

<BigValue 
  data={indy_player_stats} 
  value=Total_Third_Down_Conversions
  title="Total Third Down Conversions"
/>

<BigValue 
  data={indy_player_stats} 
  value=Total_Fourth_Down_Conversions
  title="Total Fourth Down Conversions"
/>

<BigValue 
  data={indy_player_stats} 
  value=First_Down_Rush_Rate
  fmt=pct1
  title="First Down Rush Rate"
/>

<BigValue 
  data={indy_player_stats} 
  value=First_Down_Pass_Rate
  fmt=pct1
  title="First Down Pass Rate"
/>

<BigValue 
  data={indy_player_stats} 
  value=Catch_Rate
  fmt=pct1
  title="Catch Rate"
/>

<BigValue 
  data={indy_player_stats} 
  value=Average_Rushing_Yards_Per_Attempt
  title="Average Rushing Yards Per Attempt"
/>

<BigValue 
  data={indy_player_stats} 
  value=Average_Receiving_Yards_Per_Target
  title="Average Receiving Yards Per Target"
/>

