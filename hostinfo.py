#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# hostinfo - Quick print basic information about a hostname
#
# Ansgar Grunseid
# grunseid.com
# grunseid@gmail.com
#
# License: MIT
#

import os
import sys
import json
import socket
import urllib.request, urllib.error, urllib.parse

from furl import furl
from icecream import ic


def lget(l, index, default=None):
    try:
        return l[index]
    except IndexError:
        return default


def lookupHostInfo(url):
    host = url
    if '://' in url:
        host = furl(url).host

    ipv4 = host
    if len(host.split('.')) != 4 or not all(t.isdigit() for t in host.split('.')):
        ipv4 = socket.gethostbyname(host)

    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'curl/7.37.0')]
    resp = opener.open('http://ipinfo.io/%s' % ipv4)
    js = resp.read()

    obj = json.loads(js)
    p = lambda key: obj.get(key, '')
    location = ', '.join(
        [p(key) for key in ['city', 'region', 'country', 'postal'] if p(key)])

    d = {
        'ipv4': ipv4,
        'hostname': p('hostname'),
        'location': location,
        'owner': p('org'),
        }
    return d


def main(url):
    hostinfo = lookupHostInfo(url)

    print('IPv4:     ', hostinfo['ipv4'])
    print('Hostname: ', hostinfo['hostname'])
    print('Location: ', hostinfo['location'])
    print('Owner:    ', hostinfo['owner'])


if __name__ == '__main__':
    url = lget(sys.argv, 1)

    main(url)
