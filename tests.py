import pandas as pd
import numpy as np
import requests

def get_google_sheet_df(headers: dict, google_sheet_id: str, sheet_name: str, _range: str):
    """_range is in A1 notation (i.e. A:I gives all rows for columns A to I)"""

    url = f'https://docs.google.com/spreadsheets/d/1ZO0QYKQgvxBOGv7NxKhpcyojFTdxh6syazaTszQg-CY/edit?usp=sharing/{google_sheet_id}/values/{sheet_name}!{_range}'
    r = requests.get(url, headers=headers)
    values = r.json()['values']
    df = pd.DataFrame(values[1:])
    df.columns = values[0]
    df = df.apply(lambda x: x.str.strip()).replace('', np.nan)
    return df

headers = {'authorization': f'Bearer {access_token}',
           'Content-Type': 'application/vnd.api+json'}

google_sheet_id = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
sheet_name = 'Class Data'
sample_range = 'A:F'

df = get_google_sheet_df(headers, google_sheet_id, sheet_name, sample_range)


import os
test=os.environ.get('yahoo_mail')
print(test)

os.environ

print(os.environ.get('password'))

os.environ["password"]='Tunesaispas'

os.environ['USERNAME']

os.environ.get('yahoo_mail')
yahoo_mail=os.environ.get('USERNAME')