from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *



def run_script(iface):
 #tileindex = "/home/stefan/Projekte/map_strassenkarte_ng/data/tileindex/dtm_solo_01.shp"
 tileindex = "/sogis_nas/daten_exchange/tmp_ziegler/dtm_solo_01.shp"
 dpi = 508
 scale = 10000
 lst = []

 layers = iface.legendInterface().layers()
 for layer in layers:
  lst.append(layer.id())   
 print lst

 vlayer = QgsVectorLayer(tileindex, "tileindex", "ogr")
 provider = vlayer.dataProvider()
 feat = QgsFeature()
 allAttrs = provider.attributeIndexes()
 provider.select(allAttrs)
        
 while provider.nextFeature(feat):
  geom = feat.geometry()
  print geom

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
    
  img.save("/sogis_nas/daten_exchange/tmp_ziegler/"+filename+".png","png")   
