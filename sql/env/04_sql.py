import sqlite3
c = sqlite3.connect("mf_prev_prod_sids")
cu = c.cursor()
cu.execute("""CREATE TABLE mf_prod_sids
    (name TEXT, SID TEXT, Datestamp TEXT)
    """)
c.close()
