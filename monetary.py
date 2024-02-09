from main import df, pd

s4 = df['CustomerID']
s5 = df['TransactionAmount']

data = {
    "CustomerID": s4,
    "TransactionAmount": s5
}
df3 = pd.DataFrame(data)

m = df3.groupby('CustomerID')['TransactionAmount'].sum().reset_index()
#print(m)

df4 = pd.DataFrame(m)
#print(df4)

def assign_score(value):
    if value >= 1601:
        return '3'
    elif 801 <= value <= 1600:
        return '2'
    else:
        return '1'

df4['Scores'] = df4['TransactionAmount'].apply(assign_score)
#print(df4)