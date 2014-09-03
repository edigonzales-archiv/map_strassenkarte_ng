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
    
    mapRenderer = iface.mapCanvas().mapRenderer()
    c = QgsComposition(mapRenderer)
    c.setPlotStyle(QgsComposition.Print)
    
    dpmm = dpi / 25.4
    
    paperWidth = width / dpmm
    paperHeight = height / dpmm
    
    c.setPaperSize(paperWidth, paperHeight)
    c.setPrintResolution(dpi)

    image = QImage(QSize(width, height), QImage.Format_ARGB32)
    image.setDotsPerMeterX(dpmm * 1000)
    image.setDotsPerMeterY(dpmm * 1000)
    image.fill(0)

    imagePainter = QPainter(image)
    sourceArea = QRectF(0, 0, c.paperWidth(), c.paperHeight())
    targetArea = QRectF(0, 0, width, height)
    
    c.render(imagePainter, targetArea, sourceArea)
    imagePainter.end()
    
    img.save("/tmp/"+filename+".png","png")    
    