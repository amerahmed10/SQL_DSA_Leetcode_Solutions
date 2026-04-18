import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    data = pd.merge(project,employee,on='employee_id',how='inner')
    data = data.rename(columns={'experience_years':'average_years'})
    data = data.groupby('project_id')['average_years'].mean().round(2).reset_index()
    return data[['project_id','average_years']]
    