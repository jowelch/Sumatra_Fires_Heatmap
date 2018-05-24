import requests, zipfile, io
r = requests.get("https://firms.modaps.eosdis.nasa.gov/active_fire/c6/shapes/zips/MODIS_C6_SouthEast_Asia_24h.zip")
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall()
 #I think this is getting the data from the NASA website
import shapefile
reader = shapefile.Reader("MODIS_C6_SouthEast_Asia_24h.shp")
fields = reader.fields[1:]
field_names=[field[0] for field in fields]
buffer = []
for sr in reader.shapeRecords():
    atr = dict(zip(field_names, sr.record))
    geom = sr.shape.__geo_interface__
    buffer.append(dict(type="Feature", geometry=geom, properties=atr))
import json
# Dictionary1 = dict(type="datetime.date")
# json.dumps(buffer, indent=4, sort_keys=True, default=str)
data = json.dumps({"type": "FeatureCollection", "features": buffer}, indent=2, default=str)
geojson = open("Fires_Data.js", "w")
geojson.write("var Fires = " + data + "\n")
geojson.close()



#I think this converts shapefile to geojson
#It also needs to replace the Fire_Area file so it shows the new information, it also needs to add the variable 'fire' into the file.

