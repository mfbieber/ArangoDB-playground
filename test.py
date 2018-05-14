from pyArango.connection import *
conn = Connection(arangoURL = "https://arango.research.haffson.org", username="haffson", password="6L]%o{63e(=GA96y%$s4z/Vig976J=.3")
print(conn.databases)