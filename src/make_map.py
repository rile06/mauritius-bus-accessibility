import csv
import sys

import folium

COLORS = {"": "#888888", "no": "#d62728", "limited": "#ff7f0e", "yes": "#2ca02c"}

with open(sys.argv[1], encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

m = folium.Map(location=[-20.28, 57.55], zoom_start=10)

for r in rows:
    status = r["wheelchair"]
    popup = (
        f"{r['name'] or '(no name)'}<br>"
        f"OSM id: {r['osm_id']}<br>"
        f"wheelchair: {status or 'unknown'}<br>"
        f"shelter: {r['shelter'] or '?'}<br>"
        f"bench: {r['bench'] or '?'}"
    )
    folium.CircleMarker(
        [float(r["lat"]), float(r["lon"])],
        radius=7 if status else 4,
        color=COLORS.get(status, COLORS[""]),
        fill=True,
        fill_opacity=0.7,
        popup=folium.Popup(popup, max_width=250),
    ).add_to(m)

m.save(sys.argv[2])
print(f"Mapped {len(rows)} stops to {sys.argv[2]}")
