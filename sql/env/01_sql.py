import sqlite3
c = sqlite3.connect("mf_prev_prod_sids")
cu = c.cursor()
cu.execute("""CREATE TABLE mf_prod_sids
    (model_name TEXT, model_sid TEXT, submission_date TEXT)
    """)

c.close()
