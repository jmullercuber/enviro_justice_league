import pygeohash


def distance_for_geohashes(geohash_1: str, geohash_2: str):
    return pygeohash.geohash_haversine_distance(geohash_1, geohash_2)
