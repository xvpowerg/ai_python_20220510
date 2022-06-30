import pandas as pd
data_url = 'http://bit.ly/2cLzoxH'
gap1 = pd.read_csv(data_url)
print(gap1.head(3))