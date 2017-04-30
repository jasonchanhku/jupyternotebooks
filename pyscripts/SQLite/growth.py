import pandas as pd
import sqlite3
import math
conn = sqlite3.connect("factbook.db")
facts = pd.read_sql_query("SELECT * FROM facts;", conn)
facts = facts[facts["area_land"] != 0 ]
facts = facts.dropna(axis = 0)

def final_pop(df):
    df["final"] = df["population"]*(math.e**(df["population_growth"]/100*35))
    return df

final = facts.apply(final_pop, axis =1)  

print(final.sort_values("final", ascending = False)["name"].head(10))