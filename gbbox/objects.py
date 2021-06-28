from typing import Iterable, Union, List, Literal
from functools import cached_property

from pydantic import BaseModel, conlist

from gbbox.constants import Position, GeometryType


class GeoJSON(BaseModel):
    type: GeometryType

    class Config:
        keep_untouched = (cached_property,)

    def __init__(self, geojson):
        super().__init__(**geojson)

    @cached_property
    def min_lon(self) -> float:
        return min(self.flattened_coords[::2])

    @cached_property
    def min_lat(self) -> float:
        return min(self.flattened_coords[1::2])

    @cached_property
    def max_lon(self) -> float:
        return max(self.flattened_coords[::2])

    @cached_property
    def max_lat(self) -> float:
        return max(self.flattened_coords[1::2])

    @cached_property
    def flattened_coords(self) -> List[float]:
        return list(self._chain_coords(self.coordinates))

    def bbox(self) -> List[float]:
        return [self.min_lon, self.min_lat, self.max_lon, self.max_lat]

    def _chain_coords(self, sequence) -> Iterable[float]:
        for val in sequence:
            if isinstance(val, Iterable):
                for subval in self._chain_coords(val):
                    yield subval
            else:
                yield val


class Point(GeoJSON):
    type: Literal[GeometryType.POINT.value]
    coordinates: Position


class MultiPoint(GeoJSON):
    type: Literal[GeometryType.MULTIPOINT.value]
    coordinates: conlist(Position, min_items=2)


class LineString(GeoJSON):
    type: Literal[GeometryType.LINESTRING.value]
    coordinates: conlist(Position, min_items=2)


class MultiLineString(GeoJSON):
    type: Literal[GeometryType.MULTILINESTRING.value]
    coordinates: conlist(conlist(Position, min_items=2), min_items=2)


class Polygon(GeoJSON):
    type: Literal[GeometryType.POLYGON.value]
    coordinates: conlist(conlist(Position, min_items=4))


class MultiPolygon(GeoJSON):
    type: Literal[GeometryType.MULTIPOLYGON.value]
    coordinates: conlist(conlist(conlist(Position, min_items=4)), min_items=2)


class GeometryCollection(GeoJSON):
    type: Literal[GeometryType.GEOMETRYCOLLECTION.value]
    geometries: List[
        Union[Point, MultiPoint, LineString, MultiLineString, Polygon, MultiPolygon]
    ]
