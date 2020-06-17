import xml.dom.minidom
import json

doc = xml.dom.minidom.parse("Route.xml");

locations_sim = []

for location in doc.getElementsByTagName("trkpt"):
    locations_sim.append([location.getAttribute("lat"),location.getAttribute("lon"), 0])

with open('location simulation (simple).json', 'w') as file:
    json.dump(locations_sim, file)
