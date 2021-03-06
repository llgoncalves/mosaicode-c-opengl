#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Circle(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opengl"
        self.help = "Not to declare"
        self.label = "Circle"
        self.color = "255:0:0:150"
        self.group = "2D Shapes"
        self.ports = [{"type":"mosaicode_lib_c_opengl.extensions.ports.flow",
                "label":"Flow",
                "conn_type":"Input",
                "name":"flow"},
                {"type":"mosaicode_lib_c_opengl.extensions.ports.flow",
                "label":"Flow",
                "conn_type":"Output",
                "name":"flow"},
                {"type":"mosaicode_lib_c_opengl.extensions.ports.color",
                "label":"Color",
                "conn_type":"Input",
                "name":"color"},
                {"type":"mosaicode_lib_c_opengl.extensions.ports.float",
                "label":"Radius",
                "conn_type":"Input",
                "name":"radius"}
            ]

        self.properties = [{"name": "radius",
                            "label": "Radius",
                            "type": MOSAICODE_FLOAT,
                            "lower": -2.0,
                            "upper": 2.0,
                            "step": 0.01,
                            "page_inc": 0.01,
                            "page_size": 0.01,
                            "value": 0.5,
                            }
                           ]
        self.codes["global"] = """
        float radius_$id$ = $prop[radius]$;
        float * $port[color]$;
        void $port[radius]$(float value){
            radius_$id$ = value;
        }
"""
        self.codes["declaration"] = """
        $port[color]$ = (float*)malloc (3 * sizeof (float));
        $port[color]$[0] = 1.0;
        $port[color]$[1] = 0.5;
        $port[color]$[2] = 0.0;
"""
        self.codes["function"] = """
        void mosaicgraph_draw_elipse(float radius, float * rgb){
            glColor3f(rgb[0],rgb[1],rgb[2]);
            glBegin(GL_POLYGON);
            for (int i=0; i < 360; i++){
                    float degInRad = i*3.14159/180;
                    glVertex2f(cos(degInRad)*(radius),sin(degInRad)*(radius));
                }
            glEnd();
        }
"""
        self.codes["call"] = """
        mosaicgraph_draw_elipse(radius_$id$,$port[color]$);
"""