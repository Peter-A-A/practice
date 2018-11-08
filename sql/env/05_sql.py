import sqlite3
c = sqlite3.connect("mf_prev_prod_sids")
cu = c.cursor()
for row in cu.execute("SELECT * FROM mf_prod_sids"):
    print(row)
