import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    data = pd.merge(users,rides, left_on='id',right_on='user_id',how='left',suffixes=('_left','_right'))
    data = data.groupby(['id_left','name'])['distance'].sum().reset_index().fillna(0)
    data = data.sort_values(by=['distance','name'],ascending=[False,True])
    data = data.rename(columns={'distance':'travelled_distance'})
    return data[['name','travelled_distance']]
    