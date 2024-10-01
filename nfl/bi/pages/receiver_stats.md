
---
title: Receiver_Stats_Per_Team
description: View detailed stats on penalties committed by the Miami Dolphins
---


## Total Penalties per Week (Breakdown by Penalty Type):

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

```receivers_stats
select * from pbp.receiver_stats_per_team
where Team = '${inputs.unique_teams.value}'
```
<DataTable data={receivers_stats} />

```unique_receivers
SELECT DISTINCT Receiver_Name
FROM pbp.receiver_stats_per_team
WHERE Team = '${inputs.unique_teams.value}';
```

<Dropdown
    name=unique_receivers
    data={unique_receivers}
    value=Receiver_Name
    title="Select a Player" 
    defaultValue="Jaylen Waddle"
/>

```indy_receiver_stats
select * from pbp.receiver_stats_per_team
where Receiver_Name = '${inputs.unique_receivers.value}'
```


<BigValue 
  data={indy_receiver_stats} 
  value=Targets
  title="Targets"
/>

<BigValue 
  data={indy_receiver_stats} 
  value=Total_Catches
  title="Total Catches"
/>

<BigValue 
  data={indy_receiver_stats} 
  value=Total_Yards
  title="Total Yards"
/>

<BigValue 
  data={indy_receiver_stats} 
  value=Total_Air_Yards
  title="Total Air Yards"
/>

<BigValue 
  data={indy_receiver_stats} 
  value=Adj_Air_Yards
  title="Adjusted Air Yards"
/>

<BigValue 
  data={indy_receiver_stats} 
  value=Total_YAC
  title="Total Yards After Catch"
/>

<BigValue 
  data={indy_receiver_stats} 
  value=Total_Touchdowns
  title="Total Touchdowns"
/>

<BigValue 
  data={indy_receiver_stats} 
  value=Targeted_Interceptions
  title="Targeted Interceptions"
/>

<BigValue 
  data={indy_receiver_stats} 
  value=YAC_Percentage
  fmt=pct1
  title="YAC Percentage"
/>

<BigValue 
  data={indy_receiver_stats} 
  value=Total_First_Down_Passes
  title="First Down Passes"
/>

<BigValue 
  data={indy_receiver_stats} 
  value=Third_Down_Conversions
  title="Third Down Conversions"
/>

<BigValue 
  data={indy_receiver_stats} 
  value=Fourth_Down_Conversions
  title="Fourth Down Conversions"
/>

<BigValue 
  data={indy_receiver_stats} 
  value=Total_Conversions
  title="Total Conversions"
/>

<BigValue 
  data={indy_receiver_stats} 
  value=Third_Down_Success_Rate
  fmt=pct1
  title="Third Down Success Rate"
/>

<BigValue 
  data={indy_receiver_stats} 
  value=Fourth_Down_Success_Rate
  fmt=pct1
  title="Fourth Down Success Rate"
/>

<BigValue 
  data={indy_receiver_stats} 
  value=Both_Down_Success_Rate
  fmt=pct1
  title="Third and Fourth Down Success Rate"
/>

<BigValue 
  data={indy_receiver_stats} 
  value=Total_EPA
  title="Total Expected Points Added (EPA)"
/>
