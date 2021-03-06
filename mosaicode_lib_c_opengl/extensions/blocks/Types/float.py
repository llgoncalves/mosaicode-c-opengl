#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Float(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Float"
        self.color = "73:13:117:150"
        self.group = "Types"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.float",
                    "label":"Value",
                    "conn_type":"Output",
                    "name":"value"}
            ]
        self.properties = [{"name": "size",
                            "label": "size",
                            "type": MOSAICODE_FLOAT,
                            "lower": -10000000.0,
                            "upper": 10000000.0,
                            "step": 0.01,
                            "value": 0.5,
                            "page_inc": 0.1,
                            "page_size": 0.1,
                            }
                           ]

        self.codes["global"]= """
std::vector<void (*)(float)> $port[value]$;
"""

        self.codes["declaration"] = """
        float value$id$ = $prop[size]$;
"""

        self.codes["execution"] = """
   for(auto n : $port[value]$){
       n(value$id$);
   }

"""
