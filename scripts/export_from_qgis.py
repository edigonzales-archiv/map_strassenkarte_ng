from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
import qgis.utils



tileindex = "/home/stefan/Projekte/map_strassenkarte_ng/data/tileindex/dtm_solo_01.shp"
dpi = 508
scale = 10000
lst = []

root = QgsProject.instance().layerTreeRoot()

layers = qgis.utils.iface.legendInterface().layers()
for layer in layers:
    node = root.findLayer(layer.id())
    if node.isVisible():
        lst.append(layer.id());
    
    
print lst


vlayer = QgsVectorLayer(tileindex, "tileindex", "ogr")
iter = vlayer.getFeatures()
for feature in iter:
    geom = feature.geometry()
    p1 = geom.vertexAt(0)
    p2 = geom.vertexAt(2)
    rect = QgsRectangle(p1,  p2) # wird normalisiert
    
    dx = rect.width()
    dy = rect.height()

    width = (dx/scale) / 0.0254 * dpi
    height = (dy/scale) / 0.0254 * dpi
    print height

    filename = "strassenkarte_ng_"+str(scale)+"_"+str(int(rect.xMinimum()))+"_"+str(int(rect.yMaximum()))
    print filename    
    
    # Rasterfile exportieren
#    img = QImage(QSize(width,  height), QImage.Format_RGB32)
#    img = QImage(QSize(width,  height), QImage.Format_ARGB32)  
    img = QImage(QSize(width, height), QImage.Format_ARGB32_Premultiplied)
    img.setDotsPerMeterX(dpi / 25.4 * 1000)
    img.setDotsPerMeterY(dpi / 25.4 * 1000)
    
    color = QColor(255,255,255)
    img.fill(color.rgb())
    p = QPainter()
    p.begin(img)
    p.setRenderHint(QPainter.Antialiasing)
    render = QgsMapRenderer()
    render.setLabelingEngine(QgsPalLabeling())
    render.setLayerSet(lst)
    render.setExtent(rect)
    render.setOutputSize(img.size(), dpi)
    render.render(p)
    p.end()
    
    img.save("/tmp/"+filename+".png","png")    

#    imgwriter = QImageWriter("/tmp/"+filename+".tif",  "tiff")
#    imgwriter.setCompression(1)
#    imgwriter.write(img)
    
    # Worldfile speichern
    res = dx/width
    with open("/tmp/"+filename+".pngw", 'w') as outfile:
        outfile.write(str(res))
        outfile.write("\n")
        outfile.write("0.0")
        outfile.write("\n")
        outfile.write("0.0")
        outfile.write("\n")
        outfile.write(str(-1*res))
        outfile.write("\n")
        outfile.write(str(rect.xMinimum()+0.5*res))
        outfile.write("\n")
        outfile.write(str(rect.yMaximum()-0.5*res))
        outfile.close()