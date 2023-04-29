#Get Steam64 from Steam32

from steam.steamid import SteamID

idnum = '[U:1:89195940]'

print (SteamID(idnum).id)
print (SteamID(idnum).account_id)
print (SteamID(idnum).instance)
print (SteamID(idnum).type)
print (SteamID(idnum).universe)
print (SteamID(idnum).as_32)
print (SteamID(idnum).as_64)
print (SteamID(idnum).as_steam2)
print (SteamID(idnum).as_steam3)
print (SteamID(idnum).community_url)
print (SteamID(idnum).invite_url)