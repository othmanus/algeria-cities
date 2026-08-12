# algeria-cities

This repository contains the list of all the administrative provinces and cities in Algeria.

The data is up-to-date according to the official source of the Algerian Interior Ministry, including the 10 new Wilayas.

## Languages

The list is available in:
 
- Arabic language
- ASCII, French language
- Both

## Data

There are:

- 58 Wilayas (Provinces)
- 546 Dairas (Administrations)
- 1541 Communes (City, Municipality)
- 3940 Post Codes

### Format

The list is available in different formats:

- CSV
- JSON 
- SQL
- PHP
- XLSX aka. Microsoft Excel
- Dart
- GeoJSON (wilaya boundaries)

Each format contains 3 versions of the data: in ASCII characters, in Arabic characters, and in both.

Each folder is structured as the following

```text
%format%/%file_name%       -- contains data in both Arabic and ASCII characters
%format%/ar/%file_name%    -- contains data only in Arabic characters
%format%/ascii/%file_name% -- contains data only in ASCII (French) characters
```

### Boundaries

`geojson/algeria_wilayas.geojson` contains the boundary polygon of each of the
58 wilayas as a `FeatureCollection`. It is a single file holding both languages
(no `ar/` and `ascii/` split), since the geometry would be duplicated for a few
bytes of text.

```json
{
  "type": "Feature",
  "properties": {
    "wilaya_code": "16",
    "wilaya_name_ascii": "Alger",
    "wilaya_name": "الجزائر"
  },
  "geometry": { "type": "Polygon", "coordinates": [ ... ] }
}
```

Features are sorted by `wilaya_code`, which joins to every other file in this
repository. Geometry is sourced from [simplemaps.com](https://simplemaps.com) —
check their license before redistributing.

## Contribution

To contribute with a specific format to the repository, please open a pull request. 

Desired formats:

- Java array
- Swift array

Desired data:

- Latitude and Longitude of each city
