from main import pd
from test import df7

df8 = pd.DataFrame(df7)
#print(df8.dtypes)

df8['RFMScore'] = df8['RScore'] + df8['FScore'] + df8['MScore']
print(df8)