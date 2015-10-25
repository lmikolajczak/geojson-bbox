#!/usr/bin/python
# -*- coding: utf-8 -*-

#Imports
import numpy as np

#Function
def geojson_bbox(geojson, extend=True):
    if geojson['type'] == 'FeatureCollection':
    	bbox = []
        for f in geojson['features']:
            if f['geometry']['type'] == 'MultiPolygon':
    	        a = np.array(f['geometry']['coordinates'])
    	        for _ in range(2):
    	            a = np.concatenate(a)
    	    elif f['geometry']['type'] == 'MultiLineString':
    	    	a = np.array(f['geometry']['coordinates'])
    	    	a = np.concatenate(a)
    	    elif f['geometry']['type'] == 'Point':
    	    	a = np.array([f['geometry']['coordinates']])
    	    else:
                a = np.array(f['geometry']['coordinates']).squeeze()
            a = np.array([a[:,0].min(), a[:,1].min(), a[:,0].max(), a[:,1].max()]).tolist()
            bbox.append(a)
        if extend:
            print 'Extended bbox for all features in collection:'
            rows = len(bbox)*2
            a = np.array(bbox).reshape(rows,2)
            bbox = np.array([a[:,0].min(), a[:,1].min(), a[:,0].max(), a[:,1].max()]).tolist()
        else:
            print 'Bbox for every feature in collection:'
    else:
    	print 'Bbox for feature:'
        try:
    	    geo_type = geojson['geometry']['type']
    	    coords = geojson['geometry']['coordinates']
    	except:
    	    geo_type = geojson['type']
    	    coords = geojson['coordinates']
    	if geo_type == 'MultiPolygon':
    	    a = np.array(coords)
    	    for _ in range(2):
    	        a = np.concatenate(a)
    	elif geo_type == 'MultiLineString':
    	    	a = np.array(coords)
    	    	a = np.concatenate(a)
    	elif geo_type == 'Point':
    	    a = np.array([coords])
    	else:	
    	    a = np.array(coords).squeeze()
    	bbox = np.array([a[:,0].min(), a[:,1].min(), a[:,0].max(), a[:,1].max()]).tolist()
    return bbox

#Sample data sets
single_feature = {}

#Execute function
if __name__ == "__main__":
    print geojson_bbox(single_feature)
