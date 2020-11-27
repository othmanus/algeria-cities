# algeria-cities

This repository contains the list of all the administrative provinces and cities in Algeria.

The data is up-to-date according to the [official source](https://www.interieur.gov.dz/index.php/fr/collectivit%C3%A9s-territoriales/rechercher-une-collectivite-locale.html) of the Algerian state.

## Languages

The list is available in two languages:
 
- Arabic
- French

## Data

Each file contains the following data:

- Wilaya
    - `code`: is the wilaya ID, between 1 and 48
    - `name`: in latin characters in French language
    - `name_ar`: in Arabic characters in Arabic language
- Daira
    - `code`: is the official administrative code for the daira, prefixed by the wilaya's code
    - `name`: in latin characters in French language
    - `name_ar`: in Arabic characters in Arabic language
- Commune
    - `code`: is the official administrative code for the city. **IMPORTANT:** this is NOT the postal code.
    - `name`: in latin characters in French language
    - `name_ar`: in Arabic characters in Arabic language

## Format

The list is available in different formats:

- CSV comma separated
- JSON 
- MySQL schema
- PHP
- XML
- XLSX aka. Microsoft Excel
- Dart and Flutter

## Contribution

To contribute with a specific format to the repository, please open a pull request. 

Desired formats:

- Java array
- Swift array

Desired data:

- List of the postal codes per city: according to the [official Algerian Post](https://www.poste.dz/customer/bureaux_postaux), each city can have one or many post offices, and each post office has a postal code.
- Latitude and Longitude of each city
