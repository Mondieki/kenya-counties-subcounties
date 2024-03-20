# HOW TO RENDER A MAP ON A WEB APP

For rendering multipolygon geometries on a map in a web application, you might consider using [Leaflet](https://leafletjs.com/), a leading open-source JavaScript library for mobile-friendly interactive maps. It supports various geometric types, including multipolygons, and can be easily integrated into web applications.


Here's the strucutre for our geojson file:

```
const geoJSON = {
    "type": "GeometryCollection",
    "geometries": [
        {
            "type": "MultiPolygon",
            "coordinates": [
                [
                    [
                        [
                            35.5234934,
                            0.0131824
                        ],
                        [
                            35.5242972,
                            0.0199184
                        ],
                        [
                            35.5264945,
                            0.03652
                        ]
                    ]
                ]
            ]
        }
    ]
}
```

To render the multipolygon on a map, we can use [Leaflet's `L.geoJSON method`](https://leafletjs.com/reference.html#geojson) can parse GeoJSON objects directly, making it a good fit for handling this kind of data.


