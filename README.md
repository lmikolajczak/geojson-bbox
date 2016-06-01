####Simple python module for calculating bounding box (bbox) from given GeoJSON object

**Usage**
```python
geo = GeoJSON(geojson)
bbox = geo.bbox()

print bbox
[min_x,min_y,max_x,max_y]
```
