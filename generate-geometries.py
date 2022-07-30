# To get coordinates of a county
# Iterate through all .JSON files in "counties" folder
# Get file name of the .JSON file
# Get centroid.coordinates
# Key value pair of { "center": centroid.coordinates }
# Parse through similar file name "geojson" folder
# get geometries[0] prop

# create new object with code.json filename
# save file in coordinates folder

import os
import json

for filename in os.listdir('counties'):
    f1 = open('counties/{x}'.format(x = filename))
    osm = json.load(f1)
    centre = osm['centroid']['coordinates']

    f2 = open('geojson/{x}'.format(x = filename))
    geo = json.load(f2)
    coordinates = geo['geometries'][0]['coordinates']

    county = {
        "center": centre,
        "geometries": {
            "type": "MultiPolygon",
            "coordinates": coordinates,
        }
        
    }

    # Serializing json
    json_object = json.dumps(county, indent=4)
    
    # Writing to sample.json
    with open("coordinates/{x}".format(x = filename), "w") as outfile:
        outfile.write(json_object)