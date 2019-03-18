#/us/bin/python3

import sys
import plotly
import requests 

class HeatMapper():
    def __init__(self):
        self.username = 'pbaumann'
        self.api_key ='hFuzgtv9aO7maJNVOg38'
        self.fips = None
        self.values = None
        self.binning_endpts = None
        self.title = None
        self.legend_title = None

    def createMap(self, filename):
        # Need to set fips, values, binning endpoints, title, legend title
        if (self.fips && self.values && self.beginning_endpts && self.title &&
                self.lengend_title) != None:

            fig = ff.create_choropleth(fips = getFips(), values = getValues(),
                binning_endpoints=getEndpts(), colorscale='RdBu',
                show_state_date=False, show_hover=True,centroid_marker
                = {'opacity':0}, asp=2.9, title = getTitle(),
                legend_title=getLTitle())
            py.iplot(fig, filename=filename)
            return 0
        else: 
            print ("Missing arguments for new map.")
            return 1
    
    def setFips(self, fips):
        self.fips = fips

    def getFips(self):
        if self.fips:
            return self.fips
        else:
            return None

    def setValues(self, values):
        self.fips = values

    def getValues(self):
        if self.values:
            return self.values
        else:
            return None

    def setEndpts(self, endpts):
        self.beginning_endpts = endpts

    def getEndpts(self):
        if self.binning_endpts:
            return self.binning_endpts
        else:
            return None
    
    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        if self.title:
            return self.title
        else:
            return None

    def setLTitle(self, ltitle):
        self.legend_title = ltitle

    def getLTitle(self):
        if self.getLTitle:
            return self.legend_title
        else:
            return None

