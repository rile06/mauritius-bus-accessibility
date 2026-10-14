# Mauritius Bus Stop Accessibility

An open dataset and data pipeline mapping how accessible Mauritius's bus stops are for wheelchair users, blind and low-vision riders, and other people with mobility or sensory needs.

**Status: early work in progress.**

## Why

Mauritius has no published GTFS feed for its bus network that I could find, and almost no accessibility information about its stops. If you can't tell whether a stop has a step-free boarding area, a shelter, or tactile paving, you can't plan a trip around it.

## First finding

Using the OpenStreetMap extract for Mauritius (Geofabrik, 2026-10-13):

| | Stops | Share |
|---|---|---|
| Bus stops (`highway=bus_stop` nodes) | 953 | |
| With a `wheelchair` tag | 4 | 0.4% |
| With a `tactile_paving` tag | 8 | 0.8% |
| With a `shelter` tag | 194 | 20.4% |
| With a `bench` tag | 140 | 14.7% |
| With a `name` | 144 | 15.1% |

Only 4 of 953 stops have any wheelchair information, and none are tagged as fully accessible. Closing that gap is the point of this project.

Caveat: this counts stops mapped as single points. Stops mapped as lines or areas are not included yet.

## Run it

```
python3 -m venv .venv
source .venv/bin/activate
pip install osmium
# download mauritius-latest.osm.pbf from https://download.geofabrik.de/africa/mauritius.html
# into data/raw/, then:
python src/osm_coverage.py data/raw/<filename>.osm.pbf
```

## Roadmap

- [x] Measure accessibility coverage in OpenStreetMap
- [ ] Structured pipeline (raw, cleaned, published layers) with data quality checks
- [ ] Field survey schema and a pilot survey on one bus corridor
- [ ] GTFS-style export and GeoJSON
- [ ] Small API or map for step-free trip planning
- [ ] Contribute surveyed data back to OpenStreetMap

## Data and license

Map data is © OpenStreetMap contributors, available under the [ODbL](https://www.openstreetmap.org/copyright). Code is MIT licensed.
