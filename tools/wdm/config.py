import os

import wde.config

ROOT_FOLDER = wde.config.ROOT_FOLDER = os.getenv('ROOT_FOLDER', os.path.expanduser('~/.wdm'))
EXECUTABLE = wde.config.EXECUTABLE = 'wdm'

WDE_ROOT_FOLDER = os.getenv('WDE_ROOT_FOLDER', os.path.expanduser('~/.wde'))