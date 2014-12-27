from argparse import ArgumentParser


# -*- coding: utf-8 -*-

class Options:

    def __init__(self):
        self._init_parser()

    def _init_parser(self):
        usage = 'bin/project'
        self.parser = ArgumentParser(usage=usage)
        self.parser.add_argument('-x',
                                '--example',
#                                 required=True, 
                                default='example-value',
                                dest='example',
                                help='An example option')

        self.parser.add_argument('-t',
                                '--targetdir',
                                action = 'store',
                                type = str, 
                                default ='/tmp/',
                                dest ='targetdir',
                                help = 'Directory to move the finished tiles to.')

        self.parser.add_argument('-r',
                                '--dpi',
                                action = 'store',
                                type = int, 
                                default = 635, 
                                dest ='dpi',
                                help = 'Resolution (dpi) to generate the tiles at. Default: 635.')

        self.parser.add_argument('-s',
                                '--scale',
                                action = 'store',
                                type = int, 
                                default = 25000,
                                dest ='scale',
                                help = 'Scale of the map. Default: 25000 (for 1:25000).')

        self.parser.add_argument('-c',
                                '--colortype',
                                action = 'store',
                                type = str, 
                                default = 'f',
                                dest ='colortype',
                                choices = ['sw', 'f'],
                                help = 'Color (f) or black/white (sw) map. Default: f.')

        self.parser.add_argument('--noclip',
                                action = 'store_false',
                                default = True,
                                dest ='clip',
                                help = "Don't clip the output to a geometry which is specified in the script settings.")

        self.parser.add_argument('--tile',
                                action = 'store',
                                type = str, 
                                default = "",
                                dest ='restrict_tile',
                                help = 'Only create the tile with the specified name, even if there are more tiles in the tile index than just this one. This tile must be listed in the tile index file.')

        self.parser.add_argument('-o',
                                '--overlap',
                                action = 'store',
                                type = str, 
                                default = '100.0 50.0',
                                dest ='overlap',
                                help = "Overlap (meters) in x and y direction to use for improved creation of the label layer (e.g. '0 0'). Default: '100.0 50.0'.")

        self.parser.add_argument('--antialiasing',
                                action = 'store_true',
                                default = False,
                                dest ='antialiasing',
                                help = "Generate antialiased maps.")


    def parse(self, args=None):
        return self.parser.parse_args(args)
