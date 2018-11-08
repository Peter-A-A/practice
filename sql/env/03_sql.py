import sqlite3
c = sqlite3.connect("mf_prev_prod_sids")
cu = c.cursor()
cu.execute("INSERT INTO mf_prod_sids VALUES('20 TEST LANE', \
    'gdf8g7g8', 01/11/2018)")
c.commit()
c.close()
