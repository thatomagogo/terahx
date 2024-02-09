import pandas as pd 

x = ["Thato", "Tshidiso", "Jutah", "Marvin", "Acqua"]
y = [33, 34, 37, 31, 30]

data = {
    "students": x,
    "age": y
}

df = pd.DataFrame(data)

print(df)