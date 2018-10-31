# -*- coding: cp1254 -*-


import xbmc,xbmcgui,xbmcplugin,sys
icondir = xbmc.translatePath("https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/Gigs/Boxarts/")

plugin_handle = int(sys.argv[1])

def add_video_item(url, infolabels, img=''):
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem, isFolder=False)

# -*- coding: cp1254 -*-


import xbmc,xbmcgui,xbmcplugin,sys
icondir = xbmc.translatePath("https://raw.githubusercontent.com/EmuZONE/YouTube/master/Images/Gigs/Boxarts/")

plugin_handle = int(sys.argv[1])

def add_video_item(url, infolabels, img=''):
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem, isFolder=False)

add_video_item('https://archive.org/download/IndependentGigs/Nordwind%20-%20Donnerhall.ogv',{ 'title': 'Nordwind: Donnerhall'},img=icondir + 'Donnerhall.jpg')
add_video_item('https://archive.org/download/IndependentGigs/Kraftschlag%20-%20Live%20in%20Club%20Valhalla.mp4',{ 'title': 'Kraftschlag; Live in Club Valhalla 1996'},img=icondir + 'Kraftschlag.jpg')
add_video_item('https://archive.org/download/IndependentGigs/kriegsberichter%207.ogv',{ 'title': 'Kriegsberichter: Vol. VII'},img=icondir + 'Kriegsberichter7.jpg')
add_video_item('https://archive.org/download/OldGigsFrom90erVOL1/0815%20-%20Stinkende%20Zecke%20%28live%2012.02.1995%29.mpg',{ 'title': 'Nullacht Funfzehn: Stinkende Zecke'},img=icondir + 'zecke.jpg')
add_video_item('https://archive.org/download/OldGigsFrom90erVOL1/Skrewdriver%2CBrutal%20Attack%20%26%20No%20Remorse%20-%20Live%20in%20London%201988.avi',{ 'title': 'Skrewdriver: Live in England 1988'},img=icondir + 'Skrewdriver88.jpg')
add_video_item('https://archive.org/download/OldGigsFrom90erVOL1/Sweden%2015.04.1995-1.avi',{ 'title': 'Skinheads in Sweden 1995 Vol.1'},img=icondir + 'Sweden95-1.jpg')
add_video_item('https://archive.org/download/OldGigsFrom90erVOL1/Sweden%2015.04.1995-2.avi',{ 'title': 'Skinheads in Sweden 1995 Vol.2'},img=icondir + 'Sweden95-2.jpg')
add_video_item('https://archive.org/download/OldGigsFrom90erVOL2/Blue%20Eyed%20Devils%20-%20Live%202002.avi',{ 'title': 'Blue Eyed Devils'},img=icondir + 'Devils.jpg')
add_video_item('https://archive.org/download/OldGigsFrom90erVOL2/No%20Remorse%20-%20We%20Play%20For%20You.avi',{ 'title': 'No Remorse: We Play For You Concert'},img=icondir + 'NRwpfy.jpg')
add_video_item('https://archive.org/download/OldGigsFrom90erVOL3/Lunikoff.Live.2015.mkv',{ 'title': 'Lunikoff Verschworung 2015'},img=icondir + 'Lunikoff2015.jpg')
add_video_item('https://archive.org/download/KriegsberichterMAIN/Kriegsberichter_Vol.3.mp4',{ 'title': 'Kriegsberichter: Vol. III'},img=icondir + 'Kriegsberichter3.jpg')
add_video_item('https://archive.org/download/KriegsberichterMAIN/Kriegsberichter_Vol._6.mp4',{ 'title': 'Kriegsberichter: Vol. VI'},img=icondir + 'Kriegsberichter6.jpg')
add_video_item('https://raw.githubusercontent.com/EmuZONE/YouTube/master/HTML/Kriegsberichter.Vol.1.m3u',{ 'title': 'Kriegsberichter: Vol. I'},img=icondir + 'Kriegsberichter1.jpg')
add_video_item('https://raw.githubusercontent.com/EmuZONE/YouTube/master/HTML/Kriegsberichter.Vol.2.m3u',{ 'title': 'Kriegsberichter: Vol. II'},img=icondir + 'Kriegsberichter2.jpg')
add_video_item('https://raw.githubusercontent.com/EmuZONE/YouTube/master/HTML/Kriegsberichter.Vol.5.m3u',{ 'title': 'Kriegsberichter: Vol. V'},img=icondir + 'Kriegsberichter5.jpg')
add_video_item('https://raw.githubusercontent.com/EmuZONE/YouTube/master/HTML/buhc.m3u',{ 'title': 'Oswald Mosley Tribute London'},img=icondir + 'MosleyTribute2.jpg')
add_video_item('https://raw.githubusercontent.com/EmuZONE/YouTube/master/HTML/buhc.m3u',{ 'title': 'Skrewdriver in Germany 1992'},img=icondir + 'Skrewdriver92.jpg')
add_video_item('https://archive.org/download/OldGigsFrom90erVOL3/Greven%20-%20Live%202006.avi',{ 'title': 'Greven Live 2006'},img=icondir + 'Greven2006.jpg')
add_video_item('https://raw.githubusercontent.com/EmuZONE/YouTube/master/HTML/BullyBoys.m3u',{ 'title': 'Bully Boys + Fortress in Australia'},img=icondir + 'BullyBoys.jpg')
add_video_item('https://archive.org/download/OldGigsFrom90erVOL3/Daniel%20Eggers%20-%20Live%20in%20Guben%201996%20%282005%29%20DVDRip.avi',{ 'title': 'Daniel Eggers Live (Arisches Blut)'},img=icondir + 'ArishBlood.jpg')
add_video_item('https://archive.org/download/OldGigsFrom90erVOL3/Aryan%20Nations%20World%20Congress%202002.avi',{ 'title': 'Aryan Nations Congress 2002'},img=icondir + 'AryanNation2002.jpg')
add_video_item('https://archive.org/download/OldGigsFrom90erVOL3/Skrewdriver%20-%20Live%20in%20Germany%2010.07.1993.mpg',{ 'title': 'Ian Stuart - My last Days im Reich'},img=icondir + 'LastDaysSkrew93.jpg')
add_video_item('https://archive.org/download/OldGigsFrom90erVOL3/Oidoxie%20-%20Live%20in%20Krtetice%20(2005).avi',{ 'title': 'Oidoxie Live in Krtetice'},img=icondir + 'OidoxieKretice.jpg')


xbmcplugin.endOfDirectory(plugin_handle)
xbmc.executebuiltin("Container.SetViewMode(500)")

xbmcplugin.endOfDirectory(plugin_handle)
xbmc.executebuiltin("Container.SetViewMode(500)")