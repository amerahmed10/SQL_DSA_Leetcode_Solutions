import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    act_grouped = activity.sort_values(by=['player_id','event_date']).groupby('player_id').head(1)
    return act_grouped[['player_id','device_id']]

    