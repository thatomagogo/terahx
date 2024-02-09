from main import pd
from frequency import df5
from monetary import df4
from recency import df6

s6 = pd.Series(df4['Scores']).apply(pd.to_numeric)
s7 = pd.Series(df5['Frequency']).to_numpy()
s8 = pd.Series(df6['Scores']).apply(pd.to_numeric).to_numpy()

data = {
    "CustomerID": df4['CustomerID'],
    "MScore": s6,
    "FScore": s7,
    "RScore": s8
}
df7 = pd.DataFrame(data)

#print(df7)