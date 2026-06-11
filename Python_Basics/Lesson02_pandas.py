import pandas as pd

data = {
    "Name": ["john","rain","king"],
    "Age": [12,34,32],
    "Student": [True,False,True]
}

df = pd.DataFrame(data, columns=["Name", "Age","Student"])

print(df.iloc[1])