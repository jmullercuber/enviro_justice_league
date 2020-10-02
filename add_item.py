import datetime
import os
import uuid
from decimal import Decimal

import boto3
import pygeohash

from custom_types import RecordType

DDB_TABLE = os.environ["DDB_TABLE"]

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(DDB_TABLE)


def put_physical_event(
    name: str,
    description: str,
    owner: str,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    website: str,
    address: str,
    latitude: float,
    longitude: float,
):
    geohash = pygeohash.encode(latitude=latitude, longitude=longitude)
    location_data = {
        "address": address,
        "geohash": geohash,
    }
    return put_event(
        name=name,
        description=description,
        owner=owner,
        start_time=start_time,
        end_time=end_time,
        website=website,
        **location_data
    )


def put_event(
    name: str,
    description: str,
    owner: str,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
    website: str,
    **kwargs
):
    record = {
        **kwargs,
        "name": name,
        "description": description,
        "start_time": Decimal(start_time.timestamp()),
        "owner": "system_admin",
        "end_time": Decimal(end_time.timestamp()),
        "website": website,
    }
    return put_record(RecordType.event.value, record)


def put_business(
    name: str,
    description: str,
    website: str,
    address: str,
    latitude: float,
    longitude: float,
):
    geohash = pygeohash.encode(latitude=latitude, longitude=longitude)
    record = {
        "name": name,
        "description": description,
        "website": website,
        "address": address,
        "geohash": geohash,
    }
    return put_record(RecordType.business.value, record)


def put_record(record_type, record):
    uniq_id = str(uuid.uuid4())
    table.put_item(
        Item={**record, "id": uniq_id, "type": record_type,}
    )
    return uniq_id
