# !/usr/bin/python
# -*- coding: utf-8 -*-


class GeoJSON:
    """GeoJSON class which allows to calculate bbox"""
    def __init__(self, geojson):
        if geojson['type'] == 'FeatureCollection':
            self.coords = list(self._flatten([f['geometry']['coordinates']
                           for f in geojson['features']]))
            self.features_count = len(geojson['features'])
        elif geojson['type'] == 'Feature':
            self.coords = list(self._flatten([
                        geojson['geometry']['coordinates']]))
            self.features_count = 1
        else:
            self.coords = list(self._flatten([geojson['coordinates']]))
            self.features_count = 1

    def _flatten(self, l):
        for val in l:
            if isinstance(val, list):
                for subval in self._flatten(val):
                    yield subval
            else:
                yield val

    def bbox(self):
        return [min(self.coords[::2]), min(self.coords[1::2]),
                max(self.coords[::2]), max(self.coords[1::2])]
