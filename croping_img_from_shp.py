import os
import argparse
import fiona

progfiles = os.listdir("C:\\Program Files")
qgis = "\"C:\\Program Files\\"+[s for s in progfiles if "QGIS" in s][0]+"\\OSGeo4W.bat\"" # Using OSGeo Shell form QGIS

parser = argparse.ArgumentParser()
parser.add_argument("--img", help="path of input positive images")
parser.add_argument("--shp", help="path of output in shapefile")
parser.add_argument("--out", help="directory path of cropped output images")
arg = parser.parse_args()

img = arg.img
shp = arg.shp
out = arg.out

fs = fiona.open(shp) # open .shp file with fiona
b=1
for a in fs:
    print(a)
    imgout = out+"\\"+str(b)+".tif"
    coord = a['geometry']['coordinates']
    x1, y1 = coord[0][3]
    x2, y2 = coord[0][1]
    if(x1>x2): ulx=x2; lrx=x1
    else: ulx=x1; lrx=x2
    if(y1>y2): uly=y1; lry=y2
    else: uly=y2; lry=y1
    cmd = qgis+" gdal_translate -of GTiff -projwin "+str(ulx)+" "+str(uly)+" "+str(lrx)+" "+str(lry)+" "+img+" "+imgout
    print(cmd)
    os.system(cmd)
    b+=1
