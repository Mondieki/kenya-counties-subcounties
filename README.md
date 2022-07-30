# List of Kenyan counties, their respective subcounties and their polygon boundaries

This .JSON file shows the list of (47) counties in Kenya, their codes, their geoJSON info(polygon coordinates) and respective subcounties.

---
### The counties.json structure
```
[
    {
        "name": "Bungoma",
        "capital": "Bungoma",
        "code": 39,
        "sub_counties": [
            "Bumula",
            "Kabuchai",
            .
            .
            .
            "Webuye east",
            "Webuye west"
        ]
    },
    
    .
    .
    .

    {
        "name": "Garissa",
        "capital": "Garissa",
        "code": 7,
        "sub_counties": [
            "Daadab",
            "Fafi",
            .
            .
            "Ijara",
            "Lagdera balambala"
        ]
    },

    .
    .
    .

    {
        "name": "Nairobi",
        "capital": "Nairobi City",
        "code": 47,
        "sub_counties": [
            "Dagoretti North Sub County",
            "Dagoretti South Sub County ",
            .
            .
            .
            "Lang'ata Sub County ",
            .
            .
            .
            "Starehe Sub County ",
            "Westlands Sub County "
        ]
    }
]
```

---
### counties/{county}.json

This .JSON file contains the [OSM](https://www.openstreetmap.org/) information for the county.

---

### geojson/{county}.json

Polygons are represented by the coordinates of their vertices. The vertices are represented using WGS 84 latitude and longitude pairs. 

---

### coordinates/{county}.json
Center coordinates and mutlipolyogon coordinates for the county.

---
### See it in action

Play around with [this demo](https://countieskenya.info).