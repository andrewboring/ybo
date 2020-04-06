#!/usr/bin/env python
# coding: utf-8


import sys
import os
import requests
# use urllib.parse for Python 3
#import urllib.parse
# use urllib for Python 2
import urllib
import xbmcgui
import xbmcplugin


source_url = 'https://storage.api.eriscape.com/v1/AUTH_andrew/kodi/'
r = requests.get(source_url)
items = r.text

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'movies')

#for item in items.splitlines():
#    name = os.path.splitext(item)[0]
#    link = source_url + urllib.parse.quote(item)
#    print("Movie: " + name)
#    print("Link: " + link)

for item in items.splitlines():
    link = source_url + urllib.quote(item)
    name = os.path.splitext(item)[0]
    li = xbmcgui.ListItem(name, iconImage='DefaultVideo.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=link, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)
