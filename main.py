import wilibs.wilib as wilib
from wilibs.project import project_obj
from wilibs.project.well import well_obj
from wilibs.project.well.dataset import dataset_obj
from wilibs.project.well.dataset.curve import curve_obj
import json




#login
client = wilib.login("hoang", "1")
client.resamplingCurve(client.getCurveById(1132), client.getCurveById(1137))
