#!/usr/bin/python3

import random
import json
import icons.weather as weather
import icons.base as icons
import logging

class DataSource:
    '''No help for this API.'''
    CHOICES = {}

    @staticmethod
    def define_args(parser):
        pass

    def __init__(self, **args):
        if not hasattr(self,"banner"):
            self.banner = weather.conditions("sun")


class FileDataSource(DataSource):
    @staticmethod
    def define_args(parser):
        parser.add_argument("filename", type=str, help="Sample file name")
        DataSource.define_args(parser)


    def _readFile(self, bytes=-1):
        try:
            return open(self.filename,"r").read(bytes)
        except IOError:
            logging.warn("Couldn't read from file %s" % self.filename)
            return None

    def __init__(self, filename, **args):
        self.filename = filename
        DataSource.__init__(self, **args)

