#!/usr/bin/python
#-*-coding:utf-8-*-
from keywords import MyCustomLibrary
from version import VERSION 

__version__=VERSION

class ArtisanCustomLibrary(MyCustomLibrary):
    ROBOT_LIBRARY_SCOPE='GLOBAL'    #此句作用是指该库运行的时候会作用在全局。
