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
eml = config.get("credentials", "email")
psw = config.get("credentials", "password")
section = config.get("choose", "section")
title = config.get(section, "title")
price = config.get(section, "price")
if section == "property":
    mts2 = config.get(section, "mts2")
    antq = unicode( config.get(section, "antq"), 'utf-8') #convert to unicode due to Ñ
    prop_type = config.get(section, "prop_type")
    sellr_type =  unicode( config.get(section, "sellr_type"), 'utf-8' )

kwargs1 = {'ignoreversioncheck': False, 'verbose': False, 'ignoresecuredevice': False}
device, serialno = ViewClient.connectToDeviceOrExit(**kwargs1)

kwargs2 = {'forceviewserveruse': False, 'useuiautomatorhelper': False, 'ignoreuiautomatorkilled': True, 'autodump': False, 'startviewserver': True, 'compresseddump': True}
vc = ViewClient(device, serialno, **kwargs2)

device.startActivity( main_activity )
vc.sleep(_s)
## STARTUP

# pantalla principal
vc.dump(window=-1)
vc.findViewWithTextOrRaise(u'Vender').touch()
vc.sleep(_s)
vc.dump(window=-1)


if vc.findViewWithText(u'¡Ups... Algo salió mal!'):
 print "connection fail modal appears, fff"
 vc.dump(window=-1)
 vc.findViewWithTextOrRaise(u'Volver a intentar').touch()



## pantalla de elegir foto
vc.findViewByIdOrRaise('id/no_id/11').touch() #primer elemento de la grilla
vc.dump(window=-1)
vc.findViewWithTextOrRaise(u'Usar fotos').touch()
# vc.sleep(_s)
vc.dump(window=-1)

# pantalla de ingresar el titulo
vc.findViewByIdOrRaise('id/no_id/8').setText( title ) #vc.findViewWithTextOrRaise(u'Título de tu aviso').setText( title )
vc.findViewWithTextOrRaise(u'Continuar').touch()
# vc.sleep(_s)
vc.dump(window=-1)

# pantalla de ingresar el precio
vc.findViewByIdOrRaise('id/no_id/8').setText( price ) #vc.findViewWithTextOrRaise(u'Indica cuanto cuesta').setText( price )
vc.findViewWithTextOrRaise(u'Continuar').touch()
# vc.sleep(_s)
vc.dump(window=-1)

# Pantalla de elegir categoria e informacion que depende de categoria
if section == "property":

 #tipo
 vc.findViewByIdOrRaise("id/no_id/12").touch()
 vc.dump(window=-1)
 vc.findViewWithTextOrRaise( prop_type ).touch()

 #mts2
 vc.dump(window=-1)
 #mts2_field = vc.findViewWithTextOrRaise(u'Metros Cuadrados Totales')
 #mts2_field.touch()
 #device.type("120")
 vc.findViewByIdOrRaise("id/no_id/25").setText( mts2 )

 device.drag((725, 600), (725, 200), 20)

 #antiguedad
 vc.dump(window=-1)
 vc.findViewByIdOrRaise("id/no_id/7").touch()
 vc.dump(window=-1)
 vc.findViewWithTextOrRaise( antq ).touch()
 vc.sleep(0.25)

 #tipo de vendedor
 vc.dump(window=-1)
 vc.findViewByIdOrRaise('id/no_id/12').touch()
 vc.dump(window=-1)
 vc.findViewWithTextOrRaise( sellr_type ).touch()

 vc.dump(window=-1)
 vc.findViewWithTextOrRaise(u'Publicar').touch()


print "Test took", time.time() - start_time, "seconds"
