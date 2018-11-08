import sqlite3
c = sqlite3.connect("mf_prev_prod_sids")
cu = c.cursor()
cu.execute("SELECT * FROM mf_prod_sids")
rows = cu.fetchall()
print(rows)
