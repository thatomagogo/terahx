from main import df, pd

s3 = df['CustomerID']

data = {
    "CustomerID": s3
}
df2 = pd.DataFrame(data)

f = df2['CustomerID'].value_counts()
#print(f)

df2['Frequency'] = df2['CustomerID'].map(f)
#print(df2)

df5 = pd.DataFrame(df2).drop_duplicates(subset=['CustomerID']).sort_values(by=['CustomerID'])
#print(df5)
