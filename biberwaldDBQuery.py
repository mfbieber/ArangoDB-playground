from pyArango.connection import *

import requests

requests.packages.urllib3.disable_warnings()

file = open("haffsonpw", "r")
pw = file.read()

conn = Connection(arangoURL="https://arango.research.haffson.org", username="haffson", password=pw)
db = conn["haffson"]

friendsQuery = """
LET animalName = @animalName
LET animalId = FIRST(
    FOR animal IN `Animals`
        FILTER animal.name == animalName
        RETURN animal._id
)
LET directFriends = (FOR liked IN OUTBOUND animalId `Likes`
    FILTER IS_SAME_COLLECTION(`Animals`, liked)
    RETURN liked)
LET indirectFriends = (FOR liked IN OUTBOUND animalId `Likes`
    FILTER IS_SAME_COLLECTION(`Cults`, liked)
        FOR member IN INBOUND liked `Memberships`
        RETURN member)
LET allFriends = UNION_DISTINCT(directFriends, indirectFriends)
RETURN allFriends
"""

bindVars = {"animalName": "Fuchs"}
friends = db.AQLQuery(friendsQuery, rawResults=False, bindVars=bindVars)
print(friends)