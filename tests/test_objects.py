import pytest

from pytest_cases import parametrize, fixture_ref
from pydantic import ValidationError

from gbbox.objects import (
    Point,
    MultiPoint,
    LineString,
    MultiLineString,
    Polygon,
    MultiPolygon,
    GeometryCollection,
)


class TestGeojsonObject:
    @parametrize(
        "geojson_object, geojson",
        [
            (Point, fixture_ref("point")),
            (MultiPoint, fixture_ref("multipoint")),
            (LineString, fixture_ref("linestring")),
            (MultiLineString, fixture_ref("multilinestring")),
            (Polygon, fixture_ref("polygon")),
            (MultiPolygon, fixture_ref("multipolygon")),
            (GeometryCollection, fixture_ref("geometrycollection")),
        ],
    )
    def test_init_invalid_type(self, geojson_object, geojson):
        geojson["type"] = "Invalid"

        with pytest.raises(ValidationError):
            geojson_object(**geojson)

    @parametrize(
        "geojson_object, geojson, geojson_bbox",
        [
            (Point, fixture_ref("point"), fixture_ref("point_bbox")),
            (MultiPoint, fixture_ref("multipoint"), fixture_ref("multipoint_bbox")),
            (LineString, fixture_ref("linestring"), fixture_ref("linestring_bbox")),
            (
                MultiLineString,
                fixture_ref("multilinestring"),
                fixture_ref("multilinestring_bbox"),
            ),
            (Polygon, fixture_ref("polygon"), fixture_ref("polygon_bbox")),
            (
                MultiPolygon,
                fixture_ref("multipolygon"),
                fixture_ref("multipolygon_bbox"),
            ),
            (
                GeometryCollection,
                fixture_ref("geometrycollection"),
                fixture_ref("geometrycollection_bbox"),
            ),
        ],
    )
    def test_min_lon(self, geojson_object, geojson, geojson_bbox):
        object = geojson_object(**geojson)

        assert object.min_lon == geojson_bbox[0]

    @parametrize(
        "geojson_object, geojson, geojson_bbox",
        [
            (Point, fixture_ref("point"), fixture_ref("point_bbox")),
            (MultiPoint, fixture_ref("multipoint"), fixture_ref("multipoint_bbox")),
            (LineString, fixture_ref("linestring"), fixture_ref("linestring_bbox")),
            (
                MultiLineString,
                fixture_ref("multilinestring"),
                fixture_ref("multilinestring_bbox"),
            ),
            (Polygon, fixture_ref("polygon"), fixture_ref("polygon_bbox")),
            (
                MultiPolygon,
                fixture_ref("multipolygon"),
                fixture_ref("multipolygon_bbox"),
            ),
            (
                GeometryCollection,
                fixture_ref("geometrycollection"),
                fixture_ref("geometrycollection_bbox"),
            ),
        ],
    )
    def test_min_lat(self, geojson_object, geojson, geojson_bbox):
        object = geojson_object(**geojson)

        assert object.min_lat == geojson_bbox[1]

    @parametrize(
        "geojson_object, geojson, geojson_bbox",
        [
            (Point, fixture_ref("point"), fixture_ref("point_bbox")),
            (MultiPoint, fixture_ref("multipoint"), fixture_ref("multipoint_bbox")),
            (LineString, fixture_ref("linestring"), fixture_ref("linestring_bbox")),
            (
                MultiLineString,
                fixture_ref("multilinestring"),
                fixture_ref("multilinestring_bbox"),
            ),
            (Polygon, fixture_ref("polygon"), fixture_ref("polygon_bbox")),
            (
                MultiPolygon,
                fixture_ref("multipolygon"),
                fixture_ref("multipolygon_bbox"),
            ),
            (
                GeometryCollection,
                fixture_ref("geometrycollection"),
                fixture_ref("geometrycollection_bbox"),
            ),
        ],
    )
    def test_max_lon(self, geojson_object, geojson, geojson_bbox):
        object = geojson_object(**geojson)

        assert object.max_lon == geojson_bbox[2]

    @parametrize(
        "geojson_object, geojson, geojson_bbox",
        [
            (Point, fixture_ref("point"), fixture_ref("point_bbox")),
            (MultiPoint, fixture_ref("multipoint"), fixture_ref("multipoint_bbox")),
            (LineString, fixture_ref("linestring"), fixture_ref("linestring_bbox")),
            (
                MultiLineString,
                fixture_ref("multilinestring"),
                fixture_ref("multilinestring_bbox"),
            ),
            (Polygon, fixture_ref("polygon"), fixture_ref("polygon_bbox")),
            (
                MultiPolygon,
                fixture_ref("multipolygon"),
                fixture_ref("multipolygon_bbox"),
            ),
            (
                GeometryCollection,
                fixture_ref("geometrycollection"),
                fixture_ref("geometrycollection_bbox"),
            ),
        ],
    )
    def test_max_lat(self, geojson_object, geojson, geojson_bbox):
        object = geojson_object(**geojson)

        assert object.max_lat == geojson_bbox[3]

    @parametrize(
        "geojson_object, geojson, geojson_bbox",
        [
            (Point, fixture_ref("point"), fixture_ref("point_bbox")),
            (MultiPoint, fixture_ref("multipoint"), fixture_ref("multipoint_bbox")),
            (LineString, fixture_ref("linestring"), fixture_ref("linestring_bbox")),
            (
                MultiLineString,
                fixture_ref("multilinestring"),
                fixture_ref("multilinestring_bbox"),
            ),
            (Polygon, fixture_ref("polygon"), fixture_ref("polygon_bbox")),
            (
                MultiPolygon,
                fixture_ref("multipolygon"),
                fixture_ref("multipolygon_bbox"),
            ),
            (
                GeometryCollection,
                fixture_ref("geometrycollection"),
                fixture_ref("geometrycollection_bbox"),
            ),
        ],
    )
    def test_bbox(self, geojson_object, geojson, geojson_bbox):
        object = geojson_object(**geojson)

        bbox = object.bbox()

        assert bbox == geojson_bbox
