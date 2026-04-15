import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers_no = customers[~customers['id'].isin(orders['customerId'])]
    customers_no.rename(columns={'name':'Customers'},inplace=True)
    return customers_no[['Customers']]
    