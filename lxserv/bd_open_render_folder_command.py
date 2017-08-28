#!/usr/bin/env python
# encoding: utf-8

"""

babylondreams - bd_open_render_folder_command

Release Notes:

V0.1 Initial Release - 2017-04-10

"""
import subprocess

import babylondreams
import lx
import modo

from bd_tools.var import *

__author__ = "Alexander Kucera"
__copyright__ = "Copyright 2017, BabylonDreams - Alexander & Monika Kucera GbR"
__credits__ = ["Alexander Kucera"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Alexander Kucera"
__email__ = "a.kucera@babylondreams.de"
__status__ = "Development"


class CommandClass(babylondreams.CommanderClass):
    _commander_last_used = []

    #def commander_arguments(self):
    #    return [
    #         arg_commander 
    #    ]

    def commander_execute(self, msg, flags):
        subprocess.call(['open', os.path.dirname(modo.Scene().selected[-1:][0].channel('filename').get())])


lx.bless(CommandClass, 'bd.open_render_folder_command')