#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re, sys, os
import ConfigParser
from com.dtmilano.android.viewclient import ViewClient

TAG = 'CULEBRA'
_v = '--verbose' in sys.argv
_s = 0


##SETTINGS

apk_path = "app.apk"
package_name = "com.olx.olx"
main_activity = "com.olx.olx/.ui.activities.HomeActivity"

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
vc.dump(window=-1)


## STARTUP

if apk_path:
 device.shell("shell pm clear"+package_name )
 device.shell("uninstall "+package_name )
 device.shell("install "+apk_path )
# if you do a fresh install you'll need to navigate the login, location and tutorial screens
 vc.findViewWithTextOrRaise(u'INICIO')
 vc.findViewByIdOrRaise('id/no_id/10').setText(usr)
 vc.findViewByIdOrRaise('id/no_id/12').setText(psw)
 vc.findViewByIdOrRaise('id/no_id/15').touch()
device.startActivity( main_activity )

##SEQUENCE

# pantalla principal
vc.findViewWithTextOrRaise(u'Vender').touch()
vc.sleep(_s)
vc.dump(window=-1)


if vc.findViewWithText(u'¡Ups... Algo salió mal!'):
 print "connection fail modal appears, fff"
 vc.dump(window=-1)
 vc.findViewWithTextOrRaise(u'Volver a intentar').touch()
 quit()


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

#pantalla de elegir categoria e informacion
if section == "property":
 #tipo
 vc.findViewByIdOrRaise("id/no_id/12").touch()
 vc.dump(window=-1)
 vc.findViewWithTextOrRaise( prop_type ).touch()
 #mts2
 vc.dump(window=-1)
 #vc.findViewByIdOrRaise("id/no_id/22").touch()
 vc.findViewByIdOrRaise("id/no_id/23").setText( mts2 )
 #antiguedad
 vc.dump(window=-1)
 vc.findViewByIdOrRaise("id/no_id/24").touch()
 vc.dump(window=-1)
 vc.findViewWithTextOrRaise( antq ).touch()
 vc.sleep(0.25)
 device.drag((725, 600), (725, 200), 20)

 #tipo de vendedor
 vc.dump(window=-1)
 vc.findViewByIdOrRaise('id/no_id/12').touch()
 vc.dump(window=-1)
 vc.findViewWithTextOrRaise( sellr_type ).touch()

 vc.dump(window=-1)
 vc.findViewWithTextOrRaise(u'Publicar').touch()
