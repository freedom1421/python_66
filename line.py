#!/usr/local/bin/python
# -*- coding: utf-8 -*-

def lineNotify(message):
    payload = {'message': message}
    return _lineNotify(payload)

def notifyFile(filename):
    file = {'imageFile': open(filename, 'rb')}
    payload = {'message': '-'}
    return _lineNotify(payload, file)

def notifyPicture(url):
    payload = {'message': ' ', 'imageThumbnail': url, 'imageFullsize': url}
    return _lineNotify(payload)

def notifySticker(stickerID, stickerPackageID):
    payload = {'message': ' ', 'stickerPackageId': stickerPackageID, 'stickerId': stickerID}
    return _lineNotify(payload)

def _lineNotify(payload, file=None):
    import requests
    url = 'https://notify-api.line.me/api/notify'
    token = 'HD2spNqPgHYPkm4Sngc37JLHVklRW2W0gHyGgOnYYeO'  # EDIT
    headers = {'Authorization': 'Bearer ' + token}
    return requests.post(url, headers=headers, data=payload, files=file)

# notifyFile('./logo.png')
lineNotify('อะไร')
notifySticker(10551378, 6136)
notifyFile("test.jpg")
