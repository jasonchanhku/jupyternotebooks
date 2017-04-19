import read
import pandas as pd


if __name__ == "__main__":
    df = read.load_data()
    domains = df["url"]
    
    # we want to print everything
    for name, row in domains.items():
        print("{0}: {1}".format(name, row))