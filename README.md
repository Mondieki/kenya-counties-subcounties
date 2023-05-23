# Kenyan Counties, Subcounties, and Polygon Boundaries

This repository hosts a comprehensive .JSON file containing data for all 47 counties in Kenya, including their codes, geoJSON information (polygon coordinates), respective subcounties, and capital cities.

---
### Structure of counties.json

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

### Specific County Data: counties/{county}.json

Each specific county .JSON file contains [OpenStreetMap](https://www.openstreetmap.org/) information corresponding to the respective county.

---

### GeoJSON Data: geojson/{county}.json

Polygon representations are given by coordinates of their vertices, provided as pairs of latitude and longitude using the WGS 84 coordinate system.

---

### Coordinate Data: coordinates/{county}.json

This file includes center coordinates and multipolygon coordinates for each county.

---

### Demonstration

To interact with a demonstration of the data visualized, visit [this demo](https://countieskenya.info).

## License

This project is licensed under the MIT License. For more details, please refer to the [LICENSE](https://github.com/Mondieki/kenya-counties-subcounties.git/blob/master/LICENSE) file.