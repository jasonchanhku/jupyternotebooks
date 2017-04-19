from dateutil.parser import parse
import pandas as pd
import read

def extract_hour ():
    df = read.load_data()
    ts = df["submission_time"]
    ts_parsed = ts.apply(parse)
    df["hours"] = ts_parsed.apply(lambda x: x.hour)
    return df["hours"]

if __name__ == "__main__":
    b = extract_hour()
    print(b.value_counts())
    
    
    