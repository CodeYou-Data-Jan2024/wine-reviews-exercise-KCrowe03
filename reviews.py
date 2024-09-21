# Kristen Crowe 
# 9/18/24

import pandas as pd 

df = pd.read_csv('data/winemag-data-130k-v2.csv.zip')

# Group-by country to get the count of reviews average points
summary_df = df.groupby('country').agg(
    count=('country', 'size'),  
    points=('points', 'mean')   
).reset_index()

# Round the average points to 1 decimal point
summary_df['points'] = summary_df['points'].round(1)

# Use to check column names in data set
#print(df.columns)

print(summary_df.head())

summary_df.to_csv('data/reviews-per-country.csv', index=False)
