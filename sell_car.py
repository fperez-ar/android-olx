#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re, sys, os, time, subprocess
import ConfigParser
from com.dtmilano.android.viewclient import ViewClient
utf = 'utf-8'

_s = 1
main_activity = "com.olx.olx/.ui.activities.HomeActivity"

start_time = time.time()

##SETTINGS
config = ConfigParser.ConfigParser(allow_no_value=True)
config.read('config.cfg')

section = "car" #config.get("choose", "section")
title = unicode(config.get(section, "title"), utf)
price = config.get(section, "price")

category = unicode(config.get(section, "cat"), utf)
subcat   = unicode(config.get(section, "sub"), utf)

make       = config.get(section, "make")
model      = config.get(section, "model")
year       = config.get(section, "year")
condition  = config.get(section, "condition")
km         = config.get(section, "km")
sellr_type = config.get(section, "sellr_type")

kwargs1 = {'ignoreversioncheck': False, 'verbose': False, 'ignoresecuredevice': False}
device, serialno = ViewClient.connectToDeviceOrExit(**kwargs1)

kwargs2 = {'forceviewserveruse': False, 'useuiautomatorhelper': False, 'ignoreuiautomatorkilled': True, 'autodump': False, 'startviewserver': True, 'compresseddump': True}
vc = ViewClient(device, serialno, **kwargs2)

device.shell('input keyevent KEYCODE_HOME')
device.startActivity( main_activity )
vc.sleep(_s)
## STARTUP

# pantalla principal
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

print "elapsed", round(time.time() - start_time), "seconds"

# TODO: verificar que salga la ventana de categorias
if vc.findViewById('com.olx.olx:id/category_breadcrumb'):
 vc.findViewWithTextOrRaise( unicode(category, utf) ).touch()
 vc.dump(window=-1)
 vc.findViewWithTextOrRaise( unicode(subcat, utf) ).touch()
 vc.sleep(_s)

#pre-caching fields
vc.dump(window=-1)
make_field = vc.findViewWithTextOrRaise("Marca / Modelo")
year_field = vc.findViewWithTextOrRaise(u'Año')
condition_field = vc.findViewWithTextOrRaise(u'Condición')
publish_btn = vc.findViewByIdOrRaise('com.olx.olx:id/posting_publish_button')


# modelo / marca
make_field.touch()
vc.dump(window=-1)
vc.findViewWithTextOrRaise( unicode(make, utf) ).touch()
vc.dump(window=-1)
vc.findViewWithTextOrRaise( unicode(model, utf) ).touch()

#año
year_field.touch()
vc.dump(window=-1)
print "year selection not supported, selecting default year..."
vc.findViewByIdOrRaise('android:id/button1').touch()

#condicion
condition_field.touch()
vc.dump(window=-1)
vc.findViewWithTextOrRaise(condition).touch()

#kilometraje, si presente (depende de la condicion)
km_field = vc.findViewWithText(u'Kilometraje')
if km_field:
    print "km field found."
    km_field.touch()
    device.type(km)

#tipo de vendedor
vc.dump(window=-1)
vc.findViewWithTextOrRaise(u'Tipo de vendedor').touch()
vc.dump(window=-1)
vc.findViewWithTextOrRaise(sellr_type).touch()

publish_btn.touch()

print "Test took", round(time.time() - start_time), "seconds"
