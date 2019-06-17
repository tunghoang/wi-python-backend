from .markerset_api import *
from .marker.marker_api import *
from .marker.marker_obj import Marker


class MarkerSets:
    def __init__(self, token, markersetsInfo):
        self.token = token
        self.markersetsInfo = {
            'idWell': markersetsInfo['idWell'],
            'idMarkerSet': markersetsInfo['idMarkerSet'],
            'name': markersetsInfo['name']
        }
        self.markersetId = self.markersetsInfo['idMarkerSet']

    def __repr__(self):
        obj = dict(self.markersetsInfo)
        return str(obj)

    def __str__(self):
        return self.__repr__()
    
    
    def deleteMarkerSets(self):
        check, content = deleteMarkerSets(self.token, self.markersetId)
        if check:
            return True
        else:
            print(content)
        return False

    def createMarker(self, MarkerTemplateId):
        check, content = createMarker(self.token, self.markersetId, MarkerTemplateId)
        if check:
            return Marker(self.token, content)
        else:
            print(content)
        return None
    
    def getListMarker(self):
        check, list = getListMarker(self.token, self.markersetId)
        if check is False and list is None:
            return []
        listObj = []
        for i in list:
            listObj.append(Marker(self.token, i))
        return listObj
    