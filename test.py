file = open("haffsonpw", "r")
pw = file.read()
from pyArango.connection import *
conn = Connection(arangoURL = "https://arango.research.haffson.org", username="haffson", password=pw)
print(conn.databases)