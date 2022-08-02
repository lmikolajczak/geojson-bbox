## 📐 geojson-bbox

Simple Python module for calculating bounding box (bbox) from given GeoJSON object.

Currently following GeoJSON objects are supported ([RFC 7946](https://datatracker.ietf.org/doc/html/rfc7946)):

1. [Point](https://datatracker.ietf.org/doc/html/rfc7946#section-3.1.2)
2. [MultiPoint](https://datatracker.ietf.org/doc/html/rfc7946#section-3.1.3)
3. [LineString](https://datatracker.ietf.org/doc/html/rfc7946#section-3.1.4)
4. [MultiLineString](https://datatracker.ietf.org/doc/html/rfc7946#section-3.1.5)
5. [Polygon](https://datatracker.ietf.org/doc/html/rfc7946#section-3.1.6)
6. [MultiPolygon](https://datatracker.ietf.org/doc/html/rfc7946#section-3.1.7)
7. [GeometryCollection](https://datatracker.ietf.org/doc/html/rfc7946#section-3.1.8)

### Installation

```bash
$ pip install gbbox
```

### Usage

```python
>>> from gbbox import LineString
>>>
>>> linestring_geojson = {
>>>     "type": "LineString",
>>>     "coordinates": [
>>>         [1.0, 2.0],
>>>         [3.0, 4.0]
>>>     ]
>>> }
>>>
>>> linestring = LineString(**linestring_geojson)
>>> linestring_bbox = linestring.bbox()

>>> print(linestring_bbox)
>>> [1.0, 2.0, 3.0, 4.0]

>>> print(linestring.min_lon)
>>> 1.0
```

### Development

```bash
$ docker compose up -d
# Start bash within container and enter it
$ docker exec -it gbbox bash
```

Project will be automatically installed within docker container in an editable mode and
any code changes will be immediately reflected. Keep in mind that if you have python shell
running then you have to restart it.

You can also use `make lint` and `make test` as shortcuts to run linters and tests.

### Contributing

I am open to, and grateful for, any contributions made by the community.
