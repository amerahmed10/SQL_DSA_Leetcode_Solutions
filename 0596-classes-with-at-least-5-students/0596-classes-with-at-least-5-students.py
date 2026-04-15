import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    count = courses['class'].value_counts()
    count = count[count>=5].index
    return pd.DataFrame(count, columns=['class'])