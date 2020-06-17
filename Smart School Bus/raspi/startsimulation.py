import json
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

with open('location simulation (accident).json') as file:
    locations = json.load(file)

cred = credentials.Certificate('smart-school-bus-8226e-5e6d8cd74627.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

db_ref = db.collection(u'bus').document(u'MH01ABCD')

for location in locations:
    db_ref.set({u'location': {u'latitude': location[0],u'longitude': location[1]}, u'status':location[2]}, merge=True)
    if location[2] == 1:
        break
    time.sleep(1);



