#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Copyright (C) 2013-2018  Diego Torres Milano
Created on 2018-03-27 by Culebra v14.0.0
                      __    __    __    __
                     /  \  /  \  /  \  /  \
____________________/  __\/  __\/  __\/  __\_____________________________
___________________/  /__/  /__/  /__/  /________________________________
                   | / \   / \   / \   / \   \___
                   |/   \_/   \_/   \_/   \    o \
                                           \_____/--<
@author: Diego Torres Milano
@author: Jennifer E. Swofford (ascii art snake)
'''


import re
import sys
import os

from com.dtmilano.android.viewclient import ViewClient

TAG = 'CULEBRA'

_s = 5
_v = '--verbose' in sys.argv


kwargs1 = {'ignoreversioncheck': False, 'verbose': False, 'ignoresecuredevice': False}
device, serialno = ViewClient.connectToDeviceOrExit(**kwargs1)
kwargs2 = {'forceviewserveruse': False, 'useuiautomatorhelper': False, 'ignoreuiautomatorkilled': True, 'autodump': False, 'startviewserver': True, 'compresseddump': True}
vc = ViewClient(device, serialno, **kwargs2)

vc.dump(window='-1')

no_id1 = vc.findViewByIdOrRaise("id/no_id/1")
com_olx_olx___id_left_drawer_layout = vc.findViewByIdOrRaise("com.olx.olx:id/left_drawer_layout")
no_id3 = vc.findViewByIdOrRaise("id/no_id/3")
no_id4 = vc.findViewByIdOrRaise("id/no_id/4")
no_id4 = vc.findViewWithContentDescriptionOrRaise(u'''Abrir''')
no_id5 = vc.findViewByIdOrRaise("id/no_id/5")
no_id5 = vc.findViewWithTextOrRaise(u'OLX')
com_olx_olx___id_search = vc.findViewByIdOrRaise("com.olx.olx:id/search")
com_olx_olx___id_search = vc.findViewWithContentDescriptionOrRaise(u'''Buscar''')

com_olx_olx___id_favorite_item = vc.findViewByIdOrRaise("com.olx.olx:id/favorite_item")
com_olx_olx___id_home_main_container = vc.findViewByIdOrRaise("com.olx.olx:id/home_main_container")
com_olx_olx___id_home_item_title = vc.findViewByIdOrRaise("com.olx.olx:id/home_item_title")
com_olx_olx___id_favorite_item = vc.findViewByIdOrRaise("com.olx.olx:id/favorite_item")
com_olx_olx___id_home_main_container = vc.findViewByIdOrRaise("com.olx.olx:id/home_main_container")
com_olx_olx___id_home_item_title = vc.findViewByIdOrRaise("com.olx.olx:id/home_item_title")

no_id24 = vc.findViewByIdOrRaise("id/no_id/24")
no_id25 = vc.findViewByIdOrRaise("id/no_id/25")
no_id26 = vc.findViewByIdOrRaise("id/no_id/26")
no_id27 = vc.findViewByIdOrRaise("id/no_id/27")
no_id28 = vc.findViewByIdOrRaise("id/no_id/28")
no_id29 = vc.findViewByIdOrRaise("id/no_id/29")
no_id30 = vc.findViewByIdOrRaise("id/no_id/30")

com_olx_olx___id_proximity_button = vc.findViewByIdOrRaise("com.olx.olx:id/proximity_button")
com_olx_olx___id_proximity = vc.findViewByIdOrRaise("com.olx.olx:id/proximity")

com_olx_olx___id_fab_posting_masonry_home = vc.findViewWithTextOrRaise(u'Vender')
