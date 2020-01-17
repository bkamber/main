#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def build():
    # fix AttributeError
    pisitools.dosed("sanic/testing.py", "httpx.dispatch.ASGIDispatch", "httpx.ASGIDispatch")
    pythonmodules.compile(pyVer="3")

def install():
    pythonmodules.install(pyVer="3")