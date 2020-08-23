import pandas as pd


filename = "C:/Users/Benra/OneDrive/Documents/PumpItUp/training_set_values.csv"
train = pd.read_csv(filename)




print(train.isna().sum())
