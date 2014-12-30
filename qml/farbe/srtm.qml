<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="2.7.0-Master" minimumScale="50000" maximumScale="1e+08" hasScaleBasedVisibilityFlag="1">
  <pipe>
    <rasterrenderer gradient="BlackToWhite" opacity="1" alphaBand="-1" type="singlebandgray" grayBand="1">
      <rasterTransparency/>
      <contrastEnhancement>
        <minValue>33</minValue>
        <maxValue>255</maxValue>
        <algorithm>StretchToMinimumMaximum</algorithm>
      </contrastEnhancement>
    </rasterrenderer>
    <brightnesscontrast brightness="30" contrast="0"/>
    <huesaturation colorizeGreen="128" colorizeOn="0" colorizeRed="255" colorizeBlue="128" grayscaleMode="0" saturation="0" colorizeStrength="100"/>
    <rasterresampler maxOversampling="2" zoomedOutResampler="bilinear" zoomedInResampler="bilinear"/>
  </pipe>
  <blendMode>6</blendMode>
</qgis>
