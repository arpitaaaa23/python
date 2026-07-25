import pandas as pd
data = {
    'Roll':[1,2,3],
    'name':['a','b','c','d','e','f','g'],
    'age':[1,2,3]
}
df = pd.DataFrame(data)
print(df.dtypes)