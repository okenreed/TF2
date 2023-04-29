from steam.steamid import SteamID

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'roken',
    password = 'Ellie.Ruth.1993',
    database = 'tf2_stats'
    )

mycursor = mydb.cursor()

mycursor.execute('USE tf2_stats')



sql = 'UPDATE games SET id64 = %s WHERE playerID = %s'
val = (id64, playerID)

SteamID(idnum).as_64