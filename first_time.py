#FIRST TIME SETUP
apk_path = "app.apk"
package_name = "com.olx.olx"
main_activity = "com.olx.olx/.ui.activities.HomeActivity"

if apk_path:
 device.shell("pm clear "+package_name )
 subprocess.check_output( 'adb uninstall ' + package_name, shell=True )
 subprocess.check_output( 'adb install ' + apk_path, shell=True )
 device.startActivity( main_activity )
else:
 device.startActivity( main_activity )

################################################################################
#inicio
vc.dump(window=-1)
vc.findViewWithText(u'INICIO').touch()
# mapa
vc.dump(window=-1)
vc.findViewByIdOrRaise('id/no_id/7').setText("San Fernando del Valle de Catamarca, Catamarca")
vc.findViewByIdOrRaise('id/no_id/10').touch()
# login
vc.dump(window=-1)
vc.findViewByIdOrRaise('id/no_id/10').setText(usr)
vc.findViewByIdOrRaise('id/no_id/12').setText(psw)
vc.findViewByIdOrRaise('id/no_id/15').touch()
