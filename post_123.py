def post_123(view_client, itle, price, cat, sub):

  view_client.dump(window=-1)
  if
  view_client.findViewByIdOrRaise('com.olx.olx:id/fab_posting_masonry_home')

  .touch()
  view_client.sleep(_s)

  view_client.dump(window=-1)
  if view_client.findViewWithText(u'¡Ups... Algo salió mal!'):
    print "connection fail modal appears, attempting again."
    view_client.dump(window=-1)
    view_client.findViewWithTextOrRaise(u'Volver a intentar').touch()

  view_client.findViewByIdOrRaise('com.olx.olx:id/gridTile').touch() #primer elemento de la grilla
  view_client.dump(window=-1)
  view_client.findViewByIdOrRaise('com.olx.olx:id/select_photos').touch()
  view_client.dump(window=-1)
