import os

import boto3
from boto3.dynamodb.conditions import Attr
from geo_helpers import distance_for_geohashes

DDB_TABLE = os.environ["DDB_TABLE"]

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(DDB_TABLE)


def get_records(record_type):
    response = table.scan(FilterExpression=Attr("type").eq(record_type))
    return response["Items"]


def search_nearby(geohash, record_type):
    records_w_dist = [
        {
            "payload": b,
            "distance_to_search": distance_for_geohashes(geohash, b["geohash"]),
        }
        for b in get_records(record_type)
    ]
    sorted_records = sorted(records_w_dist, key=lambda a: a["distance_to_search"])
    return sorted_records
