import pytest

from gbbox.constants import GeometryType


@pytest.fixture
def geojson():
    return {"type": GeometryType.POINT.value}


@pytest.fixture
def point():
    return {"type": GeometryType.POINT.value, "coordinates": [1.0, 2.0]}


@pytest.fixture
def point_bbox():
    return [1.0, 2.0, 1.0, 2.0]


@pytest.fixture
def multipoint():
    return {
        "type": GeometryType.MULTIPOINT.value,
        "coordinates": [[1.0, 2.0], [3.0, 4.0]],
    }


@pytest.fixture
def multipoint_bbox():
    return [1.0, 2.0, 3.0, 4.0]


@pytest.fixture
def linestring():
    return {
        "type": GeometryType.LINESTRING.value,
        "coordinates": [[1.0, 2.0], [3.0, 4.0]],
    }


@pytest.fixture
def linestring_bbox():
    return [1.0, 2.0, 3.0, 4.0]


@pytest.fixture
def multilinestring():
    return {
        "type": GeometryType.MULTILINESTRING.value,
        "coordinates": [[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]],
    }


@pytest.fixture
def multilinestring_bbox():
    return [1.0, 2.0, 7.0, 8.0]


@pytest.fixture
def polygon():
    return {
        "type": GeometryType.POLYGON.value,
        "coordinates": [
            [[10.0, 0.0], [11.0, 0.0], [11.0, 10.0], [10.0, 10.0], [10.0, 0.0]]
        ],
    }


@pytest.fixture
def polygon_bbox():
    return [10.0, 0.0, 11.0, 10.0]


@pytest.fixture
def multipolygon():
    return {
        "type": GeometryType.MULTIPOLYGON.value,
        "coordinates": [
            [
                [
                    [180.0, 40.0],
                    [180.0, 50.0],
                    [170.0, 50.0],
                    [170.0, 40.0],
                    [180.0, 40.0],
                ]
            ],
            [
                [
                    [-170.0, 40.0],
                    [-170.0, 50.0],
                    [-180.0, 50.0],
                    [-180.0, 40.0],
                    [-170.0, 40.0],
                ]
            ],
        ],
    }


@pytest.fixture
def multipolygon_bbox():
    return [-180.0, 40.0, 180.0, 50.0]


@pytest.fixture
def geometrycollection():
    return {
        "type": GeometryType.GEOMETRYCOLLECTION.value,
        "geometries": [
            {"type": GeometryType.POINT.value, "coordinates": [100.0, 0.0]},
            {
                "type": GeometryType.LINESTRING.value,
                "coordinates": [[101.0, 0.0], [102.0, 1.0]],
            },
        ],
    }


@pytest.fixture
def geometrycollection_bbox():
    return [100.0, 0.0, 102.0, 1.0]
