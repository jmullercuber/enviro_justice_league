from datetime import datetime

from add_item import put_business, put_event, put_physical_event

put_business(
    name="ZERO market - Stanley",
    description="Zero waste store for the homies in Aurora",
    website="https://www.thezeromarket.com/",
    address="2501 Dallas St, Aurora, CO 80010",
    latitude=39.753216,
    longitude=-104.8769822,
)

put_business(
    name="ZERO market - Edgewater",
    description="Zero waste store for the homies on Denver's west-side",
    website="https://www.thezeromarket.com/",
    address="5505 W 20th Ave STE 150, Edgewater, CO 80214",
    latitude=39.7485998,
    longitude=-105.0571059,
)

put_physical_event(
    name="Cleanup Utah Park",
    description="The fam bout to get their hands dirty ",
    owner="The Squad",
    start_time=datetime(year=2020, month=10, day=31),
    end_time=datetime(year=2020, month=10, day=31),
    website="example.com",
    address="Utah Park",
    latitude=39.6832799,
    longitude=-104.8445059,
)

put_business(
    name="Conscious Living",
    description="Sustainable shopping to the Springs",
    website="https://www.consciouslivingshop.com/",
    address="2616 W Colorado Ave #9, Colorado Springs, CO 80904",
    latitude=38.8486887,
    longitude=-104.8647166,
)

put_business(
    name="JOY FILL",
    description="Eco-friendly living",
    website="https://www.joyfill.co/",
    address="3843 Tennyson St, Denver, CO 80212",
    latitude=39.7702317,
    longitude=-105.0443471,
)

put_physical_event(
    name="PETter for the Environment",
    description="Bring any art materials and scraps from your house to make a home-made Halloween costume for your fur baby! Labra-Thor anyone? 🐩 🦸🏽‍♀️",
    owner="Dumb Friends League",
    start_time=datetime(year=2020, month=10, day=15),
    end_time=datetime(year=2020, month=10, day=15),
    website="example.com",
    address="2080 S Quebec St, Denver, CO 80231",
    latitude=39.6790186,
    longitude=-104.9026181,
)
