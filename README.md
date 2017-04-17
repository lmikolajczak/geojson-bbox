## 📐 geojson-bbox

Simple Python module for calculating bounding box (bbox) from given GeoJSON object.

### Installation

In cloned repo directory:

```bash
$ python setup.py install
```

### Usage

```python
>>> import gbbox
>>> feature = gbbox.GeoJSON(geojson)
>>> feature_bbox = feature.bbox()

print feature_bbox
[min_x, min_y, max_x, max_y]
```

### TODO

* add new features
* write some tests
