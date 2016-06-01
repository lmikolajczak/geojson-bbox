# !/usr/bin/python
# -*- coding: utf-8 -*-

# GeoJSON bbox

class GeoJSON:
    """
    """
    def __init__(self, geojson):
        if geojson['type'] == 'FeatureCollection':
            self.coords = list(self.__flatten([f['geometry']['coordinates']
                           for f in geojson['features']]))
            self.features_count = len(geojson['features'])
        elif geojson['type'] == 'Feature':
            self.coords = list(self.__flatten([
                        geojson['geometry']['coordinates']]))
            self.features_count = 1
        else:
            self.coords = list(self.__flatten([geojson['coordinates']]))
            self.features_count = 1

    def __flatten(self, l):
        for val in l:
            if isinstance(val, list):
                for subval in self.__flatten(val):
                    yield subval
            else:
                yield val

    def bbox(self):
        return [min(self.coords[::2]),min(self.coords[1::2]),
                max(self.coords[::2]),max(self.coords[1::2])]
