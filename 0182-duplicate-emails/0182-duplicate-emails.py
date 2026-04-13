import pandas as pd
def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    dup = person['email'].value_counts()
    dup = dup[dup > 1].index.tolist()
    dup = pd.DataFrame(dup,columns=['email'])
    return dup