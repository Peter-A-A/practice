import csv
import sqlite3

conn = sqlite3.connect("test_model_db")
c = conn.cursor()

csv_table = csv.reader(open("snapshots_test_csv.csv", newline=''))
c.execute("CREATE TABLE model_sid_search(job_id TEXT, model_name TEXT, record_created DATE, model_sid TEXT, folder_id TEXT) ")
c.executemany("INSERT INTO model_sid_search(job_id, model_name, record_created, model_sid, folder_id) values (?,?,?,?,?)", csv_table)
conn.commit()
conn.close()
