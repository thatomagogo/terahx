from main import df, pd

s1 = df['PurchaseDate']
s2 = df['CustomerID']

data = {
    "PurchaseDate": s1,
    "CustomerID": s2
}

df1 = pd.DataFrame(data)

df1['PurchaseDate'] = pd.to_datetime(df1['PurchaseDate'])
#print(df['PurchaseDate'])

df1['StartDate'] = '2023-06-11'
df1['StartDate'] = pd.to_datetime(df1['StartDate'])
#print(df1['StartDate'])

df1['Recency'] = df1['StartDate'] - df1['PurchaseDate']
#print(df1['Recency'])

#print(df1)

def assign_score(value):
    if value.days >= 41:
        return '1'
    elif 21 <= value.days <= 40:
        return '2'
    else:
        return '3'

df1['Scores'] = df1['Recency'].apply(assign_score)
#print(df1)

df6 = pd.DataFrame(df1).drop_duplicates(subset=['CustomerID']).sort_values(by=['CustomerID'])
#print(df6)

#df1.to_csv('new5.csv')