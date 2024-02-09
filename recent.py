from main import df, pd
from datetime import datetime

s1 = df['PurchaseDate']
s2 = df['CustomerID']

data = {
    "PurchaseDate": s1,
    "CustomerID": s2
}

df1 = pd.DataFrame(data).drop_duplicates(subset=['CustomerID'])
#print(df1)

d1 = '2023-06-11'
d2 = s1.loc[0]
dt1 = datetime.strptime(d1, '%Y-%m-%d').date()
dt2 = datetime.strptime(d2, '%Y-%m-%d').date()
delta = dt1 - dt2
print(delta.days)
