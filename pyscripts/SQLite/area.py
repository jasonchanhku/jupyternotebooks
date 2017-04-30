import pandas as pd
import sqlite3
import math

conn = sqlite3.connect('factbook.db')
total = conn.execute('select sum(area_land) / sum(area_water) from facts where (area_land != "") & (area_water != "");').fetchall()

print(total)