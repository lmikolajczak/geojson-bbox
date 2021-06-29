from typing import Iterable, Union, List, Literal
from functools import cached_property

from pydantic import BaseModel, conlist

from gbbox.constants import Position, GeometryType


class GeoJSON(BaseModel):
    """Base class that represents a GeoJSON object.

    GeoJSON objects are implemented according to RFC 7946 specification:
    https://datatracker.ietf.org/doc/html/rfc7946

    Attributes:
        type: GeoJSON object type
        min_lon: Decimal number between -180.0 and 180.0 (bbox left)
        min_lat: Decimal number between -90.0 and 90.0 (bbox bottom)
        max_lon: Decimal number between -180.0 and 180.0 (bbox right)
        max_lat: Decimal number between -90.0 and 90.0 (bbox top)
    """

    type: GeometryType

    class Config:
        """Configures pydantic's behaviour"""

        keep_untouched = (cached_property,)

    @cached_property
    def min_lon(self) -> float:
        return min(self._flattened_coords[::2])

    @cached_property
    def min_lat(self) -> float:
        return min(self._flattened_coords[1::2])

    @cached_property
    def max_lon(self) -> float:
        return max(self._flattened_coords[::2])

    @cached_property
    def max_lat(self) -> float:
        return max(self._flattened_coords[1::2])

    def bbox(self) -> List[float]:
        return [self.min_lon, self.min_lat, self.max_lon, self.max_lat]

    @cached_property
    def _flattened_coords(self) -> List[float]:
        return list(self._chain_coords(self.coordinates))

    def _chain_coords(self, sequence: Iterable) -> float:
        """Generates flatten version of nested iterables.

        This method (generator) works in a recursive fashion
        and flattens Iterable until it is "exhausted".

        Args:
            sequence: Any object that is an Iterable. It can
              be nested structure.

        Returns:
            Float object
            within passed Iterable. For example:

            [[1.0, 2.0], [3.0, 4.0]] will yield following values:

            1.0, 2.0, 3.0, 4.0
        """
        for val in sequence:
            if isinstance(val, Iterable):
                for subval in self._chain_coords(val):
                    yield subval
            else:
                yield val


class Point(GeoJSON):
    """Point GeoJSON object (RFC 7946)"""

    type: Literal[GeometryType.POINT.value]
    coordinates: Position


class MultiPoint(GeoJSON):
    """MultiPoint GeoJSON object (RFC 7946)"""

    type: Literal[GeometryType.MULTIPOINT.value]
    coordinates: conlist(Position, min_items=2)


class LineString(GeoJSON):
    """LineString GeoJSON object (RFC 7946)"""

    type: Literal[GeometryType.LINESTRING.value]
    coordinates: conlist(Position, min_items=2)


class MultiLineString(GeoJSON):
    """MultiLineString GeoJSON object (RFC 7946)"""

    type: Literal[GeometryType.MULTILINESTRING.value]
    coordinates: conlist(conlist(Position, min_items=2), min_items=2)


class Polygon(GeoJSON):
    """Polygon GeoJSON object (RFC 7946)"""

    type: Literal[GeometryType.POLYGON.value]
    coordinates: conlist(conlist(Position, min_items=4))


class MultiPolygon(GeoJSON):
    """MultiPolygon GeoJSON object (RFC 7946)"""

    type: Literal[GeometryType.MULTIPOLYGON.value]
    coordinates: conlist(conlist(conlist(Position, min_items=4)), min_items=2)


class GeometryCollection(GeoJSON):
    """GeometryCollection GeoJSON object (RFC 7946)"""

    type: Literal[GeometryType.GEOMETRYCOLLECTION.value]
    geometries: List[
        Union[Point, MultiPoint, LineString, MultiLineString, Polygon, MultiPolygon]
    ]

    @cached_property
    def _flattened_coords(self) -> List[float]:
        coordinates = []
        for object in self.geometries:
            coordinates.append(object.coordinates)

        return list(self._chain_coords(coordinates))
