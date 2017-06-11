import pandas as pd
from datetime import datetime
#data loading
sp = pd.read_csv("sphist.csv")

#convert dtype for Date column
sp["Date"] = pd.to_datetime(sp["Date"])

#sort by ascending dates
sp = sp.sort("Date")

#reset index 
sp = sp.reset_index(drop = True) 

# 5 day moving average
day_5 = pd.rolling_mean(sp["Close"], window = 5)
sp["day_5"] = day_5.shift()

# 30 days moving average
day_30 = pd.rolling_mean(sp["Close"], window = 30)
sp["day_30"] = day_30.shift()

#rolling 5 day standard deviation
std_5 = pd.rolling_std(sp["Close"], window = 5)
sp["std_5"] = std_5.shift()

#rolling 30 day standard deviation
std_30 = pd.rolling_std(sp["Close"], window = 30)
sp["std_30"] = std_30.shift()

#rolling 5 day average volume
vol_5 = pd.rolling_mean(sp["Volume"], window = 5)
sp["vol_5"] = vol_5.shift()

#removing rows before 1951-01-02 due to missing data generated from indicators
sp = sp[sp["Date"] > datetime(year = 1951, month = 1, day = 2)]

sp = sp.dropna(axis = 0)
sp = sp.reset_index(drop = True) 

#split into training and test data
train = sp[sp["Date"] < datetime(year = 2013, month = 1, day =1)]

test = sp[sp["Date"] >= datetime(year = 2013, month = 1, day =1)] 

#model 1: LinearRegression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
#instantiating model
lr = LinearRegression()
columns = list(train.columns)
columns = columns[7:12]
lr.fit(train[columns], train["Close"])
pred = lr.predict(train[columns])
mse = mean_squared_error(train["Close"], pred) 

#challenge to reduce error by adding 2 more indicators
print(mse)  
# manage to reduce MSE by adding 2 more indicators