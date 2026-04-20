import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    data = pd.merge(employee,bonus,on='empId',how='left')
    data = data[(data['bonus']<1000) | (data['bonus'].isna())]
    return data[['name','bonus']]