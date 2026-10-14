import sys
import osmium


class StopCounter(osmium.SimpleHandler):
    def __init__(self):
        super().__init__()
        self.total = 0
        self.tagged = {"wheelchair": 0, "tactile_paving": 0, "shelter": 0, "bench": 0, "name": 0}

    def node(self, n):
        if n.tags.get("highway") != "bus_stop":
            return
        self.total += 1
        for key in self.tagged:
            if key in n.tags:
                self.tagged[key] += 1


handler = StopCounter()
handler.apply_file(sys.argv[1])

print(f"Bus stops: {handler.total}")
for key, count in handler.tagged.items():
    print(f"  with {key:15}: {count:4} ({100 * count / handler.total:.1f}%)")
