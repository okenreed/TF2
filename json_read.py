import json
import urllib.request
import mysql.connector

def load_data():
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'roken',
        password = 'Ellie.Ruth.1993',
        database = 'tf2_stats'
        )

    mycursor = mydb.cursor()

    mycursor.execute("USE tf2_stats")
    #mycursor.execute("CREATE TABLE games (game_id int, player_id VARCHAR(255), team VARCHAR(255), kills int, class VARCHAR(255), assists int, dmg int, deaths int)")

    url = urllib.request.urlopen('https://logs.tf/api/v1/log?player=76561198049461668&limit=10')
    game_list = json.loads(url.read().decode())

    for i in game_list['logs']:
        if (i['players'] != 12):
            continue
        game_id = (i['id'])

    #opens json from logs.tf api
        urlStr = 'https://logs.tf/api/v1/log/'
        urlStr += str(game_id)
        url2 = urllib.request.urlopen(urlStr)
        stats = json.loads(url2.read().decode())


    #Iterating through the JSON list
        for j in stats['players']:
            player_id = j
            team = stats['players'][j]['team']
            kills = stats['players'][j]['kills']
            playerClass = stats['players'][j]['class_stats'][0]['type']
            assists = stats['players'][j]['assists']
            dmg = stats['players'][j]['dmg']
            deaths = stats['players'][j]['deaths']
            sql = 'INSERT IGNORE INTO games (game_id, player_id, team, kills, class, assists, dmg, deaths) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
            val = (game_id, player_id, team, kills, playerClass, assists, dmg, deaths)
            mycursor.execute(sql, val)
            mydb.commit()

if __name__ == "__main__":
    load_data()