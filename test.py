from pyArango.connection import *
conn = Connection(arangoURL = "https://arango.research.haffson.org", username="haffson", password="")
print(conn.databases)