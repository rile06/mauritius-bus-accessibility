import csv
import sys
from pathlib import Path

import osmium

TAG_COLUMNS = [
    "name", "wheelchair", "tactile_paving", "shelter", "bench",
    "bin", "lit", "covered", "operator", "network",
]


class StopCollector(osmium.SimpleHandler):
    def __init__(self):
        super().__init__()
        self.rows = []

    def node(self, n):
        if n.tags.get("highway") != "bus_stop":
            return
        row = {"osm_id": n.id, "lon": n.location.lon, "lat": n.location.lat}
        for key in TAG_COLUMNS:
            row[key] = n.tags.get(key, "")
        self.rows.append(row)


source, target = sys.argv[1], Path(sys.argv[2])
collector = StopCollector()
collector.apply_file(source)

target.parent.mkdir(parents=True, exist_ok=True)
with open(target, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["osm_id", "lon", "lat"] + TAG_COLUMNS)
    writer.writeheader()
    writer.writerows(collector.rows)

print(f"Wrote {len(collector.rows)} stops to {target}")
