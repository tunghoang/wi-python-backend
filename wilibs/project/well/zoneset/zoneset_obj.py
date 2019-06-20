from .zoneset_api import *
from .zone.zone_api import *
from .zone.zone_obj import Zone
from .zone.zone_api import *
from ..zoneset_template.zoneset_template_api import *


class ZoneSet:
    def __init__(self, token, ZoneSetInfo):
        self.token = token
        self.ZoneSetInfo = {
            'idWell': ZoneSetInfo['idWell'],
            'idZoneSetTemplate': ZoneSetInfo['idZoneSetTemplate'],
            'idZoneSet': ZoneSetInfo['idZoneSet'],
            'name': ZoneSetInfo['name']
        }
        self.ZoneSetId = ZoneSetInfo['idZoneSet']
        self.name = ZoneSetInfo['name']
   
    def __repr__(self):
        obj = dict(self.ZoneSetInfo)
        return str(obj)

    def __str__(self):
        return self.__repr__()  
    
    def getZoneSetInfo(self):
        check, content = getZoneSetInfo(self.token, self.ZoneSetId)
        if check:
            return content
        else:
            print(content)
        return {}
    
    def getAllZones(self):
        check, list = getZoneSetInfo(self.token, self.ZoneSetId)
        if check is False and list is None:
            return [] 
        listObj = list['zones']
        return listObj
    
    def deleteZoneSet(self):
        check , content = deleteZoneSet(self.token, self.ZoneSetId)
        if check:
            return None
        return content
    
    def delete(self):
        return self.deleteZoneSet()

    def renameZoneSet(self, newZoneSetName):
        zoneset = self.getZoneSetInfo()
        print(zoneset)
        check, content = editZoneSetTemplate(self.token, {'idZoneSetTemplate': zoneset['idZoneSetTemplate'], 'name': newZoneSetName})
        c, co = editZoneSet(self.token, {'idZoneSet': zoneset['idZoneSet'], 'name': newZoneSetName})
        if check and c:
            print("Update zoneset name successfull")
            return True
        else:
            print(content, co)
            return False
        return False