"""Build geojson/algeria_wilayas.geojson from a simplemaps.com Algeria export.

    python3 geojson/build.py ~/Downloads/dz.json

Joins on the wilaya name, not on simplemaps' DZxx id: they number the 10 new
wilayas in a different order (their DZ49 is El M'Ghair, ours is Timimoun), so
an id join silently mislabels codes 49-58.
"""
import json, os, re, sys, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALIAS = {  # simplemaps spelling -> this repo's spelling
    "bordj bou arrer": "bordj bou arreridj",
    "bordj baji mokhtar": "bordj badji mokhtar",
    "el m ghair": "el meghaier",
    "el menia": "el meniaa",
}


def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
    return ALIAS.get(s, s)


def centroid(geometry):
    xs, ys = [], []

    def walk(c):
        if isinstance(c[0], (int, float)):
            xs.append(c[0])
            ys.append(c[1])
        else:
            for part in c:
                walk(part)

    walk(geometry["coordinates"])
    return sum(xs) / len(xs), sum(ys) / len(ys)


def main(source):
    cities = json.load(open(os.path.join(ROOT, "json/algeria_cities.json")))
    repo = {norm(r["wilaya_name_ascii"]): r for r in cities}
    assert len(repo) == 58, "expected 58 wilayas, got %d" % len(repo)

    features = []
    for f in json.load(open(source))["features"]:
        name = f["properties"]["name"]
        assert norm(name) in repo, "no wilaya matches %r — add it to ALIAS" % name
        r = repo[norm(name)]
        features.append({
            "type": "Feature",
            "properties": {
                "wilaya_code": r["wilaya_code"],
                "wilaya_name_ascii": r["wilaya_name_ascii"],
                "wilaya_name": r["wilaya_name"],
            },
            "geometry": f["geometry"],
        })

    features.sort(key=lambda f: f["properties"]["wilaya_code"])
    codes = [f["properties"]["wilaya_code"] for f in features]
    assert codes == ["%02d" % i for i in range(1, 59)], "codes not 01..58: %s" % codes

    # A bad join puts a polygon on the wrong side of the country; every wilaya
    # centroid must land inside Algeria's bounding box.
    for f in features:
        lon, lat = centroid(f["geometry"])
        assert -9 < lon < 12 and 18 < lat < 38, \
            "%s centroid outside Algeria: %.2f,%.2f" % (f["properties"]["wilaya_code"], lat, lon)

    out = os.path.join(ROOT, "geojson/algeria_wilayas.geojson")
    with open(out, "w") as fh:
        json.dump({"type": "FeatureCollection", "features": features}, fh,
                  ensure_ascii=False, separators=(",", ":"))
    print("wrote %s (%d features)" % (out, len(features)))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(os.path.expanduser(sys.argv[1]))
