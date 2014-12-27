# -*- coding: utf-8 -*-
import os
import sys
import logging
import time
import datetime

from lib import Options
from lib import Settings
from lib import Strassenkarte

if __name__ == '__main__':    
    # read the options and arguments from the command line / and some more settings
    options = Options()
    opts = options.parse(sys.argv[1:])    
    my_settings = Settings(opts)
    
    # configure logging
    FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(filename = my_settings.get_logfile_path(), filemode = "w", format = FORMAT, level = logging.DEBUG)
    #logging.getLogger().addHandler(logging.StreamHandler())

    # check if outdir (needed for creating the logfile) exists
    check_dir = my_settings.target_dir
    if not os.path.isdir(check_dir):
        errorMessage = "Error: " + check_dir + " does not exist"
        sys.exit(errorMessage)

    # log some general information
    logging.info("Creating strassenkarte" + str(my_settings.scale) + my_settings.colortype)
    logging.info("Settings: " + str(my_settings.__dict__))
    starttime = datetime.datetime.now()    
    logging.info("Start time is " + str(starttime))

    # generate the map tiles
    logging.info("Generate Strassenkarte...")
    try:
        strassenkarte = Strassenkarte(my_settings)
        strassenkarte.create_map_tiles()
    except Exception, e:
        # better exception handling / create exceptions that fit my needs
        logging.error(e)
        sys.exit(e)
    
        
    overall_duration = datetime.datetime.now() - starttime
    logging.info("Task complete. Overall duration: " + str(overall_duration))
    logging.shutdown()

