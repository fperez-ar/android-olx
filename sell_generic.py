#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re, sys, os, time, subprocess
import ConfigParser
from com.dtmilano.android.viewclient import ViewClient

utf = 'utf-8'
_s = 0
main_activity = "com.olx.olx/.ui.activities.HomeActivity"

start_time = time.time()

##SETTINGS
config = ConfigParser.ConfigParser(allow_no_value=True)
config.read('config.cfg')

section = unicode( config.get("choose", "section"), utf)

title = config.get(section, "title")
price = config.get(section, "price")

category = unicode( config.get(section, "cat"), utf)
subcat   = unicode(config.get(section, "sub"), utf)

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

if vc.findViewById('com.olx.olx:id/retry_catalog'):
 print "connection fail modal appears, fff"
 vc.findViewByIdOrRaise('com.olx.olx:id/retry_catalog').touch()

## pantalla de elegir foto
vc.dump(window=-1)
vc.findViewByIdOrRaise('com.olx.olx:id/gridTile').touch() #primer elemento de la grilla
vc.dump(window=-1)
vc.findViewByIdOrRaise('com.olx.olx:id/select_photos').touch()
vc.dump(window=-1)

# pantalla de ingresar el titulo
vc.findViewByIdOrRaise('com.olx.olx:id/posting_title').setText( title )
vc.findViewByIdOrRaise('com.olx.olx:id/posting_title_button').touch()
# vc.sleep(_s)
vc.dump(window=-1)

# pantalla de ingresar el precio
vc.findViewByIdOrRaise('com.olx.olx:id/posting_price').setText( price )
vc.findViewByIdOrRaise('com.olx.olx:id/posting_price_button').touch()
vc.sleep(_s)
vc.dump(window=-1)

category_window = vc.findViewById('com.olx.olx:id/category_breadcrumb')
if vc.findViewById('com.olx.olx:id/category_breadcrumb'):
 category_selector = vc.findViewWithText( category )
 while not category_selector: #maybe you need to scroll...
  (x, y, w, h) = category_window.getPositionAndSize()
  start = ((x+w)/2, y+h)
  end = ((x+w)/2, y)
  device.drag(start, end, 30)
  vc.dump(window=-1)
  category_selector = vc.findViewWithText( category )

 category_selector.touch()
 vc.dump(window=-1)
 vc.findViewWithTextOrRaise( subcat ).touch()

vc.sleep(_s)
vc.dump(window=-1)
vc.findViewByIdOrRaise('com.olx.olx:id/posting_publish_button').touch()

print "Test took", time.time() - start_time, "seconds"
