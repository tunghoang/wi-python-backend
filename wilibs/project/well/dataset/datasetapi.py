from ....api_url import ROOT_API
from ....common import *
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def getDatasetInfo(token, datasetId):
    r = getDatasetInfo_RAW(token, datasetId)
    return verifyAndReturn(r)


def editDatasetInfo(token, datasetId, **data):
    payload = data
    if "name" in data:
        payload['datasetKey'] = data['name']
        payload['datasetLabel'] = data['name']
    payload['idDataset'] = datasetId
    r = editDatasetInfo_RAW(token, payload)
    return verifyAndReturn(r)


def deleteDataset(token, datasetId):
    r = deleteDataset_RAW(token, datasetId)
    return verifyAndReturn(r)


def createDataSet(token, wellId, **data):
    payload = {
        'idWell': wellId,
    }
    if 'name' in data:
        payload['name'] = data['name']
        payload['datasetKey'] = data['name']
        payload['datasetLabel'] = data['name']
    else:
        return False, 'name is required'
    if 'datasetKey' in data:
        payload['datasetKey'] = data['datasetKey']
    if 'datasetLabel' in data:
        payload['datasetLabel'] = data['datasetLabel']
    if 'bottom' in data:
        payload['bottom'] = data['bottom']
    else:
        return False, 'bottom is required'
    if 'top' in data:
        payload['top'] = data['top']
    else:
        return False, 'top is required'
    if 'step' in data:
        payload['step'] = data['step']
    else:
        return False, 'step is required'
    if 'unit' in data:
        payload['unit'] = data['unit']
    else:
        return False, 'unit is required'
    r = createDataSet_RAW(token, payload)
    return verifyAndReturn(r)


# RAW:

def getDatasetInfo_RAW(token, datasetId):
    url = genUrlWithWiId(ROOT_API + '/project/well/dataset/info', {'idDataset': datasetId}, token)
    r = requests.post(url, json={'idDataset': datasetId}, headers=tokenHeader(token), verify=False)
    return r.json()


def editDatasetInfo_RAW(token, payload):
    url = genUrlWithWiId(ROOT_API + '/project/well/dataset/edit', payload, token)
    r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()


def createDataSet_RAW(token, payload):
    url = genUrlWithWiId(ROOT_API + '/project/well/dataset/new', payload, token)
    r = requests.post(url, json=payload, headers=tokenHeader(token), verify=False)
    return r.json()


def deleteDataset_RAW(token, datasetId):
    url = genUrlWithWiId(ROOT_API + '/project/well/dataset/delete', {'idDataset': datasetId}, token)
    r = requests.delete(url, json={'idDataset': datasetId}, headers=tokenHeader(token), verify=False)
    return r.json()
