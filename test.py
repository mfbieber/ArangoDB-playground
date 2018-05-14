from pyArango.connection import *

file = open("haffsonpw", "r")
pw = file.read()

conn = Connection(arangoURL = "https://arango.research.haffson.org", username="haffson", password=pw)
print(conn.databases)