#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re, sys, os, time, subprocess
import ConfigParser
from com.dtmilano.android.viewclient import ViewClient

_s = 0
main_activity = "com.olx.olx/.ui.activities.HomeActivity"

start_time = time.time()

##SETTINGS
config = ConfigParser.ConfigParser(allow_no_value=True)
config.read('config.cfg')

section = config.get("choose", "section")
title = config.get(section, "title")
price = config.get(section, "price")

category = config.get(section, "cat")
subcat   = config.get(section, "sub")

kwargs1 = {'ignoreversioncheck': False, 'verbose': False, 'ignoresecuredevice': False}
device, serialno = ViewClient.connectToDeviceOrExit(**kwargs1)

kwargs2 = {'forceviewserveruse': False, 'useuiautomatorhelper': False, 'ignoreuiautomatorkilled': True, 'autodump': False, 'startviewserver': True, 'compresseddump': True}
vc = ViewClient(device, serialno, **kwargs2)

device.startActivity( main_activity )
vc.sleep(_s)

## STARTUP
vc.dump(window=-1)
vc.findViewByIdOrRaise('com.olx.olx:id/fab_posting_masonry_home').touch()
vc.sleep(_s)
vc.dump(window=-1)

if vc.findViewWithText(u'¡Ups... Algo salió mal!'):
 print "connection fail modal appears, fff"
 vc.dump(window=-1)
 vc.findViewWithTextOrRaise(u'Volver a intentar').touch()

## pantalla de elegir foto
vc.findViewByIdOrRaise('com.olx.olx:id/gridTile').touch() #primer elemento de la grilla
vc.dump(window=-1)
vc.findViewByIdOrRaise('com.olx.olx:id/select_photos').touch()
# vc.sleep(_s)
vc.dump(window=-1)

# pantalla de ingresar el titulo
vc.findViewByIdOrRaise('com.olx.olx:id/posting_title').setText( title )
vc.findViewByIdOrRaise('com.olx.olx:id/posting_title_button').touch()
# vc.sleep(_s)
vc.dump(window=-1)

# pantalla de ingresar el precio
vc.findViewByIdOrRaise('com.olx.olx:id/posting_price').setText( price )
vc.findViewByIdOrRaise('com.olx.olx:id/posting_price_button').touch()
# vc.sleep(_s)
vc.dump(window=-1)


# TODO: verificar que salga la ventana de categorias

vc.findViewWithTextOrRaise( unicode(category, 'utf-8') ).touch()
vc.dump(window=-1)
vc.findViewWithTextOrRaise( unicode(subcat, 'utf-8') ).touch()

vc.sleep(_s)
vc.dump(window=-1)
vc.findViewByIdOrRaise('com.olx.olx:id/posting_publish_button').touch()

print "Test took", time.time() - start_time, "seconds"
