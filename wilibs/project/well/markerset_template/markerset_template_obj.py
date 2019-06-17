from .markerset_template_api import *
from .marker_template.marker_template_api import createMarkerTemplate
from .marker_template.marker__template_obj import MarkerTemplate
from .markerset.markerset_api import createMarkerSets
from .markerset.markerset_obj import MarkerSets


class MarkerSetTemplate:
    def __init__(self, token, MarkerSetTemplateInfo):
        self.token = token
        self.MarkerSetTempateInfo = {
            'idProject': MarkerSetTemplateInfo['idProject'],
            'idMarkerSetTemplate': MarkerSetTemplateInfo['idMarkerSetTemplate'],
            'name': MarkerSetTemplateInfo['name']
        }
        self.markerSetTemplateId = MarkerSetTemplateInfo['idMarkerSetTemplate']
   
    def __repr__(self):
        obj = dict(self.MarkerSetTemplateInfo)
        return str(obj)

    def __str__(self):
        return self.__repr__()  

    def deleteMarkerSetTemplate(self):
        check, content = deleteMarkerSetTemplate(self.token, self.markerSetTemplateId)
        if check:
            return None
        return content

    def createMarkerTemplate(self, **data):
        check, content = createMarkerTemplate(self.token, self.markerSetTemplateId, **data)
        if check:
            return MarkerTemplate(self.token, content)
        else:
            return None

    def createMarkerSets(self, wellId, name):
        check, content = createMarkerSets(self.token, wellId, self.markerSetTemplateId, name)
        if check:
            return MarkerSets(self.token, content)
        else:
            return None

