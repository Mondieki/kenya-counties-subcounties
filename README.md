# List of counties in Kenya

This .JSON file shows the list of counties in Kenya, their codes and respective sub counties.

### The .json structure — key and value pairs
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

### Using Ionic/Angular

If you are using TypeScript, here's a service to retrieve the counties.
```
import { Http } from '@angular/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';

@Injectable()
export class CountiesProvider {

  constructor(public http: Http) {}

  public getJSON(): Observable<any> {
    return this.http.get('absolute/path/of/counties.json')
        .map(res => res.json());
  }

}
```