# -*- coding: utf-8 -*-

import os

class Settings:

    def __init__(self, opts):
        # path to qgis dir
        self.qgis_dir = "/home/stefan/Apps/qgis_master"
        
        # all project files (geopackages and rasterlite and qgs) in the same root project directory. 
        self.project_dir = "/home/stefan/Projekte/map_strassenkarte/"
        
        # directory to save tiles to
        self.target_dir = opts.targetdir
        
        # resolution (dpi) to generate the tiles at
        self.dpi = opts.dpi
        
        # scale of the map
        self.scale = opts.scale
        
        # color or black/white map
        self.colortype = opts.colortype
        
        # don't clip the output to a specific geometry
        self.clip = opts.clip
                
        # only generate specific tile
        self.restrict_tile = opts.restrict_tile
        
        # overlap in x an y direction
        self.overlap = opts.overlap

        # generate antialiased maps
        self.antialiasing = opts.antialiasing 
        
        
    def get_logfile_path(self):
        return os.path.join(self.target_dir, "strassenkarte" + str(self.scale) + str(self.colortype) + ".log") 


